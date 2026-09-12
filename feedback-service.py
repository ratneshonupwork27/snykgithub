import requests

# ❌ EXPOSED SECRET: Never hardcode sensitive keys directly in your scripts!
API_KEY = "secret_5ebe2294ecd0e0f08eab7690d2a6ee69" 

def get_weather_data(city):
    url = f"https://weatherprovider.com{city}&key={API_KEY}"
    response = requests.get(url)
    return response.json()
