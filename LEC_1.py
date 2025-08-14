string = "hello world!"
print(len(string))

string1 = "Paul Alarba"
string2 = "how Are you?"

concat1 = string1 + string2
print(concat1)

Concat = string1 + " " + string2
print(Concat)

string3 = "The quick brown fox jumped over the lazy dog. #1234567890!"
print(string3[16:19])


word1 = "Animals"
word2 = "Badger"
word3 = "Honey bee"
word4 = "HoneyBadger"

word1 = word1.lower()
word2 = word2.lower()
word3 = word3.lower()
word4 = word4.lower()

print(word1)
print(word2)
print(word3)
print(word4)

word1 = word1.upper()
word2 = word2.upper()
word3 = word3.upper()
word4 = word4.upper()

print(word1)
print(word2)
print(word3)
print(word4)

string4 = " Filet Mignon"
#string4 = string4.lstrip() #remove whitespace from left
print(string4.lstrip())
string5 = "Brisket "
print(string5.rstrip())

string6 = "Becomes"
string7 = "becomes"
print(string7.startswith('be'))

string6 = string6.lower()
print(string6.startswith('be'))
print(string7.startswith('be'))


#user input
prompt = "Hi what's your facebook account?"
user_input = input(prompt)
print("You said:", user_input)

prompt1 = "What's Your full Name?"
user_input1 = input(prompt1)
user_input1 = user_input1.lower()
print(user_input1)

prompt2 = "Where do yu live?"
user_input2 = input(prompt2)
#user_input2 = user_input2.len()
print(len(user_input2))
