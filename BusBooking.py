print("____________________ BUS BOOKING ____________________")

# Global variable to store user details
user_details = {}

def login():
    print("For New Register! Enter The Below Details")
    usname = input("Enter Your Name: ")
    usmail = input("Enter Your E-Mail: ")
    age = int(input("Enter Your Age: "))
    phone = input("Enter Your Phone Number: ")

    while True:
        pw = input("Enter Your Password: ")
        cpw = input("Re-Enter Your Password: ")
        if pw == cpw:
            break
        else:
            print("Passwords do not match! Please try again.")

    print("Registration Successful")
    print(" ")

    # Store user details in the global variable
    global user_details
    user_details = {
        "usname": usname,
        "usmail": usmail,
        "age": age,
        "phone": phone,
        "password": pw
    }
    liste=list(user_details)

    while True:
        print("To Login!")
        print(" ")
        usn = input("Enter Your User Name: ")
        usp = input("Enter Your Password: ")
        if usn == usname and usp == pw:
            print("Login Successful!")
            break
        else:
            print("Incorrect username or password. Please try again.")

login()

def details():
    print("User Details:")
    print(f"Name: {user_details['usname']}")
    print(f"E-Mail: {user_details['usmail']}")
    print(f"Phone Number: {user_details['phone']}")

date = input("Date Of Journey: ")
print(f"Available Buses on {date}")

class BusDetails:
    def display_buses(self):
        print("ID : 1 - Name : White Bus - Route : Chennai to Trichy")
        print("ID : 2 - Name : Black Bus - Route : Trichy to Coimbatore")
        print("ID : 3 - Name : Green Bus - Route : Coimbatore to Bengaluru")
        print("ID : 4 - Name : Yellow Bus - Route : Bengaluru to Puducherry")
        print("ID : 5 - Name : Red Bus - Route : Puducherry to Goa")
        self.select_bus()

    def select_bus(self):
        print(" ")
        id = int(input("Select the Bus ID: "))
        if id == 1:
            self.white()
        elif id == 2:
            self.black()
        elif id == 3:
            self.green()
        elif id == 4:
            self.yellow()
        elif id == 5:
            self.red()
        else:
            print("INVALID")

    def white(self):
        print("Boarding Point: New Bus Stop \nDropping Point: Old Bus Stop \nArrival Timing: 9.00pm \nReached Timing: 3.30am ")

    def black(self):
        print("Boarding Point: Junction Bus Stop \nDropping Point: Market Bus Stop \nArrival Timing: 9.00pm \nReached Timing: 2.00am")

    def green(self):
        print("Boarding Point: EvMotors Bus Stop \nDropping Point: CarAccess Bus Stop \nArrival Timing: 9.00pm \nReached Timing: 3.00am")

    def yellow(self):
        print("Boarding Point: College Bus Stop \nDropping Point: School Bus Stop \nArrival Timing: 9.00pm \nReached Timing: 3.00am")

    def red(self):
        print("Boarding Point: Office Bus Stop \nDropping Point: Bank Bus Stop \nArrival Timing: 9.00pm \nReached Timing: 3.00am")

class Booking(BusDetails):
    def bookingg(self):
        print(" ")
        print("--------------------< Booking Your Happy Journey >--------------------")
        busid = int(input("Enter Your Selecting Bus ID: "))
        if busid == 1:
            print(f"Date of Jpurney : {date}")
            print(user_details)
            print("          Bus ID : 1 \n           Name : White Bus \n           Route : Chennai to Trichy")
            self.white()
            print("          Amount : ₹699 \n          GST : 12%\n          Total Price : ₹780")
        elif busid == 2:
            print(f"Date of Jpurney : {date}")
            print(user_details)
            print("          Bus ID : 2 \n           Name : Black Bus \n           Route : Trichy to Coimbatore")
            self.black()
            print("          Amount : ₹699 \n          GST : 12%\n          Total Price : ₹780")
        elif busid == 3:
            print(f"Date of Jpurney : {date}")
            print(user_details)
            print("          Bus ID : 3 \n          Name : Green Bus \n          Route : Coimbatore to Bengaluru")
            self.green()
            print("          Amount : ₹699 \n          GST : 12%\n          Total Price : ₹780")
        elif busid == 4:
            print(f"Date of Jpurney : {date}")
            print(user_details)
            print("Bus ID : 4 \n           Name : Yellow Bus \n           Route : Bengaluru to Puducherry")
            self.yellow()
            print("Amount : ₹699 \n          GST : 12%\n          Total Price : ₹780")
        elif busid == 5:
            print(f"Date of Jpurney : {date}")
            print(user_details)
            print("Bus ID : 5 \n          Name : Red Bus \n          Route : Puducherry to Goa")
            self.red()
            print("Amount : ₹699 \n          GST : 12%\n          Total Price : ₹780")
        else:
            print(" ")
            print("Invalid! Bus Id.")
            print("Re-Booking... ")
            booking.bookingg()

bus_details = BusDetails()
bus_details.display_buses()

while True:
    print(" ")
    print("Choose The Option :")
    print("1. See Again Avalable Bus")
    print("2. Booking Ticket")
    option = int(input("Enter the options :"))
    if option == 1:
        bus_details.display_buses()
    elif option == 2:
        break
    else:
        print("Invalid! Option.")
        bus_details.display_buses()

booking = Booking()
booking.bookingg()

class bill():
        def pay(self):
            print(" ")
            payment = input("Conform Your Ticket ---->  Yes / No :")

            if payment == "yes" and "YES":
                print("[Successfully! \nYours Bus Ticket Was Booked\nHave a Great Journey!]")

            elif payment == "no" and "NO":
                booking.bookingg()
                paybill.pay()

            else:
                print("Invalid! Answer")
                booking.bookingg()

paybill=bill()
paybill.pay()

hello
