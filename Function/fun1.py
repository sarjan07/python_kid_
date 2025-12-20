time = int(input("Enter current time: "))

def gm(name):
    print("Good Morning "+name)

def ga(name):
    print("Good Afternoon "+name)

def ge(name):
    print("Good Evening "+name)

def gn(name):
    print("Good Night "+name)
    
if(time >=1 and time<=11 ):
    gm("Sarjan")
elif(time>=12 and time <=15):
    ga("Sarjan")
elif(time>15 and time <= 21):
    ge("Sarjan")
elif(time>21 and  time<=24):
    gn("Sarjan")
else:
    print("Please enter a valid time")
    
