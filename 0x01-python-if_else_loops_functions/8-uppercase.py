#!/usr/bin/python3
def uppercase(str):
    total = ''
    for chara in str:
        if ord(chara) >= 97 and ord(chara) <= 122:
            total += chr(ord(chara) - 32)
        else:
            total += chara
    print("{:s}".format(total))
