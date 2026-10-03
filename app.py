import os

import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/weather")
def get_weather():
    city = request.args.get("city", "").strip()

    if not city:
        return jsonify({"error": "Please enter a city name."}), 400

    try:
        response = requests.get(
            BASE_URL,
            params={"q": city, "appid": API_KEY, "units": "metric"},
            timeout=5,
        )
    except requests.exceptions.RequestException:
        return jsonify({"error": "Network error. Please check your connection and try again."}), 503

    if response.status_code == 401:
        return jsonify({"error": "Invalid or inactive API key."}), 401
    if response.status_code == 404:
        return jsonify({"error": f'City "{city}" not found.'}), 404
    if response.status_code != 200:
        return jsonify({"error": "Unable to fetch weather data. Please try again."}), response.status_code

    data = response.json()

    temp_c = data["main"]["temp"]
    feels_like_c = data["main"]["feels_like"]

    result = {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temp_c": round(temp_c, 1),
        "temp_f": round(temp_c * 9 / 5 + 32, 1),
        "feels_like_c": round(feels_like_c, 1),
        "feels_like_f": round(feels_like_c * 9 / 5 + 32, 1),
        "description": data["weather"][0]["description"].capitalize(),
        "icon": data["weather"][0]["icon"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
