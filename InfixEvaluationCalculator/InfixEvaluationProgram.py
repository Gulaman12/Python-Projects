#By Angelo Terminez (ater906) #InfixEvaluation
class EvaluateInfix:
	def __init__(self,string):
		self.__string = string
		self.__stack = []
		self.__calculation = []
		self.__operands =[]

	def check_precedence(self,character):
		if character == "(":
			return 0
		elif character == "^":
			return 1
		elif character == "*" or character == "/":
			return 2
		elif character == "+" or character == "-":
			return 3
		else:
			return 4
	
	def convert_to_postfix(self):
		x = EvaluateInfix(self.__stack)
		postfix = ""
		number_string = "0123456789"
		for each in self.__string:
			if each in number_string:
				postfix += each
			elif each == " ":
				postfix += each
			elif each == ".":
				postfix += each
			else:
				if each in "^*/+-<>()":
					if len(self.__stack) == 0:
						self.__stack += each
					elif each == "(":
						self.__stack += each
					elif each == ")":
						top = self.__stack.pop()
						while top != "(" and len(self.__stack) != 0:
							if top != ")":
								postfix += " "
								postfix += top
							top = self.__stack.pop()
					else:
						other_operator = x.check_precedence(each)
						precedence = x.check_precedence(self.__stack[len(self.__stack)-1])
						if precedence <= other_operator and precedence != 0:
							operator = self.__stack.pop()

							postfix += operator

							self.__stack += [each]
						else:
							self.__stack += [each]
		for each in self.__stack:
			postfix += " "
			postfix += each
		return postfix

	def get_operands(self):
		num = ""
		number_string = "0123456789"
		for operands in self.__string:
			if operands in number_string and operands != " ":
				num += operands
			else:
				num += " "
		self.__operands += [int(o) for o in num.split()]
		return self.__operands

	def postfix_calculator(self,expression_string):
		expression = expression_string.split()
		number_string = "0123456789"
		for each in expression:
			if each[0] in number_string:
				if "." not in each:
					self.__calculation +=[int(each)]
				else:
					self.__calculation +=[float(each)]
			else:
				y = self.__calculation.pop()
				x = self.__calculation.pop()
				operator = EvaluateInfix(self.__stack).check_precedence(each)
				if operator == 1 and each == "^":
					z = x ** y
				elif operator == 2 and each == "*":
					z = x * y
				elif operator == 2 and each== "/":
					z = x / y
				elif operator == 3 and each == "+":
					z = x + y
				elif operator == 3 and each == "-":
					z = x - y
				elif operator == 4 and each == "<":
					if x < y:
						z = x
					else:
						z = y
				else:
					if x > y:
						z = x
					else:
						z = y
				self.__calculation += [z]
		for each in self.__calculation:
			return each

	def get_result(self):
		expression_string = EvaluateInfix(self.__string).convert_to_postfix()
		calculate = EvaluateInfix(self.__string).postfix_calculator(expression_string)
		return calculate

def q2(expression):
	result = EvaluateInfix(expression)
	return result.get_result()
#Input Questions:
print(q2('2 + 4545')) #4547
print(q2('2 ^ ( 1 + 3 ^ 2 )')) #1024
print(q2('( 3 * 5 ) - ( 1 > 2 > 3 < 4 )')) #12
print(q2('1 + 100 > 200')) #200
print(q2('1 + ( 100 > 200 )')) #201
print(q2('40 > 15 < 35 + 10')) #50
print(q2('( 40 > 15 < 35 ) + 10')) #45
print(q2('2 * ( ( 4 < 2 + 3 ) + 3 * 4 )')) #32
