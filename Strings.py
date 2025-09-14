#lenght function
# implement a function called get_longer_word(word1, word2) it takes two words strins as parameters
# and it returns the longer word, if the words are the same lenght return the same length

def get_longer_word(word1, word2):
    word1 = len(input("Enter your first word: "))
    word2 = len(input("Enter your second word: "))

    if word1 > word2:
        return print(f"the first word is the longest {word1}")
    elif word2 > word1:
        return print(f"the second word is the longest {word2}")
    else:
        return print("Same lenght")
get_longer_word("", "")
     
#shorthand method without using range()
def shorthand():
    word = input("Enter your word: ")
    for char in word:
        print(char)
shorthand()

#slicing strings:
def first_n_charcters():
    s = input("Enter the name you want: ")
    n = int(input("Enter the len of the string: "))
    print(s[n:])
first_n_charcters()

# this is how you reverse the string
# note if you want to reverse the string the stop should be greater than the start
def string_reverse():
    string = input("Enter the string: ")
    n = int(input("Enter the start: "))
    j = int(input("Enter the stop: "))
    print(string[n:j:-1])
string_reverse()