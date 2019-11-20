# function which return reverse of a string 
name = input('Enter a word to check whether it is a palindrome: ')

def reverse(string): 
    return string[::-1] 
  
def isPalindrome(string): 
    # Calling reverse function 
    rev = reverse(string) 
  
    # Checking if both string are equal or not 
    if (string == rev): 
        return True
    return False

result = isPalindrome(name)

if result == True:
    print(f'{name} is a palindrome')

if result == False:
    print(f'{name} is not a palindrome')