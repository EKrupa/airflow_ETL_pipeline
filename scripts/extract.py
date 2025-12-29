import requests

def fetch_data():
    url = "http://api.citybik.es/v2/networks"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

def fetch_network_details(network_id):
    url = f"http://api.citybik.es/v2/networks/{network_id}"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

data = fetch_data()