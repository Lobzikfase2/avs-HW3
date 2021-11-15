from random import randint


def gen_str():
    string = ""
    string += chr(randint(ord('A'), ord('Z')))
    for i in range(randint(3, 20)):
        string += chr(randint(ord('a'), ord('z')))
    return string
