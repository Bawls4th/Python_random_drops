import random
pp = random.randrange(1,20)
guess = int(input("Enter any number: "))
while pp!= guess:
    if guess < pp:
        print("The number is too low twat.")
        guess = int(input("Enter a number again: "))
    elif guess > pp:
        print("The number is to high cunt.")
        guess = int(input("Enter a number again: "))
    else:
      break
print("You guessed it asshole!!")
