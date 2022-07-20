import re

#task 1
def hours_to_mins(x):
    result = x*60
    return result

mins = hours_to_mins(2)
print(mins)

#task 2
n=6

if n>60:
    hours = n/60
    print(hours)
else:
    mins = n*60 
    print(mins)


#task 3
def count_letters(word):
    return len([x for x in word if x.isalpha()])

print(count_letters("Word."))

