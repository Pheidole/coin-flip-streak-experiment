# coin flip streaks inspired by Automate the Boring Stuff with Python Chapter 4

import random


def coinFlipListGenerator():  # generates a list of 100 coin flip results and returns the reference to the list
    generatedList = []
    for i in range(100):
        if random.randint(0, 1) == 0:
            generatedList.append('H')
        else:
            generatedList.append('T')
    return generatedList


def checkForNumberOfStreaks(listToCheck, lengthOfStreak):
    numberOfStreaks = 0
    streakCheck = 1
    for i in range(1, len(listToCheck)):  # skip 0 as list checks previous index
        if listToCheck[i] == listToCheck[i-1]:
            streakCheck += 1
        else:
            streakCheck = 1
            continue
        if streakCheck == lengthOfStreak:  # if the streak is as long as the desired length of streak
            numberOfStreaks += 1  # add 1 to the number of streaks
    return numberOfStreaks


def userInput():
    sure = 0
    while True:
        try:
            lengthOfDesiredStreak = int(input('Please enter the length of desired streak: '))
            if lengthOfDesiredStreak < 1:
                print('Desired string must be greater than 0')
                continue
            break
        except ValueError:
            print('Length of desired streak must be an integer value.')
            print('Try again...')
            continue
    while True:
        try:
            numOfExperiments = int(input('Please enter the number of experiments you would like performed: '))
            if numOfExperiments > 1000000:
                while True:
                    try:
                        sure = int(input('Performing this many experiments may take a long time, are you sure?\n1. Yes\n2. No\n'))
                    except ValueError:
                        print('Input must be an integer. Try again...')
                        continue
                    if sure == 1 or sure == 2:
                        break
                    else:
                        print('Input must be a "1" or "2"')
                        continue
            elif numOfExperiments < 1:
                print('Number of experiments must be greater than 0')
                continue
            if sure == 1:
                sure = 0
                break
            elif sure == 2:
                sure = 0
                continue
            break
        except ValueError:
            print('Number of experiments must be an integer value.')
            print('Try again...')
            continue
    return lengthOfDesiredStreak, numOfExperiments


def coinFlipStreaks():  # main
    print('This program will check the probability of a streak (of a length you give) of heads or tails occuring in 100 coin flips.')
    print('It will perform this experiment as many times as you wish and print the average result over the given number of experiments.')
    while True:
        lengthOfDesiredStreak, numOfExperiments = userInput()
        numberOfStreaksTotal = 0
        streakOccurred = 0
        print('Valid inputs; calculating result...')
        for experimentNumber in range(numOfExperiments):
            coinFlipsList = coinFlipListGenerator()  # makes coinFlipsList reference point to generated list
            numberOfStreaks = checkForNumberOfStreaks(coinFlipsList, lengthOfDesiredStreak)
            numberOfStreaksTotal += numberOfStreaks
            if numberOfStreaks > 1:
                streakOccurred += 1
        print('The average number of streaks that occured in 100 coin flips was: {0}'. format(round((numberOfStreaksTotal / numOfExperiments), 2)))
        print('Chance of at least one streak of {0} occuring in 100 coin flips: {1}%'.format(lengthOfDesiredStreak, round((streakOccurred / (numOfExperiments / 100)), 2)))
        while True:
            try:
                again = int(input('Would you like to play again?\n1. Yes\n2. No\n'))
                if again == 1 or again == 2:
                    break
                else:
                    print('Input must be a "1" or "2"')
                    continue
            except ValueError:
                print('Input must be an integer. Try again.')
                continue
        if again == 1:
            continue
        else:
            break


coinFlipStreaks()
