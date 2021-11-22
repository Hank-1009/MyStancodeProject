"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop
# Global variables
d_l = []  # A list that stores all the words in dictionary


def main():
    """
    TODO: We are going to make an anagram generator.
    """
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    read_dictionary()
    ####################
    #                  #
    #       TODO:      #
    #                  #
    ####################
    while True:
        s = input('Find anagrams for: ')
        start = time.time()
        if s == EXIT:
            break
        else:
            use = find_anagrams(s)
            print(f'{len(use)} anagrams: {use}')
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    with open("dictionary.txt", "r") as f:
        for line in f:
            line = line.strip()  # To eliminate the /n
            d_l.append(line)


def find_anagrams(s):
    """
    :param s: The word we want to detect.
    :return: All the possible outcomes of anagram.
    """
    use = []  # 用來儲存最後的結果
    d = []  # 看儲存過的current_lst，避免重複發生
    if s not in d_l:
        print('No such word in dictionary')
    elif s in d_l:
        print('Searching...')
        find_anagrams_helper(s, [], len(s), [], use, d)
    return use


def find_anagrams_helper(s, current_lst, ans_len, used_index, used_word, d):
    """
    :param s: The word we want to detect.
    :param current_lst: The current list that stores the split words.
    :param ans_len: The length of the word that we want to detect.
    :param used_index: The index of the letter that has been used.
    :param used_word: The word that has already detected.
    :param d: A list I use to store the subset of the word.(ex. book --> b,bo,boo,book,bko.....)
    :return: All the possible outcomes of anagram.
    """
    if len(current_lst) == ans_len:
        ans = ""
        for i in current_lst:
            ans += i
        if ans in d_l:
            print("Found: "+ans)
            used_word.append(ans)
            print("Searching...")
    else:
        for j in range(len(s)):
            if j not in used_index:
                ele = s[j]
                used_index.append(j)
                # Choose
                current_lst.append(ele)
                letter = ""
                for i in current_lst:  # This for loop loop over current_lst and put it in a string called 'letter'.
                    letter += i
                if has_prefix(letter):  # To save time with has_prefix function(see whether the start is in dictionary)
                    if letter not in d:  # To see if there occurs repetitive letter in d.
                        d.append(letter)
                        # Explore
                        find_anagrams_helper(s, current_lst, ans_len, used_index, used_word, d)
                # Un-choose
                used_index.pop()  # we also need to pop out the index!
                current_lst.pop()


def has_prefix(sub_s):
    """
    :param sub_s: The start of the word.
    :return: True/False
    """
    for ele in d_l:
        if ele.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
