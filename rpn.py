#!/usr/bin/env python3

import operator
import readline
import sys
from termcolor import colored

operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow
}

def calculate(myarg):
	stack = list()
	notFirst = False
	for token in myarg.split():
		try:
			token = int(token)
			stack.append(token)
			# Lines to decrease coverage
			#if(token == 100):
			#	print "OMG!"
		except ValueError:
			func = operators[token]
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = func(arg1, arg2)
			stack.append(result)
		if(len(stack) == 1 and notFirst):
			print colored(stack, 'green')
		else:	
			print colored(stack, 'red')
		notFirst = True
	if len(stack) != 1:
		raise TypeError("Too many parameters")
	return stack.pop()

def main():
	while True:
		result = calculate(input("rpn calc> "))
		print colored((result), 'green')

if __name__ == '__main__':
	main()
