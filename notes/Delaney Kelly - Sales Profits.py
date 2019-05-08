import csv

item_types = ["Fruits", "Clothes", "Meat", "Beverages", "Office Supplies", "Cosmetics", "Snacks",
              "Personal Care", "Household", "Vegetables", "Baby Food", "Cereal"]

with open("Sales Records (1).csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("")
