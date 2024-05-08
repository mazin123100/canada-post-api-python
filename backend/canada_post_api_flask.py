from flask import Flask, jsonify
import requests
import xml.etree.ElementTree as ET

# Create a new Flask web server instance
app = Flask(__name__)

# Define your Canada Post API key, API URL, and headers
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://ws1.postescanada-canadapost.ca/AddressComplete/Interactive/Retrieve/v2.11/wsdlnew.ws"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/vnd.cpc.ship.rate-v2+xml"
}

# Define the XML namespace used in the response
NAMESPACE = {"ns": "http://www.canadapost.ca/ws/ship/rate-v2"}


def create_request_body(api_key):
    """
    This function creates the XML request body that will be sent to the Canada Post API.

    Parameters:
    api_key (str): The API key for the Canada Post API.

    Returns:
    str: The XML request body as a string.
    """
    return f"""
    <!-- The XML request body starts here -->
    <?xml version="1.0" encoding="UTF-8"?>
    <mail-item xmlns="http://www.canadapost.ca/ws/ship/rate-v2">
        <!-- The customer number is your API key -->
        <customer-number>{api_key}</customer-number>
        <!-- The parcel characteristics like weight, length, width, and height -->
        <parcel-characteristics>
            <weight>1.0</weight>
            <length>20.0</length>
            <width>20.0</width>
            <height>20.0</height>
        </parcel-characteristics>
        <!-- The service code -->
        <services>
            <service-code>DOM.EP</service-code>
        </services>
        <!-- The origin postal code -->
        <origin-postal-code>K1A0B1</origin-postal-code>
        <!-- The destination postal code -->
        <destination>
            <postal-code>M5A4B6</postal-code>
        </destination>
    </mail-item>
    <!-- The XML request body ends here -->
    """



def send_request(url, headers, body):
    """
    Function to send a POST request to the specified URL with the given headers and body.
    """
    return requests.post(url, headers=headers, data=body)


def parse_response(response):
    """
    Function to parse the XML response and return the shipping rates and estimated delivery times.
    """
    root = ET.fromstring(response.text)
    rates = []
    # Loop over each 'rate' element in the response
    for rate in root.findall(".//ns:rate", NAMESPACE):
        # Extract the service name, service code, price, and estimated delivery date
        service_name = rate.find("ns:service-name", NAMESPACE).text
        service_code = rate.find("ns:service-code", NAMESPACE).text
        price = rate.find("ns:price", NAMESPACE).text
        estimated_delivery_date = rate.find("ns:expected-delivery-date", NAMESPACE).text

        # Append the rate info to the 'rates' list
        rates.append({
            "service_name": service_name,
            "service_code": service_code,
            "price": price,
            "estimated_delivery_date": estimated_delivery_date
        })

    # Return the list of rates
    return rates


@app.route('/api/rates', methods=['POST'])
def get_rates():
    """
    Endpoint to fetch shipping rates. When a POST request is made to this endpoint,
    it sends a request to the Canada Post API, parses the response, and returns the rates.
    """
    # Create the request body, send the request, and parse the response
    request_body = create_request_body(API_KEY)
    response = send_request(BASE_URL, HEADERS, request_body)
    rates = parse_response(response)

    # Return the rates as a JSON response
    return jsonify(rates)

