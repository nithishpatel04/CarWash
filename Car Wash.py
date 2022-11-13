# Car wash Program by Nithish Patel, Varala
global f
f=0
def user_type():
    global f
    f=f+1
# Defined Admin & User Based Login
    print("enter user/admin login:")
    print("1,user")
    print("2,admin")
    print("3,back")
    log=int(input("choose login type:"))
    if log == 1:
        signup()
        login()
        return 0
    elif log == 2:
        admin_login()
        return 0
# Sign Up Option for new customers
def signup():
    sign=({"name":str(input("enter user name")),"password":str(input("enter password:"))})
    login=[sign]

# Login for existing  customers
def login():
        if str(input("enter user name")) == login("name") and str(int(input("enter password"))) == login("password"):
            print("login successful")
            print("where you want to wash your car?:")
            print("1,Hyderabad")
            print("2,Bangalore")
            print("3,Delhi")
            place = int(input("choose your option: "))
            if place == 1:
                print("Thanks for choosing Hyderabad Location, Please Continue.")
                print("checking book availabity")
                def bookings():
                    booking = []
                    if len(booking) <= 5:
                        print("booking is available")
                        status()
                    else:
                        print("bookings are not available")

                def status():
                    s = int(input("press 1 for confirm bookings:"))
                    print(s)
                    if s == 1:
                        print("booking success")
                        booking.append(1)
                    else:
                        print("booking rejected")
                    return status

            elif place == 2:
                print("Thanks for choosing Bangalore Location, Please Continue.")
                print("checking book availability")
                def bookings():
                    booking = []
                    if len(booking) <= 5:
                        print("booking is available")
                        status()
                    else:
                        print("bookings are not available")

                def status():
                    s = int(input("press 1 for confirm bookings:"))
                    print(s)
                    if s == 1:
                        print("booking success")
                        booking.append(1)
                    else:
                        print("booking rejected")
                    return status

            elif place == 3:
                print("Thanks for choosing Delhi Location, Please Continue.")
                print("check booking availability")
                def bookings():
                    booking = [0]
                    if len(booking) <= 5:
                        print("booking is available")
                        status()
                    else:
                        print("bookings are not available")

                def status():
                    s = int(input("press 1 for confirm bookings:"))
                    print(s)
                    if s == 1:
                        print("booking success")
                        booking.append(1)
                    else:
                        print("booking rejected")
                    return status

            else:
                print("Service is not available, Please Select Listed Cities.")
        else:
            print("invalid details")

# For Admin login
def admin_login():
    name=str(input("enter admin name:"))
    password=str(input("enter password:"))
    if name == "nithish" and password == "123456":
        location()
    else:
        print("invalid details")

def location():
    print("1,service available in the cities")
    print("2,add carwash service in this location")
    service = [hyd, bangalore, delhi]
    choose=int(input("enter your choice:"))
    if choose == 1:
        print("service available in:")
        print(service)
        pick=str(input("service in:"))
        if service == pick:
            print("service is available here")
            print(f"You have choose :{pick}")
            if pick == hyd:
                def orders():
                    order=[]
                    if len(order) <= 5:
                        print("orders available")
                        print("press 1 to add order")
                        o=int(input())
                        if o == 1:
                            print("booking confirmed")
                            order.append(1)
                        else:
                            print("booking rejected")

                    else:
                        print("booking not available")

            elif pick == bangalore:
                def orders():
                    order = []
                    if len(order) <= 5:
                        print("orders available")
                        print("press 1 to add order")
                        o = int(input())
                        if o == 1:
                            print("booking confirmed")
                            order.append(1)
                        else:
                            print("booking rejected")

                    else:
                        print("booking not available")
            elif pick == delhi:
                def orders():
                    order = []
                    if len(order) <= 5:
                        print("orders available")
                        print("press 1 to add order")
                        o = int(input())
                        if o == 1:
                            print("booking confirmed")
                            order.append(1)
                        else:
                            print("booking rejected")

                    else:
                        print("booking not available")


        else:
            print("service not available")

    elif choose == 2:
        print("add service in:")
        add=str(input())
        service.append(add)

    else:
        print("invalid")




