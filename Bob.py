def find_bob_occurrences(text):
    count = 0


    for i in range(len(text)):
        if text[i] == 'b' and i + 2 < len(text):
            if text[i + 1:i + 4] == 'Bob':
                count += 1

    return count


text = "Bob bobob went to the bobstore with Bobs"
print("Number of occurrences:", find_bob_occurrences(text))


#my explanation:


#the function_bob_occurrences is defined so that it will look the information of our interest in the text
#the "count" variable is written so that it can identify/count the number of times the desired pattern/repetition
#is in the text
# we use "for" to iterate (in other words, to repeat the process of searching and identifying)
#for each character
# inside of the loop, we check if the conditions of the question are met
# (if the character identified is 'b' and if there are at
# least three more characters in the text (because Bob has three letters, so 3 characters are needed).)
# if this does occur (the conditions mentioned are satisfied), we check the next
# two characters, to see if, all together, they spell out 'Bob'
#if they do form 'Bob', the 'count' variable is updated (it increases by one)
# then, at the end, the 'return' function is called so that it will
# tell us the final, complete number of times that the pattern is found in the text
