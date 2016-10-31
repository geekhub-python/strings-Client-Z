#!/usr/bin/env python3

 #	сохраняем срезы до первой "h" и после последней "h", затем удаляем их из списка 
    #	получаем строку из списка, которая состоит из символов, находящихся между 1м и последним 
    #   вхождением 'h' и делаем реверс
    #	склеиваем части изначальной строки, помещая внутрь реверснутый текст
    
text = input("Enter string: ")
my_list = text.split("h")
   
first = my_list[0] + 'h'
last = 'h' + my_list[-1]
my_list.pop(0)
my_list.pop()

reverse_text = "h".join(my_list)
reverse_text = reverse_text[::-1]

text = first + reverse_text + last

print(text)
