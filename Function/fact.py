num = int(input("Enter a number: "))
fact = 1
temp=num
while(num>1):
    fact = fact * num
    num-=1 # num = num-1
print(f"Factorial of {temp} is {fact}")


'''
factorial of a number
5*4*3*2*1
n*(n-1) 
5! = 120
num = 5

fact = fact*num
     =  1  * 5  num=num-1= 5-1 = 4
     =  5  * 4  num=num-1= 4-1 = 3
     = 20  * 3  num=3-1 = 2
     = 60  * 2  num = 2-1 = 1
     = 120 * 1  num =1-1=0 



'''