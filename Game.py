#Name: Vineet Dcunha
#"I have not given or received any unauthorized assistance on this assignment."

import random
def first_bet (bet_value , initial_value):
    'Bet 1 logic - Rolling dice 1 and dice 2. Checking if user is a winner'
    print('Rolling Dice 1')
    x = random.randrange(1,6) # generate random number between 1 and 6 for dice 1
    print('Your dice 1 returns ', x)
    print('\nRolling Dice 2')
    y = random.randrange(1,6)  # generate random number between 1 and 6 for dice 2
    print('Your dice 2 returns ', y)
    z = x + y
    print('\nSum of both dice is', z)
    if z == 7 or z == 12: # check if sum of dice is 7 or 12
        win_value = 2 * bet_value # win = double bet value
        print('\nCongrats,  you have won!!! Your have won $', win_value)
        current_value = initial_value - bet_value + win_value # Find current value
        return current_value
    else: # if sum of dice is not 7 or 12
        print('\nHard luck... You lose!!! You have lost $', bet_value)
        current_value = initial_value - bet_value # Loose bet value
        double_bet_value = 2 * bet_value # Bet value is doubled
        if (double_bet_value <= initial_value): # Check if user balance to double his bet
            print('\nDo you want to double your bet amount and roll a third dice? ')
            cont = str(input('\nEnter "Y" to roll a third dice, any other value to terminate this round. \n')) # Check if user wants to roll a third dice
            if  cont.upper() == 'Y':
                current_value = second_bet(double_bet_value , bet_value, initial_value, z) # Call function to bet again and roll a third dice
                return current_value
            else:
                print('Round terminated. \n')
                return current_value
        else:
            print('\nYou do not have sufficient amount in your wallet to continue this round. \n')
            current_value = initial_value - bet_value
            return current_value


        
def second_bet (double_bet_value , bet_value, initial_value, z):
    'Bet 2 logic - Rolling dice 3. Checking if user is winner'
    print('\nRolling Dice 3')
    a = random.randrange(1,6) # generate random number between 1 and 6 for dice 3
    print('Your dice 3 returns ', a)
    z = z + a
    print('\nSum of both dice is ', z)
    if z == 7 or z == 12: # if sum of dice is not 7 or 12
        win_triple_value = 3 * double_bet_value  # win = triple bet value
        current_value = (initial_value - double_bet_value) + win_triple_value
        print('\nCongrats,  you have won!!! You have won $', win_triple_value)
        return current_value
    else:
        print('\nHard luck... You lose!!! You have lost $', double_bet_value)
        current_value = initial_value - double_bet_value # Loose bet value
        return current_value


if __name__ == "__main__":
    print('Welcome to the game')
    n = 0
    initial_value = 0
    current_wallet_amount = 0
    value = 0
    play = str(input('Enter "Y" to play, any other value to terminate and end the game. \n')) # Check if user wants to play
    try:
        while play.upper() == 'Y': # Check if user entered value is 'Y'
            if n == 0: # for 1st round
                initial_value = 100 # Load wallet with $100
                print('Your wallet is loaded with $100.')
                try:
                    bet_value = int(input('Enter your bet value. (Your bet value should be less than your wallet amount.) \n'))# Accept user bet value. Input should be number
                except:
                    print('Bet value should be a number.\n')
                    print('\nDo you want to play again?')
                    play = str(input('Enter "Y" to play, any other value to terminate and end the game. \n')) # Check if user wants to play
                    bet_value = int(input('Enter your bet value. (Your bet value should be less than your wallet amount.) \n'))# Accept user bet value. Input should be number
                if bet_value <= initial_value: # The bet value should be less than initial amount
                    value = first_bet(bet_value , initial_value) # Call function to roll round 1 and bet 1
                    print('You have $',value,' in your wallet.\n')
                    n = n + 1
                else:
                    print('Your bet value is more than your current wallet amount. \n')
                current_wallet_amount = value
                print('Do you want to play again?')
                play = str(input('Enter "Y" to play, any other value to terminate and end the game. \n'))# Check if user wants to play
            else:
                try:
                    bet_value = int(input('Enter your bet value. (Your bet value should be less than your wallet amount.) \n'))# Accept user bet value. Input should be number
                except:
                    print('Bet value should be a number.\n')
                    print('\nDo you want to play again?')
                    play = str(input('Enter "Y" to play, any other value to terminate and end the game. \n')) # Check if user wants to play
                    bet_value = int(input('Enter your bet value. (Your bet value should be less than your wallet amount.) \n'))# Accept user bet value. Input should be number
                if bet_value <= current_wallet_amount: # The bet value should be less than wallet amount
                    value = first_bet(bet_value , current_wallet_amount) # Call function to bet again
                    print('You have $',value,' in your wallet.\n')
                    current_wallet_amount = value
                    print('Do you want to play again?')
                    play = str(input('Enter "Y" to play, any other value to terminate and end the game. \n')) # Check if user wants to play
                else:
                    print('Your bet value is more than your current wallet amount. \n')
                    play = str(input('Enter "Y" to play, any other value to terminate and end the game. \n')) # Check if user wants to play
    except ValueError:
        print('Input value not in the right format')
    print('Thank you... Good Bye')
    