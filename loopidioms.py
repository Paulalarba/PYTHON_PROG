largest_num = -1
print(largest_num)
for number in [21, 21, 23, 45, 54, 32, 45, 100]:
    if number > largest_num:
        largest_num = number
    print(f"Largest so far {largest_num}")

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)