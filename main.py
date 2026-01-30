import requests


url = "https://api.openweathermap.org/data/2.5/weather?q=Almaty&appid=642b3173fcc6a322df6069624acc1e0a&units=metric"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: Unable to fetch data, status code {response.status_code}")