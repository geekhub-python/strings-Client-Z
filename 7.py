#!/usr/bin/env python3

text = input("Enter string: ")
#	находим первое и последнее вхождение 'h'
i_first = text.find("h")
i_last = text.rfind("h")
# получаем список из групп символов, которые между 'h'
my_list = text.split("h")
# обрабатываем список таким образом, чтобы оставить первое и последнее вхождение 'h' нетронутым
my_list[0] = my_list[0] + 'h' + my_list[1]
del my_list[1]
my_list[-2] = my_list[-2] + 'h' + my_list[-1]
del my_list[-1]
# делаем из списка строку, попутно ставя 'H' на места где ранее были 'h' 
text = 'H'.join(my_list)
print(	text	)
