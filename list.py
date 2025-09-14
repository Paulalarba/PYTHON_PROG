# this is it fucking listtt
# list is mutable meaning you can change the value of list
# exercise 
my_list = [1, 2, 3, 4]
def check_list_empty(my_list):
    if my_list:
        print("The list is not empty")
    else:
        print("the list is empty")
check_list_empty(my_list)

#name_list = ["janna", "Paul", "Angelo"]
def check_name():
    name_list = input("Enter all the list: ").split()
    if "janna" in name_list:
        print("the love of my list is in the list")
    else:
        print("wala meow meow meow")
check_name()