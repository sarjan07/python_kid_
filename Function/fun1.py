time = int(input("Enter current time: "))

def gm(name = "Sarjan"):
    print("Good Morning "+name)

def ga(name = "Sarjan"):
    print("Good Afternoon "+name)

def ge(name): # without return type with argument
    print("Good Evening "+name)

def gn(name = "Sarjan"): # without return type with argument with default paramater
    print("Good Night "+name)
    
if(time >=1 and time<=11 ):
    gm()
elif(time>=12 and time <=15):
    ga()
elif(time>15 and time <= 21):
    ge()
elif(time>21 and  time<=24):
    gn()
else:
    print("Please enter a valid time")
    
