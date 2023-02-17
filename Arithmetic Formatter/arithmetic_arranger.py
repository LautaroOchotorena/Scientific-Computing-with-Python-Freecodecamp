import operator
def arithmetic_arranger(list1,Opt_Bool=False):
	numbers = list()
	ops = { "+": operator.add, "-": operator.sub }
	if len(list1)>5:
		return('Error: Too many problems.')
		exit()
	else:
		for operation in list1:
			y = operation.split()	#It creates a list separating the string
			try:
				y[0] = int(y[0]) #Those are strings at first, so now int
				y[2] = int(y[2])
			except:
				return('Error: Numbers must only contain digits.')	#Return error if they aren't int 
				exit()
			if (-10000 < y[0] < 10000) and (-10000 < y[2] < 10000):	#Numbers have less than four digits
				if (y[1] == '+') or (y[1] == '-'):
					z = ops[y[1]](y[0],y[2])
					numbers.append(y[0])
					numbers.append(y[1])
					numbers.append(y[2])
					numbers.append(z)
				else:
					return('''Error: Operator must be '+' or '-'.''')
					exit()
			else:
				return('Error: Numbers cannot be more than four digits.')
				exit()
    #each text represents a line in the output
		text_1 = ''
		text_2 = ''
		text_3 = ''
		text_4 = ''

		#Output:
		for t in range(len(list1)):	#For each operation
			if len(str(numbers[4*t]))>len(str(numbers[4*t+2])):
				text_1 = text_1 + '  ' + str(numbers[4*t])
				text_2 = text_2 + numbers[4*t+1] + ' '*(len(str(numbers[4*t]))-len(str(numbers[4*t+2]))+1) + str(numbers[4*t+2])
				text_3 = text_3 + '-'*(len(str(numbers[4*t]))+2)
				if (Opt_Bool == True):
					text_4 = text_4 + ' '*(len(str(numbers[4*t]))+2-len(str(numbers[4*t+3]))) + str(numbers[4*t+3])
			else:
				text_1 = text_1 + ' '*(len(str(numbers[4*t+2]))-len(str(numbers[4*t]))+2) + str(numbers[4*t])
				text_2 = text_2 + numbers[4*t+1] + ' ' + str(numbers[4*t+2])
				text_3 = text_3 + '-'*(len(str(numbers[4*t+2]))+2)
				if (Opt_Bool == True):
					text_4 = text_4 + ' '*(len(str(numbers[4*t+2]))+2-len(str(numbers[4*t+3]))) + str(numbers[4*t+3])
			if (t<len(list1)-1):
				text_1 = text_1 + ' '*4
				text_2 = text_2 + ' '*4
				text_3 = text_3 + ' '*4
				text_4 = text_4 + ' '*4
		text_1 = text_1 + '\n'
		text_2 = text_2 + '\n'
		#If Opt_Bool==True print the answer to the operation
		if (Opt_Bool == True):
			text_3 = text_3 + '\n'
			return(text_1 + text_2 + text_3 + text_4)
		else: 
			return(text_1 + text_2 + text_3)