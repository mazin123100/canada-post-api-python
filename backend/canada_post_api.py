import requests
import xml.etree.ElementTree as ET

# Constants
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://ws1.postescanada-canadapost.ca/AddressComplete/Interactive/Retrieve/v2.11/wsdlnew.ws"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/vnd.cpc.ship.rate-v2+xml"
}
NAMESPACE = {"ns": "http://www.canadapost.ca/ws/ship/rate-v2"}

def create_request_body(api_key):
    """
    Create the XML request body.
    """
    return f"""
    <?xml version="1.0" encoding="UTF-8"?>
    <mail-item xmlns="http://www.canadapost.ca/ws/ship/rate-v2">
        <customer-number>{api_key}</customer-number>
        <parcel-characteristics>
            <weight>1.0</weight>
            <length>20.0</length>
            <width>20.0</width>
            <height>20.0</height>
        </parcel-characteristics>
        <services>
            <service-code>DOM.EP</service-code>
        </services>
        <origin-postal-code>K1A0B1</origin-postal-code>
        <destination>
            <postal-code>M5A4B6</postal-code>
        </destination>
    </mail-item>
    """

def send_request(url, headers, body):
    """
    Send a POST request to the specified URL with the given headers and body.
    """
    return requests.post(url, headers=headers, data=body)

def parse_response(response):
    """
    Parse the XML response and print the shipping rates and estimated delivery times.
    """
    root = ET.fromstring(response.text)
    for rate in root.findall(".//ns:rate", NAMESPACE):
        service_name = rate.find("ns:service-name", NAMESPACE).text
        service_code = rate.find("ns:service-code", NAMESPACE).text
        price = rate.find("ns:price", NAMESPACE).text
        estimated_delivery_date = rate.find("ns:expected-delivery-date", NAMESPACE).text

        print(f"Service: {service_name} ({service_code})")
        print(f"Price: {price}")
        print(f"Estimated Delivery Date: {estimated_delivery_date}")
        print()

def main():
    """
    Main function to send the request and parse the response.
    """
    request_body = create_request_body(API_KEY)
    response = send_request(BASE_URL, HEADERS, request_body)
    parse_response(response)

if __name__ == "__main__":
    main()
