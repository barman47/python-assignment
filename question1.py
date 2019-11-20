# a program that allows a user to enter any ten number into an array, find sum of its elements

count = 1
array = []
total = 0
while count < 11:
    userInput = input('Provide a number and press enter: ')
    array.append(userInput)
    total += int(userInput)
    count += 1

print(f'Sum of items = {total}')
