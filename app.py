from flask import Flask, jsonify, request
import requests
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

# Define your OpenMeteo API endpoint
OPENMETEO_API_URL = "https://api.open-meteo.com/v1/forecast"

@app.route('/weather', methods=['GET'])
@cross_origin()
def get_weather():
    # Get the 'days' parameter from the query (default to 7 if not provided)
    days = request.args.get('days', default=7, type=int)
    
    # Parameters for the OpenMeteo API request
    params = {
        'latitude': 52.52,  # Berlin example
        'longitude': 13.405,
        'current_weather': True,
        'hourly': 'temperature_2m,precipitation',
        'forecast_days': days  # Specify the number of forecast days
    }

    try:
        # Make the request to OpenMeteo API
        response = requests.get(OPENMETEO_API_URL, params=params)
        response.raise_for_status()
        weather_data = response.json()

        # Return the fetched weather data as JSON
        return jsonify(weather_data), 200

    except requests.exceptions.RequestException as e:
        # Handle any API request errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
