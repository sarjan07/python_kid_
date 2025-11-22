'''
Pattern - 1 Sqaure Pattern
Method -1
 *****
 *****
 *****
 *****
 *****
'''

# for i in range(5): #row
#     for j in range(5): #column
#         print("*", end=" ")
#     print()
    
# end works for not letting print go to the next line

# Method -2
r= int(input("Enter number of rows: "))
c= int(input("Enter number of columns: "))


i=0
while i<r:
    j=0
    while j<c:
        print("*",end="")
        j+=1 #j++ or j=j+1
    print()
    i= i+1 # i = i+1


# Pattern - 2
'''
11111
22222
33333
44444
55555

12345
12345
12345
12345
12345

'''
'''r= int(input("Enter number of rows: "))
c= int(input("Enter number of columns: "))


i=1
while i<=r:
    j=1
    while j<=c:
        print(j,end=" ")
        j+=1
    print()
    i= i+1 # i = i+1
'''