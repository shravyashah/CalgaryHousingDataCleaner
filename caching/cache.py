import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__))) # adds the parent directory to the system path to allow importing from the caching module

cache_file = "caching/geocode_cache.json"

def load_cache():
    if os.path.exists(cache_file):
        with open(cache_file, "r") as f: # opens the cache file in read mode
            return json.load(f) # loads the cache data from the file and returns it as a dictionary
    return {}
def save_cache(cache):
    with open(cache_file, "w") as f: # opens the cache file in write mode
        json.dump(cache, f,indent=4) # saves the cache data to the file in JSON format