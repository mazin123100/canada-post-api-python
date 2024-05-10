from flask import Flask, jsonify, request
import requests
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the API key and endpoint
API_KEY = "YOUR_API_KEY"
API_URL = "https://ws1.postescanada-canadapost.ca/AddressComplete/Interactive/Find/v2.30/json3.ws"

app = Flask(__name__)


@app.route('/complete_address', methods=['POST'])
def get_address():
    # Get the address from the request data
    address = request.json.get('address', None)
    # If no address is provided, return an error
    if not address:
        return jsonify({'error': 'No address provided'}), 400

    # Get the complete address data from the Canada Post API
    address_data = get_canada_post_address_complete_api(API_KEY, address)
    # If address data is found, return it
    if address_data is not None:
        return jsonify(address_data)
    # If no address data is found, return an error
    else:
        return jsonify({'error': 'No address data found'}), 404


def get_canada_post_address_complete_api(api_key, address):
    # Define the parameters for the API request
    params = {
        'Key': api_key,
        'SearchFor': 'Everything',
        'Country': 'CAN',
        'SearchTerm': address,
        'LastId': '',
        'MaxSuggestions': '10',
        'MaxResults': '10'
    }

    # Make the API request
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        # Log any errors that occur during the API request
        logging.error(f"API request failed: {err}")
        return None

    # Parse the response data
    response_data = response.json()
    # If address data is found, return it
    if response_data['Items']:
        return response_data['Items'][0]
    # If no address data is found, log a warning and return None
    else:
        logging.warning("No address data found.")
        return None


# Only run the Flask development server if the script is run directly
if __name__ == "__main__":
    app.run(debug=True)
