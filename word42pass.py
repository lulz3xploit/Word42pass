#!/bin/python3

import sys
import random
import json

def spec_change(word, reverse=0):
    if not reverse:
        if word in spec_chars:
            word = spec_chars.get(word)
    else:
        try:
            word = int(word)
            if word in spec_chars.values():
                word = [str(key) for key, value in spec_chars.items() if value == word][0]
        except:
            pass

    return(word)


help_msg = """
Usage: python3 word42pass.py <number of characters> [spec_chars] [rand]

number of chars: define len of password.
 spec_chars: Is an json formats for change char with a special chars specfied:
    Ex: '{"a":"@","e":3,...}' (optional)
 rand: Randomize upper case. (optional)

 Example usage:
    python3 word42pass.py 8
    python3 word42pass.py 12 rand
    python3 word42pass.py 16 '{"a":"@","e":3,"i":1}'
    python3 word42pass.py 12 '{"a":4, "t":7, "e":3}' rand
"""

spec_chars = ""
rand = False

if len(sys.argv) < 2 or len(sys.argv) > 4:
    print(help_msg)
    sys.exit(1)

elif len(sys.argv) == 4:
    if sys.argv[2] == "rand":
        print(help_msg)
        sys.exit(1)

    spec_chars = json.loads(sys.argv[2])
    rand = True

elif len(sys.argv) == 3:
    if sys.argv[2] == "rand":
        rand = True
    else:
        spec_chars = json.loads(sys.argv[2])

vowels = list("aeiou")
consonants = list("bcdfghjklmnpqrstvwxyz")

strings = ""

while len(strings) <= int(sys.argv[1]):
    if len(strings) == 0:
        i = random.choice([1,2])
        if i == 1:
            strings = random.choice(vowels)
        elif i == 2:
            strings = random.choice(consonants)
    if spec_change(strings[-1], reverse=1) in vowels:
        strings += str(spec_change(random.choice(consonants)))
    else:
        strings += str(spec_change(random.choice(vowels)))

if rand:
    x = 0
    tuple_bool = (True, None)
    strings_list = list(strings)
    for c in strings_list:
        r = random.choice(tuple_bool)
        if r:
            strings_list[x] = c.upper()
        x += 1
    strings = "".join(strings_list)

print(strings)
