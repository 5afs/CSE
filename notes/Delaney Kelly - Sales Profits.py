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

    best_key = ""
    best_value = max(different_items.values())

    for key, value in different_items.items():
        if value == best_value:
            best_key = key

print()
print("The best product is %s at $%s." % (best_key, best_value))
