# Weather App

A simple weather lookup web app built with Flask and the OpenWeatherMap
Current Weather API.

## How it works

- **`app.py`** – Flask backend. The `/` route renders the page. The
  `/api/weather` route reads a `city` query parameter, sends a GET request
  to OpenWeatherMap's Current Weather API with your API key, and returns the
  relevant fields (temperature, feels-like, description, icon, humidity,
  wind speed) as JSON. It also maps OpenWeatherMap error responses (401, 404)
  and network failures to clear error messages.
- **`templates/index.html`** – The page markup: a form with a city input and
  a "Get weather" button, an error message area, and a result section.
- **`static/script.js`** – Handles the form submit: validates the input
  client-side, calls `/api/weather`, and renders the result or error.
- **`static/style.css`** – Styling for the page.
- **`.env`** (not committed) – Holds `OPENWEATHER_API_KEY`, loaded via
  `python-dotenv` so the key is never hard-coded in the source.

## Setup

1. Create a virtual environment and install dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Copy `.env.example` to `.env` and add your OpenWeatherMap API key:

   ```bash
   cp .env.example .env
   ```

3. Run the app:

   ```bash
   python app.py
   ```

4. Open http://localhost:5000 in your browser.

## Notes

- Get a free API key at https://openweathermap.org/api. New keys can take
  up to a couple of hours to activate — until then, requests will return a
  401 error, which the app surfaces as "Invalid or inactive API key."
