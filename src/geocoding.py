from geopy.geocoders import Nominatim
import pandas as pd
import time

#creating a geolocator object to use the Nominatim geocoding service
geolocator = Nominatim(user_agent="calgary_houses_geocoder")
def geocode_address(address):
    try:
        location = geolocator.geocode(address, country_codes="CA") # geocode the address to get the latitude and longitude
        if location: # if sucessfully geocoded, return the latitude and longitude
            return location.latitude, location.longitude
        else:
            return None, None
    except Exception as e:
        print(f"Error geocoding address {address}: {e}")
        return None, None
    
def add_geocodes(df):
    latitudes = []
    longitudes = []
    
    for address in df["address"]:
        lat, lon = geocode_address(address)
        latitudes.append(lat)
        longitudes.append(lon)
        time.sleep(1) # to avoid hitting the rate limit of the geocoding service
    
    df["latitude"] = latitudes
    df["longitude"] = longitudes
    return df