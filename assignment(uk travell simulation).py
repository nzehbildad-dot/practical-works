user_name=input("Please enter your name: ")
list_of_passports = ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown"]
otp_code=[]
pin=[8783,7732,9393,3243]
passcode_1=[]
import random


def passport_checking():
    if user_name in list_of_passports:
        print("Passport verified.")
        apply_for_visa()
    else:
        print("Passport not found. please renew")
        renew_passport()

def renew_passport():
    print("PASSPORT RENEWAL PASSWORD")
    nin_portal= {
    202902901: "John doe",
    939203902: "jane smith",
    210023021: "alice johnson",
    839920938: "bob brown"
    }
    nin=int(input("Please enter your National Insurance Number: "))
    if nin in nin_portal:
        print ("passport renewed")
        apply_for_visa()
    else:
        print("please go to ur nearset nin office and register: ")

def apply_for_visa():
    PRINT("VISA APPLICATION")
    chioce=random.randint(0,1)
    name= input("input ur name: ")
    if name == user_name:
        nin2=int(input("input ur nin: "))
        reason_for_travel=input("input ur reason for travel: ")
        duration=input("how long are you staying: ")
        fee=int(input("you are to pay the sum 3000 GDP pls input ur pin:"))
        if fee in pin:
            for i in range(6):
                print("loading...............")
            if chioce == 0:
                print("visa request rejected")
            else:
                otp=random.randint(16561,987263)
                otp_code.append(otp)
                print("this is ur visa otp don't lose it ",otp)
                booking_flight()
    else:
         print("name not in database")

def booking_flight():
    print("book flight")
    from_current=input("input your cuurent country")
    going_to=input("input the country u are going to ")
    if going_to == "unitedkingdom":
        namew=input("input your name on ur passport")
        if namew == user_name:
            reboat=int(input("pls input ur visa otp"))
            if reboat in otp_code:
                fee_booking=int(input("that will cost 123,984 naira pls input card pin "))
                if fee_booking in pin:
                    for i in range(6):
                        print("loading........")
                    passcode=random.randint(632617,876524)
                    passcode_1.append(passcode)
                    print("this is ur passcode use it when boarding flight ",passcode)
                    boarding_flight()
    else:
         print("Sorry all flights are closed only flights going to unitedkingdom is available ")

def boarding_flight():
    PRint("boarding flight")
    koat=int(input("please into ur passcode"))
    if koat in passcode_1:
        print(" Please resume boarding ")
        arrive()
    else:
        print("invaild")

def arrive():
    print("welcome to the united kingdom")
    gia=int(input("please input ur visa otp"))
    if gia in otp_code:
        print(" enjoy ur stay")
    else:
        print("please what here the securty will soon be here")

passport_checking()


    
