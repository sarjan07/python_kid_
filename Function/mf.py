def calculator(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    return sum,sub,mul
# Function with multiple return types

no1 = int(input("Enter number 1: "))
no2 = int(input("Enter number 2: "))

sum,sub,mul = calculator(no1,no2)


print("Sum ",sum)
print("Subtraction ",sub)
print("Multiplication ",mul)