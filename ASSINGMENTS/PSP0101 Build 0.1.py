# *********************************************************
# Program: TLXV_GX.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Tutorial Section: TLX Group: TL15
# Trimester: 2215
# Year: 2022/23 Trimester 1
# Member_1: ID 1221101112 | NAME : NISRINA MASYITAH BINTI MOHD NOR ZAIDI
# Member_2: ID 1221100800 | NAME : MUHAMMAD AZHAR BIN AHMAD ROSEHAIZAT
# Member_3: ID 1221101663 | NAME : LEE KAI VERN
# Member_4: ID 1221101288 | NAME : SUA WEI KHONG
# *********************************************************
# Task Distribution
# Member_1:
# Member_2:
# Member_3:
# Member_4:
# *********************************************************
# d. Your program must have ALL of the following MINIMUM requirements:
#i. Account sign up and login authentication: //
#1. Sign up for new users. //
#2. Login for registered users. //
#3. Login for administrator. //
#ii. Create, read, update, and delete (CRUD) operations using list, tuple, set and/or dictionary. //
#iii. Menu display for users and administrators. // 
#iv. Must create at least 3 different features for users and administrators.
#Seat //
#Timetable /
#Ticket purchase /
#v. Must prompt the user for input and validate data entry.
#vi. Must be written in Python programming language version 3.xx using only standard libraries (example: random, math, datetime). No unnecessary imports are allowed. Please discuss with your lecturers on which libraries can be imported.
#vii. Write sufficient comments in the script to explain your program.


#CHANGE MENU DISPLAY TO LOOP????
#THIS APPLIES TO ALL MENU DISPLAYS IN PROGRAM
#HAVE AN EXIT FEATURE ON THE MENU DISPLAY
#Tickets
#Change seats to dictionaries? maybe with all the classes
#or use if else
#for the last feature a ticket payment where it calculates the cost based on seats bought?





import re

#importing regex to limit the formating of user input when inputing dates and times
#this is to prevent the printed timetables to be broken by strange inputs
dateformat = "[0-3][0-9]/[0-1][0-9]/[0-9][0-9][0-9][0-9]"
#define the pattern/format of the date by only allowing digits of 0 to 3 and 0 to 9 for the DD
#Only allowing digits of 0-1 and 0-9 for the MM
#Only allowing the year to be 4 digits and the DD MM and YYYY must be split with a "/"

timeformat = "[0-2][0-9]:[0-5][0-9]"
#defining the patter/format of the time by only allowing digits of 0 - 2 and 0-9 for the HH
#only allowing digits of 0-5 and 0-9 for the MM and the HH and MM must be split with a ":"

#Admin Check
print("=" * 30, "\n\tAdmin Check\n","=" * 30 )
print("[1]Admin")
print("[2]Regular User")
admincheck = input("Please select an option: ")
while admincheck.lower() not in ("1", "2"):
    admincheck = input("Please select a valid option: ")
if admincheck.lower() == "1":
    print("Welcome to the program, admin")
    admin = True
else:
    print("Welcome to the program, user")
    admin = False
#Menu display asking the user if they are an admin or user
#if admin is chosen, a Boolean value named admin is set to True and vicevera
#this Boolean value will be used to allow only admins to modify the data


#Seat funtcion
#maybe add a menu dispay to book destination?

Seats = []
Letter = "A"
for x in range (1,7):
    Letter = "A"
    for i in range (0,9):
        Seats.append(Letter + str(x))
        Letter = chr(ord(Letter) + 1)

#A loop to print out a list of strings "A1" till "I6"
#Letter is initialised as "A"
#A nested for loop with the range 0,9(for the amount of characters A to I) then adds the strings A1, B1 , C1......I1 to the list
#this is done by changine the letter to its ASCII value and adding by 1 for every letter
#the outer for loop changes the number increment by 1

booked_seats = []

def seat():
    #have to make global variable or pass parameter i think idk
    #could probably add class of seats
    #maybe would be better to use dictionaries idk

    n = 0
    while n < len(Seats):
        if n == 0:
            print("BUSINESS CLASS".center(42,"="))
        if n == 18:
            print("FIRST CLASS".center(42,"="))

        if n == 36:
            print("ECONOMY CLASS".center(42,"="))
        print("|{}|{}|{}|\t|{}|{}|{}|\t|{}|{}|{}|".format(Seats[n],Seats[n+1],Seats[n+2],Seats[n+3],Seats[n+4],Seats[n+5],Seats[n+6],Seats[n+7],Seats[n+8]))
        #OR
        #print(f"|{Seats[n]}|{Seats[n+1]}|{Seats[n+2]}|\t|{Seats[n+3]}|{Seats[n+4]}|{Seats[n+5]}|\t|{Seats[n+6]}|{Seats[n+7]}|{Seats[n+8]}|\t")
        n = n + 9 
    book = input("What seat would you like to book?")
    while book.upper() not in (Seats):
        book = input("Please choose an available seat")
    count = 0
    while count < len(Seats):
        if book.upper() == Seats[count]:
            del Seats[count]
            Seats.insert(count,"XX")
            break
        else:
            count = count + 1

            
    print("Your chosen seat is {}".format(book.upper()))
    booked_seats.append(book.upper())


    #add a list of bought tickets
    #number of tickets bought = length of list

def tickets_payment():
    #Check the class of ticket
    #Rn the class of ticket is based on the number(1 to 2 is Business, 3 to 4 is First Class, 5 to 6 is economy)
    #maybe change to dictionaries but idk

    business_count = 0
    first_count = 0
    economy_count = 0
    #Initialising the number of tickets for each class as 0

    for b in booked_seats:
        if b[1] in ("1","2"):
            business_count = business_count + 1
        elif b[1] in ("3","4"):
            first_count = first_count + 1
        elif b[1] in ("5","6"):
            economy_count = economy_count + 1
    total = (business_count * business_price) + (first_count * first_price) + (economy_count * economy_price)

    print(f"Your final total is: {total}")
    
    
    #A for loop that iterates through every element in booked_seats
    #Checks the second character of every element and adds 1 to the corresponding class(1 to 2: Business, 3 to 4:First, 5 to 6: Economy)

    print(f"Business Class tickets: {business_count}")
    print(f"Firs Class Tickets: {first_count}")
    print(f"Economy Class Tickets: {economy_count}")


business_price = 200
first_price = 100
economy_price = 50
def tickets():
    if booked_seats == []:
        print("Please select a seat first.")
        return
    else:
        if admin == False:
            print(booked_seats)
            tickets_payment()
        if admin == True:
            #menu display to ask which price to change
            while True:
                print("[1]Business Price")
                print("[2]First Price")
                print("[3]Economy Price")
                print("[4]Exit")
                menu2 = input("Please select an option: ")
                while menu2 not in ("1","2","3","4"):
                    menu2 = input("Please select a valid option: ")

                if menu2 == "1":
                    businss_price = int(input("What is the new business class ticket price: "))
                if menu2 == "2":
                    first_price == int(input("What is the new first class ticket price: "))
                if menu2 == "3":
                    economy_price == int(input("What is the new economy class ticket price: "))
                if menu2 == "4":
                    break
            

            
            








#Finish off arrival timetable //
#Figure out how to limit formating for updating and adding flights //
#Implement a search feature for non admins

#Arrivals Data
arrivals_date = ["DATE","2/3/2023", "2/3/2023" , "2/3/2023" , "3/3/2023", "3/3/2023", "3/3/2023"]
arrivals_time = ["TIME","08:00" , "15:00", "19:00", "10:00", "14:00", "21:00"]
arrivals_airline = ["AIRLINE","Malaysian Airlines", "Air Asia", "Qatar Airways", "British Airways", "Malaysian Airlines", "Emirates"]
origin = ["ORIGIN","Anchorage","Vienna","Istanbul","Split","Marrakesh","Monaco"]
#Departures Data
departures_date = ["DATE","2/3/2023", "2/3/2023" , "2/3/2023" , "3/3/2023", "3/3/2023", "3/3/2023"]
departures_time = ["TIME","08:00" , "15:00", "19:00", "10:00", "14:00", "21:00"]
departures_airline = ["AIRLINE","Malaysian Airlines", "Air Asia", "Qatar Airways", "British Airways", "Malaysian Airlines", "Emirates"]
departures_destination = ["DESTINATION","Jakarta", "London", "Lisbon", "Buenos Aires", "New York City", "Cape Town"]

