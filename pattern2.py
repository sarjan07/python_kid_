'''
Pattern 2: Left Aligned Triangle
method -1
*
**
***
****
*****


r= int(input("Enter number of rows: "))
c= int(input("Enter number of columns: "))

i=1
while i<=r:
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    print()
    i+=1
'''
# method -2
'''
1
12
123         place value of j
1234
12345


1
22
333            place value of i
4444
55555
'''

'''
r= int(input("Enter number of rows: "))
c= int(input("Enter number of columns: "))

i=1
while i<=r:
    j=1
    while j<=i:
        print(j,end=" ")
        j+=1
    print()
    i+=1
'''


# Method -3
r= int(input("Enter number of rows: "))

for i in range(1,r+1):
    #         sv, ev r+1(r)
    print("*"*i)