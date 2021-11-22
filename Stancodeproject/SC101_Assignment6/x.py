
"""
r1 = input("1 row of letters: ")
    # Now, we need to check the legal conditions for every input string.
    if len(r1) != 7 or r1[1] != ' ' or r1[3] != ' ' or r1[5] != ' ' or not r1[0].isalpha() or not r1[2].isalpha() \
            or not r1[4].isalpha() or not r1[6].isalpha():
        print('Illegal input')
    else:
        r2 = input("2 row of letters: ")
        if len(r2) != 7 or r2[1] != ' ' or r2[3] != ' ' or r2[5] != ' ' or not r2[0].isalpha() or not r2[2].isalpha() \
                or not r2[4].isalpha() or not r2[6].isalpha():
            print('Illegal input')
        else:
            r3 = input("3 row of letters: ")
            if len(r3) != 7 or r1[1] != ' ' or r3[3] != ' ' or r3[5] != ' ' or not r3[0].isalpha() or not \
                    r3[2].isalpha() or not r3[4].isalpha() or not r3[6].isalpha():
                print('Illegal input')
            else:
                r4 = input("4 row of letters: ")
                if len(r4) != 7 or r4[1] != ' ' or r4[3] != ' ' or r4[5] != ' ' or not r4[0].isalpha() or not \
                        r4[2].isalpha() or not r4[4].isalpha() or not r4[6].isalpha():
                    print('Illegal input')
                else:
                    # Now, we have r1, r2, r3, r4 four strings with 16 letters(each one has 4 letters).
                    start = time.time()
                    print(r1)
                    print(r2)
                    print(r3)
                    print(r4)
                    boggle(r1, r2, r3, r4)
"""