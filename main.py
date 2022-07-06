import faces
import os
from random import randint as rd

while True:
    os.system('cls')
    print('='*10, 'Dice', '='*10)
    amount_dice = input('How many dice do you want to play? ')
    if amount_dice.isdigit():
        amount_dice = int(amount_dice)
        for c in range(amount_dice):
            number = rd(1, 6)
            if number == 1:
                print(faces.one())
            elif number == 2:
                print(faces.two())
            elif number == 3:
                print(faces.three())
            elif number == 4:
                print(faces.four())
            elif number == 5:
                print(faces.five())
            elif number == 6:
                print(faces.six())
        again = faces.check(input('Do you want to play again [Y / N]? '))
        if again:
            print('ok')
        elif not again:
            break            
    else:
        input('Just type numbers!\n') 

    
