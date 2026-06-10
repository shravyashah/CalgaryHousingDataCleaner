# Calgary Housing Data Cleaner and Ranker

## Overview

Calgary Housing Data Cleaner and Ranker is a data engineering project that deals with pipelines and transforming raw house listings in Calgary into a ranked dataset based on affordability, listing quality, and where it is located.

This project integrates skills and concepts in:
- Using pandas for data cleaning and preprocessing
- Integrating API's for geocoding (Nominatim) and finding POI's (Overpass)
- Feature engineering
- Geospatial analysis using the Haversine formula
- Designing a ranking system
- Caching to improve API latency 

## Problem Motivation 

The motivation behind this project came from my Dad who is a landlord. Often times, listings can be tedious to find and often come with missing and inconsistent data. To make the search easier and more automated, a ELT pipeline approach was used.

Pipeline: Read raw file -> Cleaning -> Geocoding -> POI extraction -> Feature Engineering -> Ranking -> Save processed file

## Key Features

1. Data Cleaning Pipeline
   - Standardized raw house listings
   - Cleaned addresses, prices, garage, and days on the market columns
   - Removed duplicate addresses by using a a normalized formatting
   - Engineered price/sqft

2. Ranking System: Score is out of 100
   - The number of bedrooms and bathrooms
   - Price/Sqft
   - Days on the Market
   - Whether property has a garage
   - How near it is to a school and grocery store
  
3. Geospatial analysis
   - Geocoded addresses using Nominatim API
   - Used the Overpass API to extract POI's (schools and grocery stores)
   - Used the Haversine formula to compute the nearest school and grocery store for each address
   - Implemented a caching system to improve API latency
  
## Power BI Dashboard

Here is a dashboard showcasing statistics on the processed house listings.
![Dashboard](outputs/House_Dashboard)
  
## Tech Stacks Used

- Python
- Pandas
- Json
- Nominatim
- Overpass

## Set up and How to run
Here are the steps to access the project on PowerShell or whatever operating system you use:
1. Go into the directory where your project is located
2. Activate venv by typing in venv\Scripts\activate in the terminal 
3. Install pandas by running the following command: pip install pandas
4. Then install geopy by running the following command: pip install pandas geopy
5. After install the overpy wrapper to access OverPass api using this command: pip install overpy
6. Then to run the project go to the directory that the project is in and then run: python -m src.main

## Future Improvements
- Could integrate real in time listings
- Can make it an interactive web app
- Use Machine Learning to predict and compare prices of other listings in the area
