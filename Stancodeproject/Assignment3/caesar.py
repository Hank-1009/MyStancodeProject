"""
File: caesar.py
Name: Hank周柏翰
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    n: The secret number
    s: Cipher string
    decipher: The outcome we want to see
    """
    n = int(input('Secret number: '))
    s = input('What\'s the cipher string? ')
    s = s.upper()
    decipher = cipher(n, s)
    print('The deciphered string is: '+decipher)


def cipher(n, s):
    """
    :param n: secret number
    :param s: cipher string
    cut: The part we cut off from ALPHABET
    remain: The remaining part of ALPHABET
    new_a: New ALPHABET
    """
    cut = ALPHABET[(len(ALPHABET)-n):]
    remain = ALPHABET[0:(len(ALPHABET)-n)]
    new_a = cut+remain  # New ALPHABET
    i = ""
    """
    If character in s is a English letter, we will change it to the corresponding letter in new_a in 'i'.
    If not, ch we will remain the same in 'i'. 
    """
    for ch in s:
        if ch.isalpha():
            i = i + ALPHABET[new_a.find(ch)]
        else:
            i = i + ch
    return i




#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
