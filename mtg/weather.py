#!/usr/bin/env python3
import requests
import pandas as pd
from datetime import datetime, timezone, timedelta

# Function to get weather data from NWS API
def get_weather_data(station_id):
    url = f"https://api.weather.gov/stations/{station_id}/observations/latest"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to format and display weather data
def display_weather_data(data):
    if data:
        # Extract the weather data properties
        properties = data['properties']
        
        # Convert temperature from Celsius to Fahrenheit
        temperature_c = properties['temperature']['value']
        temperature_f = (temperature_c * 9/5) + 32 if temperature_c is not None else None
        
        dewpoint_c = properties['dewpoint']['value']
        dewpoint_f = (dewpoint_c * 9/5) + 32 if dewpoint_c is not None else None
        
        # Convert UTC time to PST
        timestamp_utc = datetime.strptime(properties['timestamp'], "%Y-%m-%dT%H:%M:%S+00:00")
        pst_offset = timedelta(hours=-8)  # PST is UTC-8
        timestamp_pst = timestamp_utc + pst_offset
        formatted_timestamp_pst = timestamp_pst.strftime("%Y-%m-%d %H:%M:%S PST")

        weather_data = {
            'Temperature (F)': temperature_f,
            'Humidity (%)': properties['relativeHumidity']['value'],
            'Wind Speed (mph)': properties['windSpeed']['value'] * 0.621371 if properties['windSpeed']['value'] is not None else None,  # Convert from m/s to mph
            'Wind Direction': properties['windDirection']['value'],
            'Pressure (mb)': properties['barometricPressure']['value'] / 100 if 'barometricPressure' in properties and properties['barometricPressure']['value'] is not None else None,  # Convert from Pa to mb
            'Dew Point (F)': dewpoint_f,
            'Visibility (mi)': properties['visibility']['value'] / 1609.34 if properties['visibility']['value'] is not None else None,  # Convert from meters to miles
            'Updated At': formatted_timestamp_pst
        }
        
        # Create a DataFrame from the weather data
        df = pd.DataFrame([weather_data])
        print(df)
    else:
        print("Failed to retrieve weather data.")

# Main function
def main():
    station_id = "KCLS" #"KEAT"  # Pangborn Memorial Airport (East Wenatchee)
    weather_data = get_weather_data(station_id)
    display_weather_data(weather_data)

if __name__ == "__main__":
    main()

