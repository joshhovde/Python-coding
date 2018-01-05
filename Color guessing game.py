import random

words =('green', 'red', 'black', 'blue', 'orange', 'purple', 'brown', 'pink', 'yellow')
secretColor = random.choice(words)
print("Hellow. What is your name?")
name = input()
print(name + ' I am thinking of a "basic" random color. Can you guess what it is? ')


while True:
    guess = input()
    if guess in secretColor:
        print("good job you guessed correctly! Lets play again. Whats your next guess? ")
        continue
    else:
        print ("try again")
