import csv
# Drop the last digit from the number. The last digit is what we want to check against
# Reverse the numbers
# Multiply the digits in odd positions (1, 3, 5, etc.) by 2 and subtract 9 to all any result higher than 9
# Add all the numbers together
# The check digit (the last number of the card) is the amount that you
#   would need to add to get a multiple of 10 (Modulo 10)


def reverse(num: list):
    print(num[::-1])


def multiply_odd_spaces_and_subtracting_nines(num: list):
    for index in range(len(num)):
        if index % 2 == 0:
            num[index] *= 2
            if int(index) > 9:
                index -= 9


def add_all(my_list: list):
    total = 0
    for digit in my_list:
        total += digit
    return total


def check():
    if (int(digits) + last_digit) % 10 == 0:
        return True
    return False


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            old_number = row[0]
            digits = list(old_number)

            if len(digits) == 16:
                last_digit = digits[15]
                digits.remove(last_digit)
                reverse(digits)
                multiply_odd_spaces_and_subtracting_nines(digits)
                add_all(digits)
                check()
        print("OK")
