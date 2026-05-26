# Calgary Housing Data Cleaner and Ranker

## Overview

This project was a way for me to get introduced into data cleaning and preprocessing pipeline. Additionally, I thought that there might be families desiring to move to Calgary urgently due to unforseen circumstances or just wanting to move to Calgary in an easier way instead of frantically searching and deciding what house is best for them. This prompted me to attempt to build a housing search and ranking system to give an idea of listing based on completeness, location, and affordability. 

## Version 1

Version 1 is now completed and includes:
- Loading raw data from Calgary's housing sites and putting into a csv file
- Cleaned up addresses, prices, and lot prices
- Standarized address format to detect duplicates in address
- Computed price/sqft which will be used in ranking system

## What is to come
The project will move onto version 2 which will hopefully implement a ranking system based on completeness and affordability. Version 3 will implement the location aspect of the project and then the ranking system will be updated accordingly.

An interesting feature that can be added is adding live-time data, so anyone can access it at anytime without having to search up listings. Just a thought for now... 

## Set up and How to run
Here are the steps to access the project on PowerShell or whatever operating system you use:
1. Go into the directory where your project is located
2. Activate venv by typing in venv\Scripts\activate in the terminal incase you need to install something
3. Install pandas by running the following command: pip install pandas
4. Then to run the project go to the directory that the project is in and then run: python src\main.py
