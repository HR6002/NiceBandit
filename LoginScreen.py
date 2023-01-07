import csv
import re
import time
from MainPassword import*

with open("/home/hysam/Desktop/NiceBandit/Muser.csv") as csvfile:
    rows=csv.reader(csvfile)
    masterusernames= next(rows)
    masterpasswords=next(rows)





def store_10k():
    with open ("/home/hysam/Desktop/NiceBandit/10kasswords.txt", "r") as file :
        lines= file.readlines()

    return lines







def binary_search(items, target):

    min = 0
    max = len(items) - 1


    while min <= max:

        mid = (min + max) // 2


        if target.lower() in items[mid].lower():
            return True


        elif target < items[mid]:
            max = mid - 1


        else:
            min = mid + 1


    return False


def check_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'\d', password):
        return False
    
    if not re.search(r'[A-Z]', password):
        return False
    
    if not re.search(r'[a-z]', password):
        return False
    
    if not re.search(r'[^\w]', password):
        return False
    if binary_search(store_10k(), format_password(password))==True:
        return False
    if check_consequitivenumbers(password)==True :
        return False

    
    return True



def login():
    
        usrname=input("Enter username: ")
        if usrname in masterusernames:
            indx=masterusernames.index(usrname)
            psswrdd=input("enter password: ")
            if psswrdd == masterpasswords[indx]:
                print(f"\nWelcome {usrname}!\n")
                file(f"{usrname}")
                tidyUp()
                


            else:
                print("Wrong password 4 Attempts remaining")
                for i in range (0,4):
                    psswrdd=input("enter password: ")
                    if psswrdd == masterpasswords[indx]:
                        print(f"\nWelcome {usrname}!\n")
                        file(f"{usrname}")
                        tidyUp()
                        
                        
                    elif psswrdd =="exit":
                        return False
                for i in range(0,50):
                    print("too many Attempts!")
                    time.sleep(0.5)

        
            
        else:
            print("wrong username!")
            







def register():
    
    while True:
        usrname=input("Enter A username: \n")
        if usrname =="exit":
            break
        elif usrname not in masterusernames:
            while True:
                paswrd=input("enter a password: \n")
                if check_password(paswrd):
                    masterusernames.append(usrname)
                    masterpasswords.append(paswrd)
                    csv_file=open((f"/home/hysam/Desktop/NiceBandit/{usrname}.csv"), "w") 
                    with open(f"/home/hysam/Desktop/NiceBandit/{usrname}.csv", "w") as bob:
                        csv_writer=csv.writer(bob)
                        csv_writer.writerow (["-USERNAMES-"])
                        csv_writer.writerow (["-PASSWORDS-"])
                        csv_writer.writerow(["-WEBSITES-"])
                        csv_file.close()
                        save_passwords()
                        break
                    
                elif paswrd=="exit":                    
                    break
                else:
                    print("\npassword must be 8 charecters long or more, it must have a combination \nof lower case and uppercase charecters including special charecters\n and it must not be too  common ")

        else:
            print("username already exists!")
       


def format_password(password):
    return re.sub(r'[^a-zA-Z]', '', password)



def check_consequitivenumbers(numericpasswrd): 
    num = re.findall(r'\d+', numericpasswrd)
    
    counter = 0
    

    for numbers in num:
        length = len(numbers)
        if length >= 3:
            for i in range(length-1):
                first_digit = numbers[i]
                second_digit = numbers[i + 1]
                if int(second_digit) - int(first_digit) == 1 :
                    counter += 1
                elif int(second_digit)-int(first_digit)==0:
                    counter += 1
    print (counter)
    if counter >= 2:
        return True





def save_passwords():
    with open("/home/hysam/Desktop/NiceBandit/Muser.csv", "w") as file:
        csv_writer=csv.writer(file)
        #csv_writer.writerow([])
        csv_writer.writerow(masterusernames)
        csv_writer.writerow(masterpasswords)



def login_screen():
    while True:
        user=input("1- Login\n2-Register\n")
        if user=="1":
            login()
        elif user=="2":
            register()
            save_passwords()
        else:
            print("invalid Option")




