#Простейшие арифметические операции (1)
#Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть произведена над ними. Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".
def arithmetic(number1, number2, operation):
	if(operation=="+"):
		print(int(number1)+int(number2))
	elif(operation=="-"):
		print(int(number1)-int(number2))
	elif(operation=="*"):
		print(int(number1)*int(number2))
	elif(operation=="/"):
		print(int(number1)/int(number2))
	else:
		print("No support.")


number_input=input("First number: ")
number2_input=input("Second number: ")
oper=input("Operation,please: ")
arithmetic(number_input, number2_input, oper)