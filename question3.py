#A Python program to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

number = int(input("Input a number "))
dictionary = dict()

for x in range(1,number + 1):
    dictionary[x]=x*x

print(dictionary) 