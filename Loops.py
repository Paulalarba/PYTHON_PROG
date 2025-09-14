# using for loop, print the numbers 10 through 20 in order including 10 and 20
# the range() in for loop: the first parameter is where it start and the second is where it will end
# and remember the last digit will not be prented, the third parameter is called skip it is the number what you want to incremment
for num in range(10, 101, 10): #since the second parameter is greater than 100 the 100 will be printed
    print(num)

# reverse loop

for n in range(20, 9, -1):
    print(n)

# nested loop: challenge what we want is to pair all the possible number from 1-5

for i in range(1, 6):
    for j in range(1, 6):
        print(i, j)