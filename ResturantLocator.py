import googlemaps
import os
import json
from dotenv import load_dotenv
from math import radians, sin, cos, sqrt, atan2

# Load environment variables from .env file
load_dotenv()

def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371 * c  # Radius of the Earth in kilometers
    return distance * 0.621371

def find_restaurants(radius, lat, lng, keywords):
    api_key = 'AIzaSyCz3Pgl8mwi6_UWe8L7ehGypJ9gylMLPNw'
    gmaps = googlemaps.Client(key='AIzaSyCz3Pgl8mwi6_UWe8L7ehGypJ9gylMLPNw')
    all_restaurants_info = []

    radius = float(radius)

    for keyword in keywords:
        places_result = gmaps.places_nearby(location=(lat, lng), radius=(radius*1609.344) - 1500, keyword=keyword, type='restaurant')
        
        if 'results' in places_result:
            for place in places_result['results']:
                # Check if this place is already in the list to avoid duplicates
                if place['place_id'] not in [r.get('place_id') for r in all_restaurants_info]:
                    restaurant_name = place['name']
                    restaurant_lat = place['geometry']['location']['lat']
                    restaurant_lng = place['geometry']['location']['lng']
                    distance = haversine(lat, lng, restaurant_lat, restaurant_lng)
                    place_id = place['place_id']

                    # Check if photos are available for the place
                    photo_urls = []
                    if 'photos' in place:
                        for photo in place['photos']:
                            photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo['photo_reference']}&key={api_key}"
                            photo_urls.append(photo_url)

                    address = place.get('vicinity', 'Address not available')

                    all_restaurants_info.append({
                        'place_id': place_id,  # Add place_id to help identify duplicates
                        'name': restaurant_name,
                        'distance': distance,
                        'photo_urls': photo_urls,
                        'address': address
                    })

    return all_restaurants_info

