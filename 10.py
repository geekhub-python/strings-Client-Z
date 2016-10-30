#!/usr/bin/env python3

text = input("Enter string: ")
my_list = text.split("h")
n_list = []
n_list.append(my_list[0])
n_list.append(my_list[-1])
text = "".join(n_list)
print(text)
