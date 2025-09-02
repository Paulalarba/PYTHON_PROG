"""reverse words
    false class return is finally
    None if for lambda continue
    true def from while nonlocal
    and del global not with 
    as elif try of yield
    assert else import pass
    break except in raise
"""
# constants : fixed values such as numbers letters and strings
# comparison operators :
# multi-way
"""x = 1
if x < 2:
    print('small')
elif x < 10:
    print('medium')
else:
    print('large')
print('all done')"""
# try except if the try works the except is skipped: if the try fails it jumps to the except
"""astr = 'paul'
try:
    num = int(astr)
except:
    num = 20
print('Paul', num)
age = 20
try:
    name = int(age)
except:
    name = 'paul'
print('paul', name)"""
name = 'paul'
try:
    surname = int(name)
except:
    surname = 'Alarba'
print('hi', surname)


astr = 'bob'
try:
    print('hello')
    istr = int(astr)
    print('there')
except:
    istr = -1
print('Done', istr)

# real world example
age = input('Enter your age')
try:
    p_age = int(age)
except:
    p_age = -1
if p_age > 1:
    print('nice work')
else:
    print('wrong answer')