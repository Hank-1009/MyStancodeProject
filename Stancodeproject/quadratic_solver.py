"""
File: quadratic_solver.py
Name: Hank 周柏翰
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	First, I assign a,b and c corresponding to the coefficient of the quadratic, then I assign d as the discriminant.
	Second, I need to determine whether d is greater than 0, equal to 0 or smaller than 0 and print what the question
	required.
	"""
	print('StanCode Quadratic Solver!')
	a = float(input('Enter a: '))
	b = float(input('Enter b: '))
	c = float(input('Enter c: '))
	d = (b*b)-(4*a*c)
	if d > 0:
		root1 = (-b + math.sqrt(d)) / (a * 2)
		root2 = (-b - math.sqrt(d)) / (a * 2)
		print('Two roots: ' + str(root1) + ' , '+str(root2))
	elif d == 0:
		root = (-b)/(a*2)
		print('One root: '+str(root))
	else:
		print('No real roots')


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == "__main__":
	main()
