import requests,os
from dotenv import load_dotenv
load_dotenv()
city_name = 'kerala'
API_key=os.getenv("API_KEY")
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
    print('weather is',data['weather'][0]['description'])
    print('current Temperature is',data['main']['temp'])
    print('current Temperature Feels like is',data['main']['feels_like'])
    print('Humidity is',data['main']['humidity'])
else:
    print("Error:",response.status_code)

