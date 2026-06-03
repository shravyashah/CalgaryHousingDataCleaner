# Calgary Housing Data Cleaner and Ranker

## Overview

This project was a way for me to get introduced into data cleaning and piplining. Additionally, I thought that there might be families desiring to move to Calgary urgently due to unforseen circumstances or just wanting to move to Calgary in an easier way instead of frantically searching and deciding what house is best for them. This prompted me to attempt to build a housing search and ranking system to give an idea of how good house listings are based on completeness, location, and affordability. 

## Version 1

Version 1 is now completed and includes:
- Loading raw data from Calgary's housing sites and putting into a csv file
- Cleaned up addresses, prices, and lot prices
- Standarized address format to detect duplicates in address
- Computed price/sqft which will be used in ranking system

## Version 2
Version 2 is completed and includes
- Ranking system out of 100 that ranks based on price/sqft, # of bedrooms, # of bathrooms,
  number of days on the market, and if it has a garage
- Cleaned up garage and number of days on market columns

## What is to come
The project is currently in version 3 which will hopefully implement an improved ranking system. The first thing that was done in v3 was geocoding to convert the addresses
into coordinates using Nominatim so that other features can be implemented. Once that was completed, I used the Overpass Api to find poi such as schools and grocery stores. I had to limit it
to a certain area of Calgary, as trying to find schools and stores for the whole of Calgary is not plausible due to api latency issues.

An interesting feature that can be added is adding live-time data, so anyone can access it at anytime without having to search up listings. Just a thought for now... 

## Set up and How to run
Here are the steps to access the project on PowerShell or whatever operating system you use:
1. Go into the directory where your project is located
2. Activate venv by typing in venv\Scripts\activate in the terminal 
3. Install pandas by running the following command: pip install pandas
4. Then install geopy by running the following command: pip install pandas geopy
5. After install the overpy wrapper to access OverPass api using this command: pip install overpy
6. Then to run the project go to the directory that the project is in and then run: python -m src.main 
