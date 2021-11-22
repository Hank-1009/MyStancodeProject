"""
File: largest_digit.py
Name: Hank周柏翰
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: The value we want to detect.
	:return: The number which represent the largest digit.
	"""
	if n < 0:
		n = -n  # 先把數字轉正
	if n % 10 == n:  # Base Case, if n has only one digit, return itself.
		return n
	else:  # Recursive
		return max(n % 10, find_largest_digit(n // 10))








if __name__ == '__main__':
	main()
