# Importing time and math libraries.
import time
import math

t = 3

while True:
        # Taking an input from user for transaction.
    print("1: Add, 2: Subtract, 3: Multiply, 4: Divide, 5: Take Power, 6: Square Root, 7: Take Absolute")
    transaction = int(input("Pick a transaction: "))

    # Addition
    if transaction == 1:
        # Taking values.
        num1 = int(input("First Number: "))
        num2 = int(input("Second Number: "))
        result = num1 + num2
        print("The sum of ", num1, " and ", num2, " is ", result)
        time.sleep(t)

    # Subtract
    elif transaction == 2:
        # Taking values.
        num1 = int(input("First Number: "))
        num2 = int(input("Second Number: "))
        result = num1 - num2
        print(num1, " out of ", num2, " is ", result)
        time.sleep(t)

    # Multiply
    elif transaction == 3:
        # Taking values.
        num1 = int(input("First Number: "))
        num2 = int(input("Second Number: "))
        result = num1 * num2
        print(num1, " times ", num2, " is ", result)
        time.sleep(t)

    # Divide
    elif transaction == 4:
        # Taking values.
        num1 = int(input("First Number: "))
        num2 = int(input("Second Number: "))
        result = num1 / num2
        print(num1, " over ", num2, " is ", result)
        time.sleep(t)

    # Power
    elif transaction == 5:
        # Taking values.
        num = int(input("Number: "))
        power = int(input("Power: "))
        try:    
            result = math.pow(num, power)
            print(num, " to the power of ", power, " is ", result)
        except:
            print("You can not even read this integer.")
        time.sleep(t)

    # Square root
    elif transaction == 6:
        # Taking value.
        num = int(input("Number: "))
        result = math.sqrt(num)
        print("Square root of ", num, " is ", result)
        time.sleep(t)

    # Absolute
    elif transaction == 7:
        num = int(input("Mutlak değeri alınacak sayı: "))
        result = abs(num)
        print("The absolute value of ", num, " is ", result)
        time.sleep(t)

    else:
        print("There is no such transaction.")
        time.sleep(t)