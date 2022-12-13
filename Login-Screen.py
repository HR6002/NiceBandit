import csv
import re
import time

with open("/home/hysam/Desktop/NiceBandit/Muser.csv") as csvfile:
    rows=csv.reader(csvfile)
    masterusernames= next(rows)
    masterpasswords=next(rows)


            



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
    
    return True



def login():
    while True:
        usrname=input("Enter username: ")
        if usrname in masterusernames:
            indx=masterusernames.index(usrname)
            psswrdd=input("enter password: ")
            if psswrdd == masterpasswords[indx]:
                print(f"\nWelcome {usrname}!\n")
                return usrname
            elif psswrdd=="exit":
                break
            else:
                print("Wrong password 4 Attempts remaining")
                for i in range (0,4):
                    psswrdd=input("enter password: ")
                    if psswrdd == masterpasswords[indx]:
                        print(f"\nWelcome {usrname}!\n")
                        return usrname
                    elif psswrdd =="exit":
                        return False
                for i in range(0,50):
                    print("too many Attempts!")
                    time.sleep(0.5)
        elif usrname=="exit":
            break
        
            
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
                    csv_file=open((f"{usrname}.csv"), "w")
                    csv_file.close()
                    break
                elif paswrd=="exit":
                    break
                else:
                    print("\npassword must be 8 charecters long or more, it must have a combination \nof lower case and uppercase charecters including special charecters\n")

        else:
            print("username already exists!")
       






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



login_screen()