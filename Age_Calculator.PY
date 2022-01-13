import time

age= int(input("Enter your age or Year of birth "))
currentYear=2022
yob =0 
lsAge=len(str(age))

if lsAge==4:
    yob=age
elif lsAge<=2:
    yob=currentYear-age
    print(age,yob)
else:
    print("enter valid")

while True:
    print("\n\n\n\n\n\n\nWelcome to Mystic's Age Calculator \n What do you want to do ")
    a=int(input("1-To see when you will turn 100.    \n2-To see when you will turn a particular age    \n3-To see your age on particular age  \n4-Quit \n (Enter the coresponding number )\n-"))
    if a==1:
        print(f"You will turn 100year old in {yob+100} ")
    elif a==2:
        pin=int(input("enter age "))
        print(f"you will turn {pin}year old in {pin+yob} ")
    elif a==3:
        pyr=int(input("enter year"))
        print(f"you will be {pyr-yob}  years old in {pyr} ")
    elif a==4:
        print("thankyou for using our age calculator")
        break
    else:
        pass
    time.sleep(3)
