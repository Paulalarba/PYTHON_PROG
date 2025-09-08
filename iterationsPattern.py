"""# counting in a loop
zork = 0
print("BEFORE", zork)
for thing in [3, 23, 32, 4, 2, 4, 20]:
    zork = zork + 1
    print(zork, thing)
print("AFTER", zork)"""
"""
# summing in a loop
sum = 0
print("BEFORE", sum)
for num in [12, 31, 23, 32, 53, 53]:
    sum = sum + num
    print(f"{num} {sum}")
print(sum)
"""
#finding the average in a loop
"""count = 0
sum = 0
print(f"before: {count} {sum}")
for value in [9, 21, 23, 54, 75, 64, 35]:
    count = count + 1
    sum = sum + value
    avarage = sum / count
    print(f"{count} {value} {sum}")
print(f"{avarage:.2f}")"""

#filtering in a loop
"""num = 20
for largest in [21, 12, 45, 64, 66, 75]:
    if largest > num:
        print(f"largest number: {largest}")
print(largest)"""

# found loop it if you want to found a number prints 3
"""found = False
for value in [12, 32, 52, 1, 2, 3, 45]:
    if value == 32:
        found = True
    print(f"Found: {found}")"""

# how to find the largest  value
"""largest_num = -1
for num in [1, 5, 33, 52, 100, 102, 101]:
    if num > largest_num:
        largest_num = num
    print(f"{largest_num} {num}")
print(f"{largest_num}")"""

# how to find the smallest value:
Smallest = None
for num in [2, 12, 11, 14, 13, 1]:
    if Smallest is None:
        Smallest = num
    elif num < Smallest:
        Smallest = num
    print(f"{Smallest} {num}")
print(Smallest)