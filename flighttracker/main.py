# import libraries
import requests
import json
from bs4 import BeautifulSoup
import pandas as pd

# Area extent of the search
lon_min, lat_min = -125.974, 30.038
lon_max, lat_max = -68.748, 52.214

# Rest API Query
# user_name = ''
# password = ''
url = 'https://opensky-network.org/api/states/all'
url_data = f'https://opensky-network.org/api/states/all?lamin={lat_min}&lomin={lon_min}&lamax={lat_max}&lomax={lon_max}'
response = requests.get(url_data).json()

# Load to a Pandas dataframe
col_name = ['icao24', 'callsign', 'origin_country', 'time_position', 'last_contact', 'baro_altitude', 'on_ground', 'velocity',
            'true_track', 'vertical_rate', 'sensors', 'geo_altitude', 'squawk', 'spi', 'position_source']
flight_df = pd.DataFrame(response['states'])
flight_df = flight_df.loc[ : , 0:16]
flight_df.columns = col_name
flight_df = flight_df.fillna('No Data')
flight_df.head()