import json

def merge_json_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        test_data = json.load(f1)
        food_alternative_results = json.load(f2)
    
    merged_results = []

    for item in food_alternative_results:
        for test_item in test_data:
            if item["Restaurant"] == test_item["name"]:
                merged_item = {

                    "place_id": test_item["place_id"],
                    "name": item["Restaurant"],
                    "menuItem": item["Item"],
                    "Calories": item["Calories"],
                    "Protein": item["Protein"],
                    "price": item["Price"],
                    "distance": test_item["distance"],
                    "photo_urls": test_item["photo_urls"],
                    "address": test_item["address"]
                }
                merged_results.append(merged_item)
    return merged_results 
   