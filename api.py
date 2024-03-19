from flask import Flask, request, jsonify
from flask_cors import CORS
from MenuSort import filter_items as menu_filter_items
from ResturantLocator import find_restaurants as locate_restaurants
from grabItems import filter_items as item_filter_items
from createFinalFormatResults import merge_json_files
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/test', methods=['POST'])
def test_endpoint():
    data = request.json
    category = data.get('category')
    goal = data.get('goal')
    price = data.get('price')
    distance = data.get('distance')

    # Example latitude and longitude
    latitude = 37.367273
    longitude = -120.423080

    location_items = locate_restaurants(distance, latitude, longitude, category)
    filter_item = item_filter_items(goal, price, category)

    with open('location.json', 'w') as json_output_file:
        json.dump(location_items, json_output_file, indent=4)

    with open('filteredItems.json', 'w') as json_output_file:
        json.dump(filter_item, json_output_file, indent=4)

    merged_data = merge_json_files("location.json", "filteredItems.json")
    
    return jsonify(merged_data)

if __name__ == '__main__':
    app.run(debug=True)
