import random
n = random.randrange(1,20)
guess = int(input("Enter any number: "))
while n!= guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter a number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter a number again: "))
    else:
      break
print("You guessed it asshole!!")
