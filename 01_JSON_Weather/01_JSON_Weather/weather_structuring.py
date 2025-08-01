import json
import pandas as pd

with open('weather.json') as f:
    data = json.load(f)

records = []
for item in data['list']:
    records.append({
        'City': data['city']['name'],
        'Country': data['city']['country'],
        'DateTime': item['dt_txt'],
        'Temperature (K)': item['main']['temp'],
        'Humidity (%)': item['main']['humidity'],
        'Weather': item['weather'][0]['main'],
        'Description': item['weather'][0]['description']
    })

df = pd.DataFrame(records)
print(df)
