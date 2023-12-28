import random, sys

#msg = "Roll the doyce"
#print(msg)

#for i in range(1,10,2):     # inizializzatore, condizione, iteratore
#    print(random.randint(1,20))

found = False
counter = 0
secretNumber = random.randint(1,20)
print("I'm thinking 'bout a number between 1 and 20. \nTake a guess:")

while found == False:
    guess = input()
    counter += 1
    if int(guess) < secretNumber:
        print("Your guess is too low")
    elif int(guess) > secretNumber:
        print("Your guess is too high")
    else:
        print("Good job! You guessed my number in " + str(counter) + " guesses!")
        found = True

while True:
    print("Type 'exit' to exit.")
    response = input()
    if response == 'exit':
        sys.exit()
    print("You typed " + response + ".")

match term:
    case pattern1:
        action1
    case pattern2:
        action2
    case pattern3:
        action3
    case _:
        defaulltAction