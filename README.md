# canada-post-api-python
This repository contains a Python-based prototype for interacting with the Canada Post API, alongside Vue.js 3
# Canada Post API Python Script

This script uses the Canada Post API to retrieve shipping rates and estimate delivery times. It also includes a Vue.js frontend to interact with the API.

**Installation**

To install the required dependencies, run the following command:
pip install -r requirements.txt

**Usage**

To use the script, you'll need to replace `YOUR_API_KEY` with your actual Canada Post API key.

1. Run the script using Python: `python canada_post_api.py`
2. Open a web browser and navigate to `http://localhost:8080` to interact with the Vue.js frontend.

**Code Explanation**

The script uses the `requests` library to send a POST request to the Canada Post API with the required XML data. The API returns a response in XML format, which is parsed using the `xml.etree.ElementTree` library.

The script then extracts the shipping rates and estimated delivery times from the XML response and prints them to the console.

The Vue.js frontend is used to interact with the API and display the shipping rates and estimated delivery times. The frontend sends a POST request to the API with the required data and receives the response in XML format, which is then parsed and displayed on the page.

**Requirements**

* Python 3.7 or higher
* `requests` library
* `xml.etree.ElementTree` library
* Vue.js 3.x or higher
* Node.js 14.x or higher
* requests==2.25.1
* xml.etree.ElementTree==1.4.7
