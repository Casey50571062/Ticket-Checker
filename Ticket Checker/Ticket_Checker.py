from datetime import date as dy
import sys 

def checkerInt(Value):
    fail = True
    while fail == True:
        try:
            Value= int(Value)
            fail=False
            return Value
        except:
            print("Unable to complete")
            fail = True
            Value = input("A number: ")

print("Welcome to Copington Adventure park")
print("Adult tickets cost £20""\nChild tickets cost £12""\nSenior tickets cost £11")

Adult = input("How many adults are going: ")
tickets=checkerInt(Adult)*20
Child = input("How many Children  are going: ")
tickets+=checkerInt(Child)*12
Senior = input("How many Seniors are going: ")
tickets+=checkerInt(Senior)*11
wristbands = input("How many wristbands will you be buying: ")
wristbands=checkerInt(wristbands)
tickets+=wristbands*20

Name = input("What is the best persons last name: ")
Parking_pass = input("Do you need a parking pass? Enter Y or N: ").upper()
while Parking_pass != "Y" and Parking_pass != "N":
    Parking_pass = input("Do you need a parking pass? Enter Y or N: ").upper()

print(f"Your total is £{tickets}")
input("Now onto payment, our machine only takes £20 and £10's, we will manually give out change :3")
payed=0
while payed < tickets:
    entered =  input("Do you want to enter a £20 or a £10")
    if entered == "20":
        payed+=20
    elif entered == "10":
        payed+=10
    elif entered == "card":
        payed = tickets
    else:
        print("please enter one")
change = payed-tickets
if change>0:
    print(f"Your change is {change}")

print(f"\nYour ticket {Name}: ")
print(f"Amount of tickets bought {Adult+Child+Senior}")
print(f"Amount of Wristbands bought { wristbands}")
print(f"Your total is £{tickets}")
print(f"Todays date {dy.today()}")
if Parking_pass == "Y":
    print("Parking pass obtained")
print("\nThank you for your purchase")
    