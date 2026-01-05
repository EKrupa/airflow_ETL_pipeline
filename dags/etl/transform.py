import pandas as pd
from etl.extract import fetch_data
from etl.extract import fetch_network_details

#clean station data returns top stations
def transform_networks(network_details, top_n=5):
    stations = network_details['stations']
    df = pd.DataFrame(stations)
    
    df['free_bikes'] = df['free_bikes'].fillna(0).astype(int)
    df['empty_slots'] = df['empty_slots'].fillna(0).astype(int)
    df['latitude'] = df['latitude'].astype(float)
    df['longitude'] = df['longitude'].astype(float)

    df['total_slots'] = df['free_bikes'] + df['empty_slots']
    df['availability_ratio'] = df.apply(
        lambda row: row['free_bikes'] / row['total_slots'] if row['total_slots'] > 0 else 0, axis=1
    )
    df['network_id'] = network_details['id']
    df['network_name'] = network_details['name']

    #sort free bikes, keep top n
    df_sorted = df.sort_values(by='free_bikes', ascending=False).head(top_n)

    return df_sorted

def transform_top_stations_all_networks(top_n=5):
    networks = fetch_data()['networks']
    all_top_stations = []

    for network_info in networks:
        network_id = network_info['id']
        network_details = fetch_network_details(network_id)
        top_stations = transform_networks(network_details, top_n)
        all_top_stations.append(top_stations)

    combine_df = pd.concat(all_top_stations, ingnore_index=True)
    return combine_df