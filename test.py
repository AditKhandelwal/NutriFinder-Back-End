from ResturantLocator import find_restaurants
from grabItems import filter_items
from createFinalFormatResults import merge_json_files
import json

# Access the data fields sent from the client
category = "Hamburger"
goal = 'medium'
price_type = 'medium'
distance = 100

latitude = 37.367273  # Example latitude
longitude = -120.423080  # Example longitude
radius = 20000  # Example radius in meters

# Get location items and filter items
location_items = find_restaurants(radius, latitude, longitude, category)
filter_item = filter_items(goal, price_type, category)

with open('location.json', 'w') as json_output_file: 
     json.dump(location_items, json_output_file, indent=4)

with open('filteredItems.json', 'w') as json_output_file: 
     json.dump(filter_item, json_output_file, indent=4)

merged_data = merge_json_files("location.json", "filtereditems.json", "wow.json")

with open('foodAlternativeResults.json', 'w') as json_output_file:
    json.dump(merged_data, json_output_file, indent=4)

print("Merged data has been written to 'foodAlternativeResults.json'")