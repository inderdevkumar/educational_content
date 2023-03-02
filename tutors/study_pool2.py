
import math

def calculate():
    print("Welcome to the simple math helper.\nWhat would you like to calculate?\n1. Sqrt\n2. Log\n3. Factorial")

    user_math= input()
    
    num= int(input("Enter the number to sqrt:\n"))
    
    cal= 0
    if (user_math == "1"):
        cal= math.sqrt(num)

    elif (user_math == "2"):
        cal= math.log(num)

    elif (user_math == "3"):
        cal= math.factorial(num)
    
    print(cal)
calculate()
