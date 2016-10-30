#!/usr/bin/env python3

text = input("Enter string: ")
#	находим первое вхождение 'f'
i_first = text.find("f")
#	делаем срез строки после первого вхождения и находим следующий символ "f"
second_text = text[i_first+1:]
i_second = second_text.find("f")

if (i_first == -1):
	print(-2)
elif(i_first != -1 and i_second == -1):
	print(-1)
else:
	print(i_second + i_first + 1)
