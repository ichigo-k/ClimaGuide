import os
from dotenv import load_dotenv
import requests as req
import sys

load_dotenv(".env.local")

GEOCODING_API_KEY= os.getenv("GEOCODING_API_KEY")


def get_latlng(location):
    if len(location) <= 0:
        print("Please enter a valid location")
        return sys.exit()

    try:
        latlng = req.get(f"https://api.opencagedata.com/geocode/v1/json?q={location}&key={GEOCODING_API_KEY}").json()

        if not latlng.get("results"):
            print("Location not found")
            return sys.exit()
        else:
            return latlng['results'][0]['geometry']
    except:
        print("Something went wrong, please try again!")
        sys.exit()