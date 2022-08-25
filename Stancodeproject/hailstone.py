"""
File: hailstone.py
Name: Hank 周柏翰
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    hailstone sequences are incredible math!
    """
    print('This program computes Hailstone sequences.')
    print('')
    hailstone_incredible()


def hailstone_incredible():
    n = int(input('Enter a number: '))
    """
    k is the number of steps to reach 1
    """
    k = 0
    if n == 1:
        k = 0
    while n != 1:
        while (n % 2) == 1 and n != 1:
            print(str(n) + ' is odd, so I make 3n+1: ' + str(3 * n + 1))
            n = int((3 * n + 1))
            k += 1
            """             
            now n is even
            """
        while (n % 2) == 0:
            print(str(n) + ' is even, so I take half: ' + str(int(n / 2)))
            n = int((n / 2))
            k += 1
    """
    jump out the loop when n equals to 1
    """
    print('It took ' + str(k) + ' steps to reach 1.')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
