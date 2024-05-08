import requests
import logging

# Set up logging you can switch to print if you want a simpler script
logging.basicConfig(level=logging.INFO)

# Define the API key and address
API_KEY = "YOUR_API_KEY"
ADDRESS = "123 Main St, Toronto, ON M5A 1A1"


def get_canada_post_address_complete_api(api_key, address):
    """
    This function uses the Canada Post API to retrieve a complete address for a given address and postal code.

    Parameters:
        api_key (str): Your Canada Post API key.
        address (str): The address for which you want to retrieve the complete address.

    Returns:
        address_data (dict): A dictionary containing the complete address fields.
    """
    url = "https://ws1.postescanada-canadapost.ca/AddressComplete/Interactive/Find/v2.30/json3.ws"
    params = {
        'Key': api_key,
        'SearchFor': 'Everything',
        'Country': 'CAN',
        'SearchTerm': address,
        'LastId': '',
        'MaxSuggestions': '10',
        'MaxResults': '10'
    }

    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        response_data = response.json()

        # Check if there are any items in the response
        if response_data['Items']:
            # Extract the address data from the first item
            address_data = response_data['Items'][0]
            return address_data
        else:
            logging.warning("No address data found.")
            return None
    else:
        # Handle API error response
        logging.error(f"API request failed with status code {response.status_code}.")
        return None


# Call the function to get the complete address
address_data = get_canada_post_address_complete_api(API_KEY, ADDRESS)

# Log the complete address data
if address_data is not None:
    logging.info(address_data)
