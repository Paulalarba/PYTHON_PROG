"""String = 'Paul Alarba'
name = String[0]
print(name)

first_name = "Paul"
n = 0
fname = first_name[n - 2]
print(fname)

while n < len(String):
    lenString = String[n]
    print(f"{n} {lenString}")
    n = n + 1

for x in String:
    print(x)

caunt = 0
for last_name in String:
    if last_name == 'a':
        caunt = caunt + 1
print(caunt)"""

"""for n in "banana":
    print(n)"""

# slicing string "up to but not including"

"""name = "Paul Alarba"
print(name[0:4])
print(name[:6])
print(name[6:])
print(name[:])

#string concatanation happen when in + is used in two or more string
first_name = "Paul"
last_name = "Alarba"
full_name = first_name + " " + "Janna" #this is concatanation
print(f"{full_name}")"""

#using in as logical operator
"""name = 'Paul'
'a' in name
#the output is only true or false just like in boolean
if 'a' in name:
    print("Found it")"""

#searching in string

full_name = '  Paul Alarba  '
Find = full_name.find('b')
print(Find)
# find is method call that find the letter ask and it seach trough to string list it start in 0 and if it doesn't find it it returns -1

#search and replace the replace() is like a search and replace operation in word procces it replaces all occurrences of the search string with the placement string
nstr = full_name.replace('Paul',  'Janna')
print(nstr)
change = full_name.replace('a', 'b')
print(change)

#stripping whitespace istrip() abd rstrip() remove whitespace at the left and right, the strip removes both beggining and ending whitespaces
Lstrip = full_name.lstrip()
print(Lstrip)
Rstrip = full_name.rstrip()
print(Rstrip)
both = full_name.strip()
print(both)

# Parsing and extractiong 
my_gmail = 'paulnicoralarba@gail.com'

gmail = my_gmail.find('@')
Replace = my_gmail.replace('@','$')
print(Replace)

remove_gmal = my_gmail[gmail:]
print(remove_gmal)