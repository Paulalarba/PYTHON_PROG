# this is it fucking listtt
# list is mutable meaning you can change the value of list
# exercise 
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1]
"""def check_list_empty(my_list):
   if my_list:
    print("The list is not empty")
   else:
    print("the list is empty")
check_list_empty(my_list)

 #name_list = ["janna", "Paul", "Angelo"]
def check_name():
    name_list = input("Enter all the name: ").split()
    name_list = [name.lower() for name in name_list]
    if "janna" in name_list:
        print("the love of my list is in the list")
    else:
        print("wala meow meow meow")
check_name()

def count_x():
    num = int(input("Enter the number you want to count: "))
    count = 0
    for nums in my_list:
        if nums == num:
            count = count + 1
    print(f"result: {count}: the number you want to count: {num}")
    if count == 0:
        print(f"the number {num} is not in the list")
count_x()

# built in function that can be use in list
print(max(my_list))
print(min(my_list))
print(sum(my_list))"""

# append() it adds one new item to the end of a list
# you can append any datatype, take not you cant add to arguments example: (1, 2) this is no valid
# but you can append a list my_list.append([1, 2]) this is valid
# challenge ask the user what to append

# my_list.append("append last")
# print(my_list)
def challenge_append():
    add = input("Enter what to append: ") # this will always accept as string no matter what you input
    my_list.append(add)
    print(my_list)
challenge_append()
# .pop() is gonna pop the index in the list you want, by default it gonna pop the last index in string but you can modify it
# note always remember that the index[] is start at zero
# my_list.pop(0)
# print(my_list)
# #challenge ask the user to input the index that gonna pop
# def challenge_pop():
#     delete = int(input("Enter the index you want to delete: "))
#     my_list.pop(delete)
#     print(my_list)
# print(my_list)
# challenge_pop()