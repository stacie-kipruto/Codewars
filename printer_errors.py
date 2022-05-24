def printer_error(s):
    colour_string = "abcdefghijklm"
    
    errors = 0
    length_of_str = len(s) #totalno.of strings
    
    for letter in s:
        if letter not in colour_string:
            errors = errors + 1
    return str(errors) + "/" + str(length_of_str)
