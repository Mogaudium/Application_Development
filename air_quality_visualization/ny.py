import requests
import pandas as pd
from datetime import datetime, timedelta

def get_aqi_data(city, start_date, end_date):
    url = f'https://api.openaq.org/v2/measurements?city={city}&date_from={start_date}&date_to={end_date}&parameter=pm25&limit=10000'
    response = requests.get(url)
    data = response.json()

    if data['meta']['found'] == 0:
        return None

    aqi_data_list = []

    for result in data['results']:
        aqi_data = {
            'date': result['date']['utc'],
            'location': result['location'],
            'aqi': result['value'],
            'parameter': result['parameter']
        }
        aqi_data_list.append(aqi_data)

    return aqi_data_list

def save_aqi_data_to_csv(aqi_data_list, output_file='ny_aqi_data.csv'):
    df = pd.DataFrame(aqi_data_list)
    df.to_csv(output_file, index=False)

if __name__ == '__main__':
    city = 'New York'  # Changed from 'Los Angeles' to 'New York'
    start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    end_date = datetime.now().strftime('%Y-%m-%d')

    aqi_data_list = get_aqi_data(city, start_date, end_date)

    if aqi_data_list:
        save_aqi_data_to_csv(aqi_data_list)
        print(f'Saved AQI data for {city} to aqi_data.csv')
    else:
        print(f'Failed to download AQI data for {city}')
