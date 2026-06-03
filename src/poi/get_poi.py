import overpy
import time
api = overpy.Overpass(url="https://overpass.kumi.systems/api/interpreter")

#Overpass API query to fetch points of interest (POIs) such as schools and grocery stores in Calgary
#In Overpass there are 3 different types of elements: nodes, ways, and relations.
#Nodes are an individual points with a unique latitude and longitude
#Ways are a collection of nodes that form a polyline or polygon, such as a building or a park
#Relations are a collection of nodes and ways that form a logical group, such as a bus route or a neighborhood

def fetch_schools():
    query = """ 
    (
      node["amenity"~"school|college|university"](51.02,-114.1,51.05,-114.0);
       
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
    
    return schools

def fetch_grocery_stores():
    # Placeholder for fetching grocery store data
    # call API from a service like OpenStreetMap or a local database to get nearby grocery stores based on geocoded coordinates
    query = """
    (
      node["shop"="supermarket"](51.02,-114.1,51.05,-114.0);
     
    );
    out center; 
    """
    result = api.query(query) # ask to give results based on the query
    grocery_stores = []
    for node in result.nodes:
        grocery_stores.append((node.lat, node.lon)) # add the latitude and longitude of each grocery store to the list
    return grocery_stores