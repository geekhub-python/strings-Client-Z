#!/usr/bin/env python3

text = input("Enter string: ")
res_list = []
res_list.append(text[0])

for i in range(len(text)):
	if(i%3 == 0):
		continue
	else:
		res_list.append(text[i])

text = "".join(res_list)

print(text)
