import math
import pandas as pd

def haversine_distance(lat1, lon1, lat2, lon2):
    radius = 6371  # Earth's radius in kilometers

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a)) 
    result = c * radius
    result = round(result, 2)  # Round the final distance to 2 decimal places

    return result