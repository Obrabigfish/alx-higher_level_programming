#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    total = len(argv) - 1
    if total < 1:
        print("{} arguments.".format(total))
    elif total == 1:
        print("{} argument:".format(total))
    else:
        print("{} arguments:".format(total))
    for i in range(total):
            print("{}: {}".format(i + 1, argv[i +1])) 
