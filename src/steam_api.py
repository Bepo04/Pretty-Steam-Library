import requests
import json

def get_steam_library(steam_api_key, steam_id):
    # Base URL to get library games
    url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001"
    params = {
        "key": steam_api_key,
        "steamid" : steam_id,
        "format" : "json",
        "include_appinfo" : 1
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4))
    else:
        print("error loco")