from flask import Flask, jsonify
import requests
from flask_cors import CORS  # Import the CORS module

app = Flask(__name__)
cors = CORS(app, supports_credentials=True)  # Enable CORS for all routes


# Your existing route
@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    api_url = 'http://127.0.0.1:5001/api'  # Correct the URL to match the /api route

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

        json_data = response.json()
        return jsonify(json_data)

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Request to {api_url} failed: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(debug=True, port=8000)
