# Write a Python program to read the value of an integer m and display the value of n is 1 when m is larger than 0, 0 when m is 0 and -1 when m is less than 0.
m= int(input("Enter a number: "))

if m>0:
    n=1
elif m<0:
    n=-1
else:
    n=0
    
print("The value of result is ",n)