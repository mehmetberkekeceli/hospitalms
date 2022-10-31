import random
number = random.randint(1,10)
trying = 3
while trying > 0:
    trying -= 1
    yourGuess = int(input('yourGuess: '))
    if number == yourGuess:
        print("Congrulations!")
        break
    elif number > yourGuess:
        print('up')
    else:
        print('down')

        if trying == 0:
         print(f':/ Please try again. yourGuess : {number}')