#!/usr/bin/python3

# Do not change the following line
test_dictionary = {1:'a', 2:'b', 3:'c', 4:'d'} 

# Enter your function (and nothing else) below this line

def show_value(key,dict={}):
    key = str(key)
    is_key_in = [str(dict[k]) for k in dict.keys() if key==str(k)]
    if len(is_key_in) > 0:
        return ''.join(is_key_in)
    else:
        return key+" is not a valid key."
