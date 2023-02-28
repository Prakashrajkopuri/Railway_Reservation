#Railway management system

from random import*
import random
import numpy as np

print("""
-----------------------Welcome to Railway Reservation Portal------------------
******************************************************************************""")
rail_info = """
Choose one of the following option: \n
1.Book Ticket
2.Cancel Ticket
3.Check PNR
4.Check seat availability
5.Create new account
6.Check previous bookings
7.Login
8.Exit
"""

a=0  #global variable
user_details = {1234:['Prakash Raj','0000','Nallapadu',9876543210]}
train_details = {'Odisha' : [12345,[[30,234],[20,424],[23,600]],'wed','cal','kgp'],
                 'Amaravathi': [12121,[[32,234],[20,434],[34,634]],'mon','cal','kgp'],
                 'falaknama':[45672,[[23,255],[34,345],[45,679]],'sun','bhuv','hyd']}
user_bookings ={234567890:[1234,'Prakash Raj','odisha',1,'wed']}
# def function to call the ticket conformation
def confirm_ticket(train_details,train,id,tickets,user_details,coach):
    con = input("confirm? (y/n) : ")
    con=con.lower()
    if con=='y':
        print("Booking successful !")
        pnr =np.random.randint(100000000,999999999) #it generate the pnr number with the help of numpy and random modules.
        user_bookings[pnr]=[id,user_details[id][0],train,tickets,train_details[train][2]]
        print("Please note pnr number : ",pnr)
        c=coach 
        if c=='1ac':
            train_details[train][1][0][0]=train_details[train][1][0][0]-tickets
            print("remaining tickets : ",train_details[train][1][0][0])
        elif c=='2ac':
            train_details[train][1][1][0]=train_details[train][1][1][0]-tickets
            print("remaining tickets : ",train_details[train][1][1][0])
        elif c=='sl':
            train_details[train][1][2][0]=train_details[train][1][2][0]-tickets
            print("remaining tickets : ",train_details[train][1][2][0])
    elif con=='n':
        print("not booked!")

