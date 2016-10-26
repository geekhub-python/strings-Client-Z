#!/usr/bin/env python3

text = input("Enter string: ")
n = text.find(" ")
part_1 = text[:n]
part_2 = text[n:]
new_string = part_2 + " " + part_1
print(new_string)
