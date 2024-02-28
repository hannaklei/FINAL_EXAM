# Explanation:
#
# Lists are mutable because particular elements within them
# can be changed/modified. However, the content of strings
# cannot be changed, per se. if we try to change specific elements/characters
# in a string, there will be an error. this shows us that strings
# are immutable.
# what we can do if we want to modify a string is create a new one by
# including only the parts/elements from the previous string that we wish to keep,
#perhaps adding something in between or appending to the end, depending on what
#we want the new string to look like.

#HERE IS AN EXAMPLE:

# Lists are mutable
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# Modifying the list
my_list[0] = 10
print("Modified list:", my_list)

# Strings are immutable
my_string = "hello"
print("Original string:", my_string)

# Attempting to modify the string (will result in an error)
# my_string[0] = 'H'  # This line will raise a TypeError

# Instead, we create a new string with the modified content
new_string = 'H' + my_string[1:]
print("Modified string:", new_string)


