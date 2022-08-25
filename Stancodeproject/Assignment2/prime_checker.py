"""
File: prime_checker.py
Name: Hank 周柏翰
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
# This constant controls when to stop
EXIT = -100


def main():
	"""
	Welcome to the prime checker!
	Lets check whether a positive integer is a prime number or not.
	"""
	print('Welcome to the prime checker')
	check_prime_number()


def check_prime_number():
	"""
	First, I assign 2 to k, then I use a infinite while loop to determine whether n is a prime number or not.
	There are two steps:
	1. if n can't be divided by every positive integer that are smaller than itself(except 1), then it is an prime number.
	So we use k+=1 to ensure all the numbers are checked.
	*DO not forget 2 is the special case of prime number, so when n initially equals 2, print n is a prime number.
	2. if n can be divided by any numbers smaller than itself, then it is not a prime number(Here I use the if condition,
	so we do not need to check all the numbers smaller than n if the condition is already fulfilled.
	"""
	n = int(input('n: '))
	if n == EXIT:
		print('No numbers were entered')
	else:
		while True:
			k = 2
			while n > k:
				if (n % k) == 0:
					print(str(n) + ' is not a prime number')
					break
				else:
					k += 1
			if n == k:
				print(str(n) + ' is a prime number')
			n = int(input('n: '))
			if n == EXIT:
				print('Have a good one!')
				break







###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
