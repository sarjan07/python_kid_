# for: when you know how many number of iterations you want to perform
# while: when you don't know how many number of iterations you want to perform

num = int(input("Enter a number: ")) # num =123
rev=0

temp=num
while(num>0):
	digit = num%10  # digit = 1%10 = 1
	rev = rev*10+digit  # rev= (32*10) + 1 = 320+1=321 
	num = num//10 
	
print("Reversed number : " ,rev)
if temp == rev:
    print("Number is a Palindrome.....")
else:
    print("Number is not a Palindrome.....")