
import csv
import random
import string


#Main Function:
#1- Users can store password with its associated username and website
#2- users can lookup passwords either by entering the username or website (if website is enetered then it returns all the usernames and the passwordsm )
def file(files):
    global target
    target=files
    with open(f"/home/hysam/Desktop/NiceBandit/{files}.csv") as file:
        rows=csv.reader(file)
        global usernames
        usernames=next(rows)
        global passwords
        passwords=next (rows)
        global websites
        websites=next(rows)
    return files

def store_usernmes_password_weblink(username, password, weblink):
    
    with open(f"/home/hysam/Desktop/NiceBandit/{target}.csv", "w") as file:
        
        usernames.append(username)
        passwords.append(password)
        websites.append(weblink)





        csv_writer=csv.writer(file)
        csv_writer.writerow (usernames)
        csv_writer.writerow (passwords)
        csv_writer.writerow(websites)


def get_indexes(lst, query):
    indexes = []
    for i, element in enumerate(lst):
        if element == query:
            indexes.append(i)
    return indexes

def display_results(index):
    if len(index)==0:
        print("DOES NOT EXIST!")
    count=0
    for items in index:
        count+=1
        foundUsername=usernames[items]
        foundPassword=passwords[items]
        foundWebsite=websites[items]
        print("_________________________________________________________________")
        print(f"{count}.  -{foundUsername}-,    -{foundPassword}-,   -{foundWebsite}-")





def generate_password():
  # Generate a random 10-character password
  password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=10))
  
  # Check if the password has consecutive numbers and regenerate it if it does
  while any(str(i) in password[i:i+3] for i in range(len(password)-2)):
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=10))
  
  return password



def tidyUp():
    x=0
    while x==0:

        print("""
        Greetings!
        1-Search Passwords
        2-Store New Password
        3-Change passwords
        4-V1iew all 
        """)
        user_input=input("")
        if user_input=="1":
            one()
        elif user_input=="2":
            two()
        elif user_input=="3":
            three()
        elif user_input=="4":
            four()
        elif user_input=="exit":
            x=x+1




def one():
    typeos=""
    user_input1=input("""
    Search by:
    1-username
    2-website 
    """)

    userinput2=input("Enter search query:   ")
    if user_input1=="1":
        typeos=usernames
    else:
        typeos=websites
    display_results(get_indexes(typeos,userinput2))






def two():
    input1=input("Enter Username:   ")
    input2=input("Enter Password:   ")
    input3=input("Enter website:    ")
    store_usernmes_password_weblink(input1, input2, input3)


def three():
    lst=""
    query=""
    inout1=input("""
    1- To search by website 
    2- to search by username
    """)
    if inout1=="1":
        lst=websites
    elif inout1=="2":
        lst=usernames
    query=input("enter search query:    ")





    indexes = []
    for i, element in enumerate(lst):
        if element == query:
            indexes.append(i)
    


    if len(indexes)==0:
        print("DOES NOT EXIST!")
    count=0
    for items in indexes:
        count+=1
        foundUsername=usernames[items]
        foundPassword=passwords[items]
        foundWebsite=websites[items]
        print("_________________________________________________________________")
        print(f"{count}.  -{foundUsername}-,    -{foundPassword}-,   -{foundWebsite}-")


    index_to_change=int(input("enter rownumber to change"))
    index_to_change=(index_to_change)-1
    targetindex=indexes[index_to_change]
    change=input("""
    what would you like tii change?
    1-password
    2-username   
    """)
    if change=="1":
        changelist=passwords
    elif change=="2":
        changelist=usernames
    replacementitem=input("enter replacement item:  ")
    changelist[targetindex]=replacementitem
    store_usernmes_password_weblink(None, None, None)



def four():
    l = len(usernames)
    count = 0
    
    for i in range(0, l):
        print(f"{count:<5}{usernames[i]:<15}{passwords[i]:<15}{websites[i]:<15}")
        count += 1




#(display_results(get_indexes(usernames, "username2")))
#print (usernames[1])
#print(generate_password())




    
        