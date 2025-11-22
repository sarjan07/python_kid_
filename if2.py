# Write a program that calculates the annual bonus for an employee
#  based on their years of service and performance rating. The rules are:
#  • If years of service are greater than 10 and bonus is 20% of salary.
#  • If years of service are between 5 and 10 and bonus is 10% of salary.
#  • If years of service are less than 5 and bonus is 5% of salary.
#  • Otherwise, no bonus.

ys= int(input("Enter years of service: "))
sal = int(input("Enter your salary: "))

bonus=0

if ys > 10:
    bonus=0.20*sal
elif 5 <=ys <=10:
    bonus=0.10*sal
elif ys < 5:
    bonus=0.05*sal
else:
    bonus=0
    
print("Bonus :",int(bonus))