def collatz(number):
    if number % 2 == 0:
        print(int(number/2))
        return number/2
    else:
        print(int(3 * number + 1))
        return 3 * number + 1
    
try:
    num = int(input("Insert number to analyse: \n"))
    while num != 1:
        num = collatz(num)
except ValueError:
    print("Mi sa che qua ti serve un po' di Cambly, diomeo")