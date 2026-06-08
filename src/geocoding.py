from geopy.geocoders import Nominatim
from scripts.geocode_cache import load_cache, save_cache
import json
import time

#creating a geolocator object to interact with the Nominatim geocoding service
geolocator = Nominatim(user_agent="calgary_houses_geocoder")

cache = load_cache() # cache to store previously geocoded addresses and their corresponding latitude and longitude

def is_valid_geocode(lat, lon): 
    if lat is None or lon is None:
        return False
    return 50.8 <= lat <= 51.2 and -114.4 <= lon <= -113.8
# This function checks to see if the coordinates are valid and are in Calgary

def geocode_address(address):
    try:
        # 1. Check if the address is already in the cache
        if address in cache: # check if the address has already been geocoded and stored in the cache
            return cache[address] # return the cached latitude and longitude if available
        # 2. If not in cache, geocode the address and api call
        location = geolocator.geocode(address, country_codes="CA") # geocode the address to get the latitude and longitude
        if location: # if sucessfully geocoded, return the latitude and longitude
            lat,lon = location.latitude, location.longitude
            #3. Validate the geocoded coordinates to ensure they are within the expected range for Calgary
            if is_valid_geocode(lat, lon): # check if the geocoded coordinates are within the expected range for Calgary
                cache[address] = (lat, lon) # store the geocoded coordinates in the cache for future use
                return lat, lon
        cache[address] = (None, None) # if geocoding fails or returns invalid coordinates, store None in the cache to avoid repeated attempts
        return None, None
    except Exception as e:
        print(f"Error geocoding address '{address}': {e}")
        cache[address] = (None, None) # store None in the cache in case of an error to avoid repeated attempts
        return None, None
# This function essentially determines whether we need to call the api or not and what to save in the cache. The first step is to check if the address has already
# been geocoded. If it has then simply return the address and coordinates and no api call is needed. If that is not true we call the api to find the coordinates
# for the address and save it if it is valid, if not we store none in the cache.
     
def add_geocodes(df):
    latitudes = []
    longitudes = []   
    for address in df["address"]:
        if address in cache: # check if the address has already been geocoded and stored in the cache
            lat, lon = cache[address] # retrieve the cached latitude and longitude if available   
        else:
            lat, lon = geocode_address(address)
            time.sleep(1) # to avoid hitting the rate limit of the geocoding service
    
        latitudes.append(lat)
        longitudes.append(lon)
    df["latitude"] = latitudes
    df["longitude"] = longitudes
    df["geo_valid"] = df["latitude"].notna() & df["longitude"].notna() # add a column to indicate whether the geocoding was successful
    
    save_cache(cache) # save the updated cache to the file
    return df
# This function first creates empty lists of lat and lon, then it loops thru every address and checks to see
# if the address has been geocoded we add to the lists respectively, if not we, we need to call the api but with a 1 sec buffer.
# Then three new columns are added, lat, lon and if the geocoding was successful

def load_geocodes():
    with open("scripts/geocode_cache.json", "r") as f:
        return json.load(f)
# This reads the json file where the coord are saved and it returns it
