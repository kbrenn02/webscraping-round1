import requests
import pandas as pd
import time


# This functions sends GET request to the OpenSky API to fetch the current states of all aircraft (as noted by 'all' in url). 
# Checks if there is an error in fetching data or if the data is empty
def fetch_opensky_data():
    url = "https://opensky-network.org/api/states/all"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data from OpenSky API: {e}")
        return None

    data = response.json()

    if data['states'] is None:
        print("No aircraft data available at this time.")
        return None
    
    return data


# takes raw data from the fetch and puts it in a Pandas dataframe (and adds a timestamp)
def process_data(data):
    columns = [
        "icao24", "callsign", "origin_country", "time_position", "last_contact",
        "longitude", "latitude", "baro_altitude", "on_ground", "velocity",
        "true_track", "vertical_rate", "sensors", "geo_altitude", "squawk",
        "spi", "position_source"
    ]

    df = pd.DataFrame(data['states'], columns=columns)
    df['timestamp'] = data['time']
    return df


# Pretty self explanatory -- saves the dataframe to a CSV file
def save_to_csv(df, filename):
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")


# organizing fetching, cleaning, and exporting of data
def main():
    print("Fetching data from OpenSky Network API...")
    #fetch data
    data = fetch_opensky_data()
    
    if data:
        # if data exists, processes the data
        df = process_data(data)
        # generate a timestamp to create a unique filename
        timestamp = time.strftime('%Y%m%d_%H%M%S', time.gmtime(data['time']))
        filename = f"opensky_data_{timestamp}.csv"
        # save to csv using the above created file name
        save_to_csv(df, filename)

if __name__ == "__main__":
    main()