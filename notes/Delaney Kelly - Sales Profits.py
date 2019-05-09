import csv

different_items = {}

with open("Sales Records (1).csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    print("Processing...")

    for row in reader:
        if row[0] == "Region":
            continue
        old_number = float(row[13])
        item_type = row[2]
        try:
            different_items[item_type] += old_number
        except KeyError:
            different_items[item_type] = old_number

    for value in different_items:
       

    print(different_items)
    best_product = max(different_items)
    print(best_product)
