import requests


url = "https://api.openweathermap.org/data/2.5/weather?q=Almaty&appid=&units=metric"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: Unable to fetch data, status code {response.status_code}")
