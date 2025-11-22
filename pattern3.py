'''
    +
    +
+ + + + +
    +
    +

'''

# size = 5
# mid = size//2
size = int(input("Enter number of size you want to enter: "))
mid = size//2

i=0
while i<size:
    j=0
    while j<size:
        if i==mid or j==mid:
            print("+",end=" ")
        else:
            print(" ",end=" ")
        j+=1
    print()
    i+=1