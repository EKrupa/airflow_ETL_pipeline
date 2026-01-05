import pandas as pd
from etl.extract import fetch_data
from etl.extract import fetch_network_details

def transform_networks(data):
    df = pd.DataFrame(data["networks"])
    df = df.drop_duplicates()
    return [
        {"name": network["name"],
         "city": network["location"]["city"]
         }
         for network in df.to_dict(orient="records")
    ]

if __name__ == "__main__":
    raw_data = fetch_data()
    transformed = transform_networks(raw_data)
    print(transformed)



def get_network_id_by_name(name):
    data = fetch_data()
    for network in data["networks"]:
        if network["name"].lower() == name.lower():
            return network["id"]
    return None

def transform_stations(network_id):
    data = fetch_network_details(network_id)
    stations = data["network"]["stations"]
    df = pd.DataFrame(stations)
    df["bikes_per_station"] = df["free_bikes"]
    return df


def most_bikes_station(df):
    return df.loc[df["bikes_per_station"].idxmax()]

