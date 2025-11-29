n = int(input("Enter size of array : "))
arr =[]

print("Enter array element: ")
i=0
while i<n:
    arr.append(int(input()))
    # i = i+1
    i+=1
    
print("Array : ",arr)

search = int(input("Enter number to search: "))

i=0
found = False
while i<n:
    if arr[i] == search:
        found = True
        break
    i+=1
    
if found:
    print("Element found successufully.....................")
else:
    print("Element not found...............")