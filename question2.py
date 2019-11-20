# a Python program to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
dictionary = dict()
for x in range(1,16):
    dictionary[x] = x**2
print(dictionary)  