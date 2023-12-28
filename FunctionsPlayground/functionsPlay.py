import random, time, sys

def hello(name):
    print("Hodwy! " + name)

hello("Alice")
print("------------------------------------------------------")

def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return "It is decidedly so"
    elif answerNumber == 3:
        return "Yes"
    
def getAnswerBetter(answerNumber):
    match answerNumber:
        case 1:
           return "It is certain"
        case 2:
            return "It is decidedly so"
        case 3:
           return "Yes"
        case 4:
            return "Reply hazy try again"
        case 5:
           return "Ask again later"
        case 6:
            return "Concentrate and ask again"
        case 7:
           return "My reply is no"
        case 8:
            return "Outlook not so good"
        case 9:
            return "Very doubtful"

rand = random.randint(1,9)
fortune = getAnswerBetter(rand)
print(fortune) #print(getAnswer(random.randint(1,3)))
print("------------------------------------------------------")

def spam():
    global eggs
    eggs = "spam local"
    print(eggs)

def bacon():
    eggs = "bacon local"
    print(eggs)
    spam()
    print(eggs)

eggs = "global"
bacon()
print(eggs)
print("------------------------------------------------------")

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error: invalid argument.")

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
print("------------------------------------------------------")

def samn(divideBy):
    return 42 / divideBy

try:
    print(samn(2))
    print(samn(12))
    print(samn(0))
    print(samn(1))
except ZeroDivisionError:
    print("Error: Invalid argument.")
print("------------------------------------------------------")

indent = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)

        if indentIncreasing:
            indent = indent + 1
            if indent == 20:
                indentIncreasing = False
            
        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True
        
except KeyboardInterrupt:
    sys.exit()