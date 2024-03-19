import json

def filter_items(calorie_type, price_type,category):
    # Define calorie ranges
    with open('input.json') as json_file:
        data = json.load(json_file)

    if calorie_type == 'low':
        calorie_range = (0, 300)
    elif calorie_type == 'medium':
        calorie_range = (301, 500)
    elif calorie_type == 'high':
        calorie_range = (501, float('inf'))
    else:
        raise ValueError("Invalid calorie type. Please specify 'low', 'medium', or 'high'.")

    # Define price ranges
    if price_type == 'low':
        price_range = (0.0, 3.0)
    elif price_type == 'medium':
        price_range = (5.01, 10.0)
    elif price_type == 'high':
        price_range = (10.01, float('inf'))
    else:
        raise ValueError("Invalid price type. Please specify 'low', 'medium', or 'high'.")
    
    # Filter items based on calorie and price range
    filtered_items = [item for item in data if 
                      calorie_range[0] <= int(item['Calories']) <= calorie_range[1] and
                      price_range[0] <= float(item['Price'].replace('$', '')) <= price_range[1]]
    return filtered_items

# def grabPerfectItem(category): 
#     #this will read the menu for input.json and if it finds the restaurant in the "Restaurant" tag it will print the item 
#     with open('input.json', 'r') as f:
#         data = json.load(f)
#         for item in data:
#             if (item['Category'] == category):
#                 print(item['Item'])
#                 print(item['Category'])
#                 print(item['Price'])
#                 print(item['Calories'])
#                 print(item['Fat'])
#                 print(item['Carbs'])
#                 print(item['Protein'])
#                 print(item['Sodium'])
#                 print(item['Ingredients'])
#                 print("\n")
                

        
    return data

# Example usage
# grabPerfectItem("Burger")
