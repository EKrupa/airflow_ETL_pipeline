import requests

def fetch_data():
    url = "http://api.citybik.es/v2/networks"
    response = requests.get(url)
    response.raise_for_status()  
    return response.json()

def fetch_network_details(network_id):
    url = f"http://api.citybik.es/v2/networks/{network_id}"
    response = requests.get(url)
    response.raise_for_status()  
    return response.json()['network']


def get_top_stations_for_network(network, top_n=5):
    stations = network['stations']
    stations_sorted = sorted(stations, key=lambda s: s['free_bikes'], reverse=True)
    

    top_stations = [
    {
        'network_id': network['id'],
        'network_name': network['name'],
        'station_id': s['id'],
        'station_name': s['name'],
        'free_bikes': s['free_bikes'],
        'empty_slots': s['empty_slots'],
        'latitude': s['latitude'],
        'longitude': s['longitude']
    }
    
    for s in stations_sorted[:top_n]
    ]
    return top_stations

def get_top_stations_all_networks(top_n=5):
    networks = fetch_data()
    all_top_stations = []

    for network_info in networks['networks']:
        network_id = network_info['id']
        network_details = fetch_network_details(network_id)
        top_stations = get_top_stations_for_network(network_details, top_n)
        all_top_stations.extend(top_stations)

    return all_top_stations

if __name__ == "__main__":
    top_stations = get_top_stations_all_networks(top_n=5)
    print(top_stations)