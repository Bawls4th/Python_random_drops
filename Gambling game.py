import random
import sys


def casino_cardgame():
    print("BLYYYYAAAAAT! Welcome to Casino.")

def lost_financial():
    print("You've gone financial debt. Thanks for wasting your shit.")

def main():
    casino_cardgame()

    name = input("Name: ")
    money = int(input("Enter amount of money from your financial: "))
    print(f"Welcome {name}. Your initial financial amount is ${money}.")

    gambling = True
    while gambling:
        while True:
            try:
                bet = int(input("Place your bet: "))
                if bet > 0 and bet <= money:
                    break
                elif bet > money:
                    print("Bet on exceeds your money idiot. ")
                elif bet == 0:
                    print("GET OUUUTTT!!!")
                    sys.exit()
                else:
                    print("Bet more Pusssys. ")

            except ValueError:
                print("Is u retard ehh? Bet MONEEEEYY!!!!!!.")

        player_card = random.randint(1, 15)
        dealer_card = random.randint(1, 15)

        print(f"Your card is {player_card}. Dealer's card is {dealer_card}.")

        if player_card == dealer_card:
            print("Draw!")
        elif player_card > dealer_card:
            print(f"You win ${bet} Lucky Bastard!")
            money += bet
        else:
            print(f"Dealer wins ${bet}, Bitch!!!")
            money -= bet

        if money <= 0:
            print("You're out of Financial money!")
            lost_financial()
            break
        else:
            while True:
                state = input("Do you want to keep playing? (Losers Never Quit) [Y/N]: ")
                if state == 'y' or state == 'Y':
                    break
                elif state == 'n' or state == 'N':
                    print(f"Thanks for wasting your time cyKAAAA! Your financial money is ${money}.")
                    gambling = False
                    break
                else:
                    print("Invalid Dickhead. Please enter Y or N: ")

main()
