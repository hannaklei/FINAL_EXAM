
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
number = 2974101607733149676776769413377061014792
number_str = str(number)

if palindrome(number_str):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")