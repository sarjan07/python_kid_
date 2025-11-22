num = int(input("Enter a number: ")) //num =123
rev=0

while(num>0):
	digit = num%10  //digit = 1%10 = 1
	rev = rev*10+digit  // rev= (32*10) + 1 = 320+1=321 
	num = num/10 //num = 1/10
	
print("Reversed number : " ,rev)
