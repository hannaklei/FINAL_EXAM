def is_url(input_str):
    if input_str.startswith("http://") or input_str.startswith("https://") or input_str.startswith("ftp://"):
        return True
    elif "." in input_str:
        return True
    else:
        return False

url_input = input("Enter a string to check if it's a URL: ")
if is_url(url_input):
    print("The input is a URL.")
else:
    print("The input is not a URL.")


    #EXPLANATION BELOW

    # Check if the input starts with a protocol prefix (such as http://, the way
    #URLs usually start
    # Then, check if the input contains a period (.), since this tells us that there's
    #a domain name

    #then we test the function by asking for a user input
    #if the input meets the conditions, the program will print that it is, indeed, a URL