import json
import os

BASE_DIR = os.path.dirname(__file__)
cache_file = os.path.join(BASE_DIR, "geocode_cache.json")
os.makedirs(BASE_DIR, exist_ok=True) # ensure the cache directory exists

def load_cache():
    if os.path.exists(cache_file):
        with open(cache_file, "r") as f: # opens the cache file in read mode
            return json.load(f) # loads the cache data from the file and returns it as a dictionary
    return {}
def save_cache(cache):
    with open(cache_file, "w") as f: # opens the cache file in write mode
        json.dump(cache, f,indent=4) # saves the cache data to the file in JSON format

def save_geocodes(geocodes):
    with open(cache_file, "w") as f: # opens the cache file in write mode
        json.dump(geocodes, f, indent=4) # saves the geocodes data to the file in JSON format with indentation for readability

