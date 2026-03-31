# AI-powered waste classifier (no external libraries)

# Expanded dataset: dictionary of items and categories
waste_categories = {
    # Wet waste
    "banana peel": "wet",
    "apple core": "wet",
    "vegetable scraps": "wet",
    "tea leaves": "wet",
    "food leftovers": "wet",
    "orange peel": "wet",
    "cooked rice": "wet",

    # Dry waste
    "paper": "dry",
    "cardboard": "dry",
    "old books": "dry",
    "cloth": "dry",
    "wood pieces": "dry",
    "dust": "dry",
    "broken toys": "dry",

    # Recyclable waste
    "plastic bottle": "recyclable",
    "plastic wrapper": "recyclable",
    "glass bottle": "recyclable",
    "tin can": "recyclable",
    "newspaper": "recyclable",
    "aluminium foil": "recyclable",
    "magazine": "recyclable",

    # Hazardous waste
    "battery": "hazardous",
    "medicine strip": "hazardous",
    "paint can": "hazardous",
    "broken tube light": "hazardous",
    "e-waste": "hazardous",
    "chemical container": "hazardous",
    "expired medicine": "hazardous"
}

# Take user input
item = input("Enter a waste item name: ").strip().lower()

# Prediction with partial matching
found = False
for key in waste_categories:
    if item in key:  # allows partial matches like "banana"
        print("Predicted Category:", waste_categories[key])
        found = True
        break

if not found:
    print("Item not found in dataset. Please try one of these:", list(waste_categories.keys()))
