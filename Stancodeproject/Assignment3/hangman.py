"""
File: hangman.py
Name: Hank周柏翰
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Let's play a hangman game!
    """
    hang_man()


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def hang_man():
    ans = random_word()  # 'ans' is the real answer
    guess = ""  # 'guess' is the unknown term(--------), we start with an empty string and create it with the for loop.
    for i in range(len(ans)):
        guess += "-"
    print('The word looks like: ' + str(guess))
    print('You have ' + str(N_TURNS) + ' guesses left.')
    word = input('Your guess: ')  # Our guess
    word = word.upper()
    n = N_TURNS  # n are the times that we can still guess.
    # Check whether 'word' in line 57 is illegal or not. After the check, word will be in right format.
    word = illegal_format(word)
    """
    Now we need to check whether we have a wrong guess or not.(First term)
    'word' is our guess after the  wrong check.(in the right format)
    'n1' is the number that we can still guess after the wrong check.
    """
    word, n1 = wrong_guess(word, n, guess, ans)
    while word in ans:  # We will go in this loop when we start guessing right.
        print('You are correct!')
        for j in range(len(ans)):  # To check whether there are same words in 'ans' or not, so I use the index system
            ch = ans[j]  # Using for loop, it will check all the words in ''ans
            if ch != word:
                pass
            else:
                guess = guess[0:j] + ans[j] + guess[(j + 1):]
        if guess == ans:  # when guess==ans, we jump out the loop.
            print('You win!!')
            print('The word was ' + ans)
            break
        print('The word looks like: ' + guess)
        print('You have ' + str(n1) + ' guesses left.')
        word = input('Your guess: ')
        word = word.upper()
        word = illegal_format(word)  # Every guess still needs to check the legality.
        """
        This time, we need to put n1 into the function because 'n1' is the number that we can still guess after the 
        first term wrong check.
        Also, every guess may be wrong, so there will have new 'word' and 'n1' 
        """
        word, n1 = wrong_guess(word, n1, guess, ans)


def illegal_format(word):
    """
    :para word: Our guess
    It is a function that warns the user when they input illegal format.
    illegal format: 'word' is not alpha and 'word' have more than one English letter.
    """
    while not word.isalpha() or len(word) != 1:
        print('illegal format')
        word = input('Your guess: ')
        word = word.upper()
    return word


def wrong_guess(word, n, guess, ans):
    """
    :para word: Our guess, str
    :para n: int, n==N_TURNS at the beginning, but it will decrease if we guess wrong.
    :para ans: The answer, str
    :para guess: the unknown term(----------) after 'The words looks like: ', str
    This is a function that describe the situation when user continuously guesses wrong, but it will break when user
    guesses right.
    """
    while word not in ans:
        if n <= 1:
            print('There is no ' + word + '\'s in the word')
            print('You are completely hung : (')
            print('The word was: ' + ans)
            break
        else:
            print('There is no ' + word + '\'s in the word')
            print('The word looks like: ' + guess)
            print('You have ' + str(n - 1) + ' guesses left.')
            n -= 1
            word = input('Your guess: ')
            word = word.upper()
            illegal_format(word)
    return word, n


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
