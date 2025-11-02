num1=input("Enter number 1: ")
num2 = input("Enter number 2: ")
num3 = input("Enter number 3: ")

if num1>num2:
    if num1>num3:
        print(num1," is greatest...")
    else:
        print(num3," is greatest...")
elif num2>num3:
    if num2>num1:
        print(num2, " is greatest...")
    else:
        print(num1," is greatest...")
elif num3>num1:
    if num3>num2:
        print(num3," is greatest...")
    else:
        print(num2, " is greatest...")
else:
    print("Enter a valid number...")
    
# enter number: 55
# o/p: 55 is divisible by 11 and 5
