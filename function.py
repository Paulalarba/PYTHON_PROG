def greet(name, greeting):
    message = name + " " + greeting
    print(message)
greet("Paul", "hello")

def two_sum(num1, num2):
    result = num1 + num2
    print(result)

two_sum(7, 10)

def three_sum(num1, num2, num3):
    result = num1 + num2 + num3
    print(result)
three_sum(2, 23, 4)

# return in function: it has to primary purpose
# the first one is when a function encounter a return the code immedately exit meaning the other code after the return will not be executed
# the second onw is sending a value back to its caller
def num_two(num1, num2):
    return(num1 + num2)

print(num_two(21, 21))

def product(num1, num2):
    return num1 * num2
prod = product(21, 9)
print(prod)

#local and global scope: the local scope can access the global but the global can't access the local
age = 10
def name_age(age):
    age = 100
    print(age + 2)

name_age(age)

# default argument

def name_greet(name = "Paul", greeting = "hello"): #this function is valid
    print(name + " " + greeting)
name_greet()

def name_greet1(name, greeting = "hi"): # this is valid
    print(name + " " + greeting)

name_greet1("Paul")

# def name_greet2(name = "Paul", greetings): #this is not valid
#     print(name + " " + greeting)
