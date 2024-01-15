#!/usr/bin/python3
def no_c(my_string):
    if my_string[:]:
        new = my_string.translate({ord("c"): None})
        second = new.translate({ord("C"): None})
        return second
    return my_string
