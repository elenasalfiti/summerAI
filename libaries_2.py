import math as mt 
import random as rm

result_1 = mt.pow(2,4)
print("result_1 is", result_1)

result_2 = mt.sqrt(16)
print("result_2 is", result_2)

result_3 = rm.randint(0,100)
print("result_2 is", result_3)

names = ["Elena", "Reina", "Jess", "Wakka", "Inacio"]
print("Original names: ", names)
rm.shuffle(names)
print("names after shuffling: ", names)

result_4 = rm.choice(names)
print("Chosen name is: ", result_4)