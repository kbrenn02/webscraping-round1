# import libraries
import requests
import json
from bs4 import BeautifulSoup
import pandas as pd

# Area extent of the search
lon_min,lat_min=-125.974,30.038
lon_max,lat_max=-68.748,52.214

# Rest API Query
url = f'https://opensky-network.org/api/states/all?lamin={lat_min}&lomin={lon_min}&lamax={lat_max}&lomax={lon_max}'
response1 = requests.get(url)
response2 = requests.get(url).json()
if (response1.status_code == 200):
    html_content = response1.text
    print('Successful')
else:
    print(f"Failed to retrieve the web page. Status code: {response1.status_code}")

# Parse HTML using beautiful soup
soup = BeautifulSoup(html_content, 'html.parser')


# Load to a Pandas dataframe
col_name = ['icao24', 'callsign', 'origin_country', 'time_position', 'last_contact', 'baro_altitude', 'on_ground', 'velocity',
            'true_track', 'vertical_rate', 'sensors', 'geo_altitude', 'squawk', 'spi', 'position_source']
flight_df = pd.DataFrame(response2['states'])
print('test1')
print(response2)
print('test2')
print(response2['states'])
print(flight_df.shape)
print(flight_df.head())
# flight_df = flight_df.loc[ : , 0:16]
# flight_df.columns = col_name
# flight_df = flight_df.fillna('No Data')
# flight_df.head()