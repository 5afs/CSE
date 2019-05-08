import csv

item_types = []
item_profits = []

with open("Sales Records (1).csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    print("Processing...")

    for row in reader:  # getting item types in a list
        item_class = row[2]
        if item_class not in item_types:
            item_types.append(item_class)

    item_types.remove(item_types[0])

    for item in item_types:
        item_profits.append(0)
        # for row in reader:

    print(item_types)
    print(item_profits)

'''
make a list of ints for the profit sums
for every row that has that item type, add the profit to the index for that item type
find which item has the biggest profits
print that item type out and its profit saying its the best one

# item_profits[item_types.index(item)] = row[13]

for row in reader:
        for item in item_types:  # adding up the sums
            item_profits.append(row[13])
'''
