import random
def casino_cardgame():
    a = "Welcome To python gamble bet money/life savings"

    print(a)

def lost_financial():
    wp = "You've Gone Debt. Thx For Playing."

    print(wp)

def main():
    casino_cardgame()

    Name = input("Name of lucky Bastard: ")
    dolla = int(input("Amount of Money: "))
    print("Welcome Mr./Ms. " + Name + ". Your Financial Money is " + str(dolla) + " of Savings.")

    Gambling = True
    while Gambling:
        bet = input("Place your Financial Bet: ")
        nobet = int(bet) == 1 or int(bet) <= -1
        while nobet:
            print("Nigga is Pussy.")
            bet = input("Bet MORE!!!: ")
            nobet = int(bet)  == 1 or int(bet) <= -1

        bet = int(bet)

        PlayerCard = random.randint(1, 15)
        DealerCard = random.randint(1, 15)

        print("Your card is " + str(PlayerCard) + ". CPU card is " + str(DealerCard) + ".")

        if PlayerCard == DealerCard:
            print("Draw, Lucky shit.")
            money = dolla
        elif PlayerCard > DealerCard:
            print("You win " + str(bet) + " You Bastard")
            money = dolla + bet
        else:
            print("Dealer Won  " + str(bet) + " You're Bankrupt Bitch")
            money = dolla - bet

        if money == 0:
            print("You're out of money!")
            lost_financial()
            DophamineGamb = False
            break
        else:
            print("Your money is now " + str(money) + " Gold.")
            state = input("Keep PLaying? [Y/N]  (Winners never quit) ")
            if state == 'y' or state == 'Y':
                DophamineGamb = True
            elif state == 'n' or state == 'N':
                print("Youre Financial Saving is " + str(money) + " Quitter...")
                print("Thanks For wasting your time.")
                break
main()