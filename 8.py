#!/usr/bin/env python3

text = input("Enter string: ")
#	находим первое и последнее вхождение 'f'
i_first = text.find("f")
i_last = text.rfind("f")
if (i_last == i_first and i_last != -1):
	print(i_first)
elif(i_first != i_last):
	print(i_first, i_last)
elif(i_last != -1 and i_first != -1):
	pass
