🌦️ Weather App (Python)

This is a simple Python script that fetches current weather data for a city using the OpenWeatherMap API.

🚀 Features

Fetches real-time weather data

Shows:

Weather description

Current temperature

Feels-like temperature

Humidity

Uses environment variables to keep the API key secure

🛠️ Requirements

Make sure you have Python installed (Python 3.7+ recommended).

Install the required libraries:

pip install requests python-dotenv

📂 Project Structure
weather-app/
│
├── weather.py
├── .env
└── README.md

🔑 API Key Setup

Create an account on OpenWeatherMap

Get your API key

Create a .env file in the project folder

Add your API key like this:

API_KEY=your_api_key_here


⚠️ Do not share your API key publicly

🧪 How to Run

Edit the city name in the script (use a valid city, not a state):

city_name = "Kochi"

Run the script:

python weather.py

📌 Example Output
weather is overcast clouds
current Temperature is 30.82
current Temperature Feels like is 30.97
Humidity is 42
