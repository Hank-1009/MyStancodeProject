"""
File: similarity.py
Name: Hank周柏翰
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    1. Input s1 as the sequence to search
    2. Input s2 as the sequence to match
    3. Doing homology and find the best match: s3
    """
    s1 = input('Please give me a DNA sequence to search: ')  # Input s1 as the sequence to search
    s1 = s1.upper()
    s2 = input('What DNA sequence would you like to match? ')  # Input s2 as the sequence to match
    s2 = s2.upper()
    s3 = homology(s1, s2)  # Doing homology and find the best match: s3
    print('The best match is '+s3)


def homology(s1, s2):
    """
    s1: DNA sequence to search
    s2: DNA sequence that we want to match
    """
    similarity = 0  # I use score system to represent the similarity of two sequences.
    new_similarity = ""  # represent the score of each match
    """
    There are (len(s1)-len(s2)+1) pairs to calculate the similarity score.
    If the base of s1 equals to base of s2, score of similarity will plus one, otherwise will pass
    (each time one base to compare) 
    """
    for i in range((len(s1)-len(s2)+1)):
        for j in range(len(s2)):
            s1_base = s1[i+j]  # The base of sequence1
            s2_base = s2[j]  # The base of sequence2
            if s1_base == s2_base:
                similarity += 1
            else:
                similarity += 0
        new_similarity += str(similarity)
        similarity = 0  # Don't forget to reset the value of similarity
    position = new_similarity.find(max(new_similarity)) # find the position that represents the maximum score of the sequence
    best_match = s1[position:(position+len(s2))]
    return best_match




###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
