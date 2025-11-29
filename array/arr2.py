# take a value from user in array and display it

n = int(input("Enter array size: "))
# n=4

sum=0
arr=[]
i=0
while i<n:
    num=int(input())
    arr.append(num)
    i +=1

i=0
while i<n:
    sum = sum + arr[i]
    i+=1

print("Array element are: ",arr)
print("Sum of array :",sum)