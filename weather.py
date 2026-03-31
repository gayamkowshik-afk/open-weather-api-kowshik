import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API key not found. Please set API_KEY in .env file")

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

# Handle responses properly
if response.status_code == 200:
    data = response.json()
    
    temperature = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {weather}")

elif response.status_code == 429:
    print("Rate limit exceeded. Please try again later.")

elif response.status_code == 404:
    print("City not found. Check spelling.")

else:
    print(f"API Error: {response.status_code}")

# Do not log user location data to protect privacy.
# Logging city names may violate GDPR data minimization principle.
