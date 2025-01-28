python
import requests
import pandas as pd
import matplotlib.pyplot as plt

def fetch_air_quality_data():
    url = 'https://api.example.com/air-quality-abu-dhabi'
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data)

def fetch_public_transportation_data():
    url = 'https://api.example.com/public-transportation-abu-dhabi'
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data)

def visualize_air_quality(df):
    plt.figure(figsize=(10, 6))
    df.plot(x='timestamp', y=['PM2.5', 'NO2', 'O3'], kind='line')
    plt.title('Air Quality Index Over Time')
    plt.xlabel('Time')
    plt.ylabel('AQI Levels')
    plt.show()

def visualize_transportation_usage(df):
    plt.figure(figsize=(10, 6))
    df.groupby('month')['passenger_count'].sum().plot(kind='bar')
    plt.title('Monthly Public Transportation Usage')
    plt.xlabel('Month')
    plt.ylabel('Passenger Count')
    plt.show()

air_quality_df = fetch_air_quality_data()
public_transportation_df = fetch_public_transportation_data()

visualize_air_quality(air_quality_df)
visualize_transportation_usage(public_transportation_df)
