"""
File: boggle.py
Name: Hank周柏翰
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
# Global variables
d_l = []  # A list that stores all the words in dictionary
used_word = []


def main():
    """
    TODO: To make a boggle game!
    """
    read_dictionary()
    ####################
    #                  #
    #       TODO:      #
    #                  #
    ####################
    # Now, we need to check the legal conditions for every input string.
    a = []  # I use 'a' to store all the strings.
    for i in range(4):
        r = input(str(i + 1) + " row of letters: ")
        if len(r) != 7 or r[1] != ' ' or r[3] != ' ' or r[5] != ' ' or not r[0].isalpha() or not r[2].isalpha() \
                or not r[4].isalpha() or not r[6].isalpha():
            print('Illegal input')
            break
        else:
            a.append(r)
    if len(a) == 4:
        start = time.time()
        boggle(a[0], a[1], a[2], a[3])
        print('There are '+str(len(used_word))+' words in total')
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    with open(FILE, "r") as f:
        for line in f:
            line = line.strip()  # To eliminate the /n
            d_l.append(line)


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for ele in d_l:
        if ele.startswith(sub_s):
            return True
    return False


def boggle(r1, r2, r3, r4):
    """
    :param r1: (str) string with 4 english letters and space
    :param r2: (str) string with 4 english letters and space
    :param r3: (str) string with 4 english letters and space
    :param r4: (str) string with 4 english letters and space
    :return: number of words for boggle.
    """
    r1 = r1.lower()
    r2 = r2.lower()
    r3 = r3.lower()
    r4 = r4.lower()
    r1 = r1.split(' ')
    r2 = r2.split(' ')
    r3 = r3.split(' ')
    r4 = r4.split(' ')
    # Now, r1, r2, r3, r4 are four lists.
    board = [r1, r2, r3, r4]
    m = len(board)
    n = len(board[0])
    word = []
    used_index = []  # list of tuple with index used
    for i in range(m):
        for j in range(n):
            boggle_helper(board, word, i, j, used_index)


def boggle_helper(board, word, i, j, used_index):
    if len(word) >= 4 and ''.join(word) in d_l:  # The question asks for word that has more than 4 letters
        if ''.join(word) not in used_word:
            used_word.append(''.join(word))
            print("Found: \"" + ''.join(word) + "\"")
        elif ''.join(word) in used_word:  # special case to deal word that has letters bigger than 5
            for x, y in [(-1, -1), (-1, -1), (-1, -0), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                cur_x, cur_y = i + x, j + y
                if 0 <= cur_x < len(board) and 0 <= cur_y < len(board[0]) and (cur_x, cur_y) not in used_index:
                    # Choose
                    word.append(board[i][j])
                    used_index.append((i, j))
                    letter = ''
                    for k in word:
                        letter += k
                    if has_prefix(letter):
                        # Explore
                        boggle_helper(board, word, cur_x, cur_y, used_index)
                    # Un-choose
                    used_index.pop()
                    word.pop()
    else:
        # 多一次(-1, -1)是為了怕第一次就跑到base case，而不把(-1, -1)當成一個方向。
        for x, y in [(-1, -1), (-1, -1), (-1, 0), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            cur_x, cur_y = i + x, j + y
            if 0 <= cur_x < len(board) and 0 <= cur_y < len(board[0]) and (cur_x, cur_y) not in used_index:
                # Choose
                word.append(board[i][j])
                used_index.append((i, j))
                letter = ''
                for k in word:
                    letter += k
                if has_prefix(letter):
                    # Explore
                    boggle_helper(board, word, cur_x, cur_y, used_index)
                # Un-choose
                used_index.pop()
                word.pop()


if __name__ == '__main__':
    main()