def add_flight(timetabletype):
    new_date = input("What is the date of the new flight(dd/mm/yyyy): ")
    while True:
        if re.match(dateformat, new_date):
            break
        else:
            new_date = input("Please enter the date in dd/mm/yyyy format: ")
        
    
    new_time = input("What is the time of the new flight(HH:MM): ")
    while True:
        if re.match(timeformat, new_time):
            break
        else:
            new_time = input("Please enter the time in HH:MM format: ")
        
    new_airline = input("What is the airline of the new flight: ")

    if timetabletype == "departures":
        new_destination = input("What is the destination of the new flight: ")
        departures_date.append(new_date)
        departures_time.append(new_time)
        departures_airline.append(new_airline)
        departures_destination.append(new_destination)
    else:
        new_origin = input("What is the origin of the new flight: ")
        arrivals_date.append(new_date)
        arrivals_time.append(new_time)
        arrivals_airline.append(new_airline)
        origin.append(new_origin)





def update_flight(timetabletype):
    line = int(input("Which flight you wish to update (Please enter no.): "))
    while True:
        if timetabletype == "departures":
            while line not in range (1,len(departures_date)):
                line = int(input("Please enter a valid number: "))
            print("[1]Date")
            print("[2]Time")
            print("[3]Airline")
            print("[4]Destination")
            print("[5]Exit")
        else:
            while line not in range (1,len(arrivals_date)):
                line = int(input("Please enter a valid number: "))
            print("[1]Date")
            print("[2]Time")
            print("[3]Airline")
            print("[4]Origin")
            print("[5]Exit")

        update_menu = input("Which element would you like to update: ")
        while update_menu not in ("1","2","3","4","5"):
            update_menu = (input("Option invalid, try again"))

        if update_menu == "1":
            update_date = input("What is the new date: ")
            while True:
                if re.match(dateformat, update_date):
                    break
                else:
                    update_date = input("Please enter the date in dd/mm/yyyy format: ")
            if timetabletype == "departures":
                departures_date[line] = update_date
            else:
                arrivals_date[line] = update_date

        if update_menu == "2":
            update_time = input("What is the new time of the flight: ")
            while True:
                if re.match(timeformat, update_time):
                    break
                else:
                    update_time = input("Please enter the time in HH:MM format: ")
            if timetabletype == "departures":
                departures_time[line] = update_time
            else:
                arrivals_time[line] = update_time
        
        if update_menu == "3":
            update_airline = input("What is the new airline of the flight: ")
            if timetabletype == "departures":
                departures_airline[line] = update_airline
            else:
                arrivals_airline[line] = update_airline

        if update_menu == "4":
            if timetabletype == "departures":
                update_destination = input("What is the new destination of the flight")
                departures_destination[line] = update_destination
            else:
                update_origin = input("What is the new origin of the flight")
                origin[line] = update_origin

        if update_menu == "5":
            break
            
def delete_flight(timetabletype):
    remove = int(input("Which flight would you like to delete: "))
    #allow exit sequeunce?
    if timetabletype == "departures":
        while remove not in range (1,len(departures_date)):
            remove = int(input("Please enter a valid number: "))
        del departures_date[remove],departures_time[remove],departures_airline[remove], departures_destination[remove]
        
    else:

        while remove not in range (1,len(arrivals_date)):
            remove = int(input("Please enter a valid number: "))
        del arrivals_date[remove],arrivals_time[remove],arrivals_airline[remove], origin[remove]

