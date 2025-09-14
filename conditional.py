# def full_name(age, name):
#     age = int(input("enter your age: "))
#     name = input("Enter your name: ")
#     print(f"Your age is {age} and your name is: {name}")
# full_name(" ", " ")

# def check_birtday(month, day, year):
#     birthday = input()
# def check_under_age(age):
#     age = int(input("Enter your age: "))
#     if age < 18:
#         print("You can't buy an alcohol your under age")
#     else:
#         print("what alcohol you want?")

# check_under_age(" ")

# implement the get_min(a, b,) function in the code editor
# it should retrurn the minimum of a and b 
# if they are equal it doesnt matter which value you return
def get_min(a, b):
    a = int(input("Enter number for a: "))
    b = int(input("Enter number for b: "))

    if a < b:
        print(f"A is the minimum: {a}")
        return a
    elif a == b:
        print("they are equal: {a} {b}")
        return a
    elif a > b:
        print(f"B is the minimum{b}")
        return b
get_min("", "")

# implement the function called check_range(num)
def check_range(num):
    num = int(input("Enter a number: "))
    if num < 0:
        return print("Negative")
    elif num == 0:
        return("zero")
    elif num > 0 and num < 10:
        return print("positive single digit")
    elif num >= 10:
        return print("positive multi digit")
check_range("")

# implement the discount_app(age) function, it accepts an intege age and should return true if the age is less than 18
# or the age is greater than or equal to 65 otherwise it should return false

def discount_app(age):
    age = int(input("Enter your age: "))
    if age < 18 or age >= 65:
        return "True"
    else:
        return "False"
discount_app(age="")

# truthy and Falsy : to make it simple every thing that is 0 emphy or empty list and boolean false is always falsy because it has nothing 
# while the truthy is opposite it has to have a value
x = 10
if x:
    print("This shit is True") # this will print cuz it is true
y = 0
if y:
    print("This shit is falsy") # this will not print because it is false