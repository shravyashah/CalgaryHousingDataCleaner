import overpy
import os
import pandas as pd
api = overpy.Overpass(url="https://overpass.kumi.systems/api/interpreter")
#Overpass API query to fetch points of interest (POIs) such as schools and grocery stores in Calgary
#In Overpass there are 3 different types of elements: nodes, ways, and relations.
#Nodes are an individual points with a unique latitude and longitude
#Ways are a collection of nodes that form a polyline or polygon, such as a building or a park
#Relations are a collection of nodes and ways that form a logical group, such as a bus route or a neighborhood

def fetch_schools():
    query = """ 
    (
      node["amenity"~"school|college|university"](50.8,-114.4,51.2,-113.8);
      way["amenity"~"school|college|university"](50.8,-114.4,51.2,-113.8);     
    );
    out center; 
    """
    # The query first defines an area with the name "Calgary" and assigns it to a variable called .searchArea. 
    # Then, it searches for nodes, ways, and relations that have the tag "amenity" set to "school" within the defined search area. 
    # Finally, it outputs the results with the center coordinates of each element.
    result = api.query(query) # ask to give results based on the query
    schools = []
    for node in result.nodes:
        schools.append((node.lat, node.lon)) # add the latitude and longitude of each school to the list
    
    for way in result.ways:
        if way.center_lat is not None and way.center_lon is not None: # check if the way has valid center coordinates
            schools.append((way.center_lat, way.center_lon)) # add the center coordinates of each school way to the list
    return schools

def fetch_grocery_stores():
    # Placeholder for fetching grocery store data
    # call API from a service like OpenStreetMap or a local database to get nearby grocery stores based on geocoded coordinates
    query = """
    (
      node["shop"="supermarket"](50.8,-114.4,51.2,-113.8);
      way["shop"="supermarket"](50.8,-114.4,51.2,-113.8);
    );
    out center; 
    """
    result = api.query(query) # ask to give results based on the query
    grocery_stores = []
    for node in result.nodes:
        grocery_stores.append((node.lat, node.lon)) # add the latitude and longitude of each grocery store to the list
    for way in result.ways:
        if way.center_lat is not None and way.center_lon is not None: # check if the way has valid center coordinates
            grocery_stores.append((way.center_lat, way.center_lon)) # add the center coordinates of each grocery store way to the list
    return grocery_stores

#creates two files, schools.csv and grocery_stores.csv, in the data/processed directory, which contain the latitude and longitude of schools and grocery stores in Calgary, respectively.
SCHOOLS_FILE = "data/processed/schools.csv"
GROCERY_STORES_FILE = "data/processed/grocery_stores.csv"

def load_schools():
    if os.path.exists(SCHOOLS_FILE):
        df = pd.read_csv(SCHOOLS_FILE) # load the cached schools data from a CSV file
        return list(zip(df["latitude"], df["longitude"])) # return a list of tuples containing the latitude and longitude of each school
    print("Fetching schools data from API...")
    schools = fetch_schools() # fetch the latitude and longitude of schools in Calgary
    
    os.makedirs(os.path.dirname("data/processed"), exist_ok=True) # create the directory if it doesn't exist
    pd.DataFrame(schools, columns=["latitude", "longitude"]).to_csv(SCHOOLS_FILE, index=False) # save the schools data to a CSV file for future use
    
    return schools

    
def load_grocery_stores():
    if os.path.exists(GROCERY_STORES_FILE):
        df = pd.read_csv(GROCERY_STORES_FILE) # load the cached grocery stores data from a CSV file
        return list(zip(df["latitude"], df["longitude"])) # return a list of tuples containing the latitude and longitude of each grocery store
    print("Fetching grocery stores data from API...")
    grocery_stores = fetch_grocery_stores() # fetch the latitude and longitude of grocery stores in Calgary
    os.makedirs(os.path.dirname("data/processed"), exist_ok=True) # create the directory if it doesn't exist
    pd.DataFrame(grocery_stores, columns=["latitude", "longitude"]).to_csv(GROCERY_STORES_FILE, index=False) # save the grocery stores data to a CSV file for future use

    return grocery_stores