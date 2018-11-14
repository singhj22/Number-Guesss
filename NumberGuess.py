import random
'''

@author: Jugat Singh
Number Guess

'''
num= random.randrange(1,21)

guess = int(input("Please enter a number that you guess between 1 to 20: "))

if (guess>=1 and guess<=20):
        if (guess==num):
            print('You have guessed the correct number. The number was ', num)
        else:
            print('You have guessed the wrong number. The number was ', num)
else:
    print('You have entered an invalid number.')
