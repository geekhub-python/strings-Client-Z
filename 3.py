#!/usr/bin/env python3

import math

text = input("Enter string: ")
n = math.ceil(len(text) / 2)
part_1 = text[:n]
part_2 = text[n:]
new_string = part_2 + part_1
print(new_string)