def arrival_timetable(timetabletype):
        while True:
            i = 0
            while i < len(arrivals_date):
                airlineformat = arrivals_airline[i].ljust(20)
                originformat = origin[i].ljust(20)
                if i == 0:
                    print("|{}\t|{}\t|{}\t|{}\t|{}\t|".format("NO.",arrivals_date[i] + " " * 5, arrivals_time[i],airlineformat, originformat))
                else:
                    print("|{}\t|{}\t|{}\t|{}\t|{}\t|".format(i,arrivals_date[i],arrivals_time[i],airlineformat, originformat))
                i = i + 1

    #Menu Display for admins to add, modify or delete fligts
    #begins with While True so that the menu display loops once one feature is completed   
            if admin == True:
                print("[1]Delete Flight")
                print("[2]Update Flight")
                print("[3]Add Flight")
                print("[4]Exit")
            timetable_menu = input("Choose an option from the Menu: ")
            while timetable_menu not in ("1","2","3","4"):
                timetable_menu = (input("Option invalid, try again"))

            if timetable_menu == "1":
                delete_flight(timetabletype)

            if timetable_menu == "2":
                update_flight(timetabletype)

            if timetable_menu == "3":
                add_flight(timetabletype)

            if timetable_menu == "4":
                break

def departure_timetable(timetabletype):
    while True:
        i = 0
        while i < len(departures_date):
            airlineformat = departures_airline[i].ljust(20)
            destinationformat = departures_destination[i].ljust(20)
            if i == 0:
                print("|{}\t|{}\t|{}\t|{}\t|{}\t|".format("NO.",departures_date[i] + " " * 5, departures_time[i],airlineformat, destinationformat))
            else:
                print("|{}\t|{}\t|{}\t|{}\t|{}\t|".format(i,departures_date[i],departures_time[i],airlineformat, destinationformat))
            i = i + 1
    #Menu Display for admins to add, modify or delete fligts
    #begins with While True so that the mneu display loops once one feature is completed   
        if admin == True:
            print("[1]Delete Flight")
            print("[2]Update Flight")
            print("[3]Add Flight")
            print("[4]Exit")
        timetable_menu = input("Choose an option from the Menu: ")
        while timetable_menu not in ("1","2","3","4"):
            timetable_menu = (input("Option invalid, try again"))

        if timetable_menu == "1":
            delete_flight(timetabletype)

        if timetable_menu == "2":
            update_flight(timetabletype)

        if timetable_menu == "3":
            add_flight(timetabletype)

        if timetable_menu == "4":
            break





#Menu Display 
def menu():
    while True:
        print("[1]Check Flight Timetable")
        print("[2]Purchase Tickets")
        print("[3]Choose Seat")
        print("[4]Exit Program")
        menu_option = (input("Choose Option from Menu"))
        while menu_option not in ("1","2","3","4"):
            menu_option = (input("Option invalid, try again"))

        if menu_option == "1":
            print("[1]Arrivals")
            print("[2]Departures")
            AD_timetable = input("Please select an option: ")
            while AD_timetable not in ("1","2"):
                AD_timetable = input("Please select a valid option: ")
            if AD_timetable == "1":
                timetabletype ="arrivals"
                arrival_timetable(timetabletype)
            if AD_timetable == "2":
                timetabletype = "departures"
                departure_timetable(timetabletype)
        elif menu_option == "2":
            tickets()
        elif menu_option == "3":
            seat()
        elif menu_option == "4":
            break




#Maybe have a text file with username and password and read from it
#registration would write to the file

while True:
    print("[1]Registration")
    print("[2]Login")
    print("[3]Exit the program")
    menu1 = input("Please select an option: ")
    while menu1 not in ("1","2","3"):
        menu1 = input("Please select a valid option: ")

    if menu1 == "1":
        print("=" * 30, "\n\tRegistration\n","=" * 30 )
        Username = input("Username: ")
        Password = input("Password: ")
        Confirm_Password = input("Reenter Passowrd: ")
        while Password != Confirm_Password:
            print("Passwords are not the same. Please retry")
            Password = input("Password: ")
            Confirm_Password = input("Reenter Password: ")

        
    elif menu1 =="2":
        i = 0
        #loops 3 times to allow only 3 unsuccessful attempts
        print("=" * 30, "\n\tLogin\n","=" * 30 )
        while i < 3:    
            username_login = input("What is your username: ")
            password_login = input("What is your password: ")
            if Username == username_login and password_login == Password:
                print("LOGGED IN !!!")
                break
            else:
                print("Access denied! Please try again.")
            i = i + 1
        if i == 3:
            print("Too many attempts for the day. Please try again later.")
        
        menu()
    elif menu1 =="3":
        break




