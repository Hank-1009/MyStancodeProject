"""
File: weather_master.py
Name: Hank 周柏翰
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
# This constant controls when to stop
EXIT = -100
# EXIT= -1


def main():
    """
    Weather_master() tells us the highest,lowest and average temperature of all the days. Furthermore, it tells us how
    many days we can issue the low temperature alarm.
    """
    print('StanCode \"Weather Master 4.0\"!')
    weather_master()


def weather_master():
    """
    There are three steps:
    1. we assign 't1' as the initial temperature, so if there is only t1 alone, the highest, lowest and the average
    temperature will all be t1.( I use 'lowest' and 'highest' to represent the lowest and highest temperature.)
    2. I use 'k' to count the times we enter temperature, use 'summation' to calculate the summation  of all
    temperatures entered and use 'cold' to calculate the number of temperatures below 16 degrees.
    3. After all temperatures are entered, we can print the highest and lowest temperature by the if statement
    and count the mean of all temperatures by (summation/k).
    """
    t1 = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
    if t1 == EXIT:
        print('No temperatures were entered')
    else:
        highest = t1
        lowest = t1
        summation = t1
        k = 1
        if t1 < 16:
            cold = 1
        else:
            cold = 0
        while True:
            t = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
            if t == EXIT:
                break
            if t > highest:
                highest = t
            if t < lowest:
                lowest = t
            if t < 16:
                cold += 1
            summation = summation+t
            k += 1
        print('Highest temperature = ' + str(highest))
        print('Lowest temperature = ' + str(lowest))
        print('Average = '+str((summation/k)))
        print(str(cold)+' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
