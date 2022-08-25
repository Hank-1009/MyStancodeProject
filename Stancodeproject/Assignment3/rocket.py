"""
File: rocket.py
Name: Hank周柏翰
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3
# end is the length of the rocket.
end = 2*SIZE+2


def main():
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	"""
	The number of row(i) equals to 'SIZE'.
	The number of column(j) equals to 'end'.
	I calculate i and j with math to achieve the goal.
	"""
	for i in range(SIZE):
		for j in range(end):
			if j <= SIZE <= (i + j) < (2 * SIZE):
				print('/', end='')
			elif j > SIZE and 2 <= (j-i) < (SIZE+2):
				print('\\', end='')
			else:
				print(' ', end='')
		print('')


def belt():
	"""
	The number of row(i) equals to 'end'.
	In the start and the end point, we print '+', otherwise we print'='.
	"""
	for i in range(end):
		if i == 0 or i == (end-1):
			print('+', end='')
		else:
			print('=', end='')
	print('')


def upper():
	"""
	First, I separate the function with two parts, SIZE is odd and SIZE is even.
	Print | in the start and the end of every row. (must be the first step in the loop)
	Print '.' under the math conditions( left side and right side) ( must be the second step in the loop)
	When size is odd, '\' will be  printed on points where (i+j) is odd and '/' will be printed on points where (i+j) is
	even
	When size is even, '\' will be  printed on points where (i+j) is even and '/' will be printed on points where (i+j) is
	odd
	I use elif to ensure that every instructions only be executed within each i and j
	"""
	a = SIZE
	if a % 2 == 1:  # size is odd
		for i in range(SIZE):
			for j in range(end):
				if j == 0 or j == (end-1):
					print('|', end='')
				elif (i + j) < SIZE:    # left side points
					print('.', end='')
				elif (j-i) > (SIZE+1):  # right side points
					print('.', end='')
				elif (i+j) % 2 == 1:
					print('/', end='')
				else:
					print('\\', end='')
			print('')
	if a % 2 == 0:  # size is even
		for i in range(SIZE):
			for j in range(end):
				if j == 0 or j == (end-1):
					print('|', end='')
				elif (i + j) < SIZE:
					print('.', end='')
				elif (j-i) > (SIZE+1):
					print('.', end='')
				elif (i+j) % 2 == 0:
					print('/', end='')
				else:
					print('\\', end='')
			print('')


def lower():
	"""
		Print | in the start and the end of every row.(must be the first step)
		Print '.' under the math conditions( left side and right side)(must be the second step)
		 '\' will be  printed on points where (i+j) is odd and '/' will be printed on points where (i+j) is
		even
	"""
	for i in range(SIZE):
		for j in range(end):
			if j == 0 or j == (end - 1):
				print('|', end='')
			elif (j-i) <= 0:  # left side points
				print('.', end='')
			elif (i+j) >= (2*SIZE+1):  # right side points
				print('.', end='')
			elif (i+j) % 2 == 1:
				print('\\', end='')
			else:
				print('/', end='')
		print('')











###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()