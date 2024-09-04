import os
import random
import sys

def main():
    Name = input("Enter Retard Player: ")
    Revolvers = ['Reichsrevolver', 'ALFA', 'Astra', 'Beretta']

    print("Choose Revolver: ")
    for i in range(len(Revolvers)):
        print(f"{i + 1}. {Revolvers[i]}")

    while True:
        try:
            pick = int(input("Enter choice of gun cyKa!: "))
            if 1 <= pick <= len(Revolvers):
                gunselect = Revolvers[pick - 1]
                break
            else:
                print("BLYAAAAAT нахуй!!!!")
        except ValueError:
            print("Invalid Choice Мудак. Please enter your choice Лох")

    print(f"You chose {gunselect}")
    print("Welcome to Russian Roulette Сука блять!!!")

    while True:
        user = input("Are you ready? [Y/N]: ").strip().upper()
        if user == 'Y':
            break
        elif user == 'N':
            print("Too scared? Exiting...")
            print("/you get shot in the ass...")
            sys.exit()
        else:
            print("Invalid choice. Please enter Y or N.")

    gun = [0,0,0,1,0,0]
    if random.choice(gun) == 1:
        print("RIP_BOZO")
        os.system('taskkill /IM pycharm64.exe /F')
    else:
        print("сказочный долбоёб! It means you survived")

main()
