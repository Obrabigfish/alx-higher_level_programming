#!/usr/bin/python3
if __name__ == "__main__":
    for content in dir(hidden_4):
        if content[:2] != "__":
            print("{:s}".format(content))