while True:
    print(rail_info)
    option = int(input("Enter your option : "))
    if option==1 :
        def check_user_id(user_details):
            id = int(input("Enter user ID : "))
            if id in user_details:
                def check_password(user_details):
                    pass_word = input("Enter your password : ")
                    if pass_word==user_details[id][1]:
                        print("Welcome ",user_details[id][0],"!")
                        source_station = input("Enter Source station : ")
                        destination_station = input("Enter destination station : ")
                        def check_tain_details(train_details,a):
                            for i in train_details:
                                if source_station in train_details[i] and destination_station  in train_details[i]:
                                    print("Train name : ",i," Number :",train_details[i][0]," Day of Travel : ",train_details[i][2])
                                    a=1
                                else:
                                    a=a+1
                                    if a==3:
                                        print("No trains available!")
                                        return 3
                        b=check_tain_details(train_details,a)
                        if b==3:
                            pass
                        else:
                            def check_train_number(train_details,a):
                                train_number = int(input("Enter train number :"))
                                for i in train_details: 
                                    if train_number in train_details[i]:
                                        print("No of seats available in 1AC :",train_details[i][1][0][0])
                                        print("No of seats available in 2AC :",train_details[i][1][1][0])
                                        print("No of seats available in SL :",train_details[i][1][2][0])
                                        train = i
                                        def check_coach(train_details,train):
                                            coach = input("Enter the coach : ")
                                            coach = coach.lower()
                                            tickets = int(input("Enter the number of tickets : "))
                                            if coach=='1ac':
                                                print("You have to pay : ",(train_details[train][1][0][1])*tickets)
                                                confirm_ticket(train_details,train,id,tickets,user_details,coach)
                                            elif coach=='2ac':
                                                print("You have to pay : ",(train_details[train][1][1][1])*tickets)
                                                confirm_ticket(train_details,train,id,tickets,user_details,coach)
                                            elif coach=='sl':
                                                print("You have to pay : ",(train_details[train][1][2][1])*tickets)
                                                confirm_ticket(train_details,train,id,tickets,user_details,coach)
                                            else : 
                                                print("invalid coach number")
                                                check_coach(train_details,train)
    
                                        check_coach(train_details,train)
                                    else:
                                        a=a+1
                                        if a==3:
                                            print("Invalid train number")
                                            check_train_number(train_details,a)
                            check_train_number(train_details,a)
                    else:
                        print("Entered Invalid password!")
                        check_password(user_details)
                check_password(user_details)
            else:
                print("Invalid user ID !")
                check_user_id(user_details)
        check_user_id(user_details)
    elif option==2:
        def check_user_id(user_details):
            id = int(input("Enter user ID : "))
            if id in user_details:
                def check_password(user_details):
                    pass_word = input("Enter your password : ")
                    if pass_word==user_details[id][1]:
                        print("Welcome ",user_details[id][0],"!")
                        pnr_numer = int(input("Enter your PNR number : "))
                        if pnr_numer in user_bookings:
                            print("booked tickets are : ")
                            print("Name : ",user_bookings[pnr_numer][1])
                            print("Train : ",user_bookings[pnr_numer][2])
                            print("No of tickets : ",user_bookings[pnr_numer][3])
                            print("Day of travel : ",user_bookings[pnr_numer][4])
                            print()
                            print("Do you want to cancel the tickets ")
                            cancel = input("Cancel? y/n : ")
                            cancel = cancel.lower()
                            if cancel=='y': 
                                user_bookings.pop(pnr_numer)
                                print("Canceled tickets successfully!")
                                print("Money will refund in 2 days :)")
                            else:
                                print("Not canceled !")
                        else:
                            
                            print("No bookings!")
                    else:
                        print("Entered Invalid password!")
                        check_password(user_details)
                check_password(user_details)
            else:
                print("Invalid user ID !")
                check_user_id(user_details)
        check_user_id(user_details)
    elif option==3:
        def check_pnr(user_bookings):
            pnr=int(input("Enter your PNR number: "))
            if pnr in user_bookings:
                print("Name: ",user_bookings[pnr][1])
                print("Train Name: ",user_bookings[pnr][2])
                print("No of Tickets: ",user_bookings[pnr][3])
                print("Day of travel:",user_bookings[pnr][4])
            else:
                print("Invalid PNR")
                check_pnr(user_bookings)
        check_pnr(user_bookings)
    elif option==4:
        print("****   Avilable seats   ****")
        src=input("Enter source station: ")
        des=input("Enter destination station: ")
        def check_tain_details(train_details,a):
            for i in train_details:
                if src in train_details[i] and des  in train_details[i]:
                    print("Train name : ",i," Number :",train_details[i][0]," Day of Travel : ",train_details[i][2])
                    a=1
                else:
                    a=a+1
                if  a==3:
                    print("No trains available!")
                    return 3
        b=check_tain_details(train_details,a)
        if b==3:
            pass
        else:
            def check_train_number(train_details,a):
                train_number = int(input("Enter train number :"))
                for i in train_details:
                    if train_number in train_details[i]:
                        print("No of seats available in 1AC :",train_details[i][1][0][0])
                        print("No of seats available in 2AC :",train_details[i][1][1][0])
                        print("No of seats available in SL :",train_details[i][1][2][0])
            check_train_number(train_details,a)
    elif option==5:
        user_name = input("Enter your name : ")
        user_pass = input("Enter your password : ")
        user_home = input("Enter your hometown : ")
        user_phone = int(input("Enter your phone number : "))
        user_id = np.random.randint(1000,9999)
        user_details[user_id]=[user_name,user_pass,user_home,user_phone]
        print("Your user ID is : ",user_id)
    elif option==6:
        def check_user_id(user_details):
            id = int(input("Enter user ID : "))
            if id in user_details:
                def check_password(user_details):
                    pass_word = input("Enter your password : ")
                    if pass_word==user_details[id][1]:
                        print("Welcome ",user_details[id][0],"!")
                        def check_user_details(user_bookings):
                            for p in user_bookings:
                                if id in user_bookings[p]:
                                    print("PNR NO: ",p," ","Train Name: ",user_bookings[p][2]," ","NO of TIckets: ",user_bookings[p][3]," ","Day of travel: ",user_bookings[p][4])
                        check_user_details(user_bookings)
                    else:
                        print("Invalid password")
                        check_password(user_details)
                check_password(user_details)
            else:
                print("Invalid User ID")
                check_user_id(user_details)            
        check_user_id(user_details)
        main=input("press any key to enter main menu: ")
    elif option==7:
        def check_user_id(user_details):
            id = int(input("Enter user ID : "))
            if id in user_details:
                def check_password(user_details):
                    pass_word = input("Enter your password : ")
                    if pass_word==user_details[id][1]:
                        print("Welcome ",user_details[id][0],"!")
                        print("Villege: ",user_details[id][2])
                        print("Cell no: ",user_details[id][3])   
                    else:
                        print("Invalid password")
                        check_password(user_details)
                check_password(user_details)
            else:
                print("Invalid User ID")
                check_user_id(user_details)            
        check_user_id(user_details)
        main=input("press any key to enter main menu: ")
    elif option==8:
        print()
        print("-"*20,'  Thank you  ','-'*20)
        break
    else :
        print("Enter valid option !")
#############################      Thank You        #####################################