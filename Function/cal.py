# with return type with argument

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b
def div(a,b):
    return a/b

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
choice = int(input("Enter your choice(1-4)"))

if(choice == 1):
    print("Sum of 2 numbers are " , add(num1,num2))
elif(choice == 2):
    print("Subtraction of 2 numbers are " , sub(num1,num2))
elif(choice == 3):
    print("Multiplication of 2 numbers are " , mul(num1,num2))
elif(choice == 4):
    print("Division of 2 numbers are " , div(num1,num2))
else:
    print("Please enter a valid choice......")