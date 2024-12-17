#importing the module
import sys

#this function will be the first to run as soon as the main function executes def initial_phonebook():
rows, cols = int(input("Please enter initial number of contacts:")),5

    #We are collecting the initial number of contacts the user wants to have in the
        # phonebook already. User may also enter 0 if he doesn't wish to enter any
phone_book = []
print(phone_book)
for i in range(rows):
        print("\nEnter contact %d details in the following order (ONLY):" % (i+1))
        print("Note: * indicates mandatory fields")

print("...........................................")
temp = []
for j in range(cols):
    # We have taken the conditions for values of j only for the personalized fields
    # such as name, number, e-mail id,dob,catagory etc
        if j == 0:
                temp.append(str(input("Enter name*:")))
                # We need to check if the user left the name empty as its mentioned that
                # name & number are mandatory fields.
                # So implement a condition to check as below.
                if temp[j] == '' or temp[j] == '':
                        sys.exit(
                                "Name is a mandatory field. Process exiting due to bank field")
                                #This will exit the process if a blank field is encountered.
        if j == 1: 
                temp.append(int(input("Enter number*:")))
                # We do not need to check if user has entered the number because int automatically
                # takes care of it. Int value cannot accept a blank as that counts as a string.
                # So the process automatically exits without us using the sys package.
        if j == 2:
                temp.append(str(input("Enter e-mail address:")))
                #Even if this field is left as blank, None will take the blank's place
                if temp[j] == '' or temp[j] == '':
                        temp[j] = None
        if j == 3:
                temp.append(str(input("Enter date of birth(dd/mm/yy):")))
                # Whatever format the user enters dob in it wont make a difference to the compilier
                # Only while searching the user will have to enter query exactly the same as
                # he entered during the input so as to ensure accurate searches
                if temp[j] == '' or temp[j] == '':
                #Even if this field is left as blank, None will take the blank's place
                        temp[j] = None
        if j== 4:
                temp.append(str(input("Enter catagory(Family/Friends/Work/Others):")))
                if temp[j] == '' or temp[j] == '':
                        temp[j] = None

                phone_book.append(temp)
                # By this step we are appending a list temp into a list phone_book
                # That means phone_book is a 2-D array and temp is a 1-D array
                print(phone_book)
                return phone_book
def menu():
        # We created this simple menu function for
        # code reusability & also an interactive console
        # Menu func will only execute when called
        print("*********************************************")
        print("\t\t\tSMARTPHONE DIRECTORY", flush=False)
        print("*********************************************")
        print("\tYou can now perform the following operations on this phonebook\n")
        print("1. Add a new contact")
        print("2. Remove an existing contact")
        print("3. Delete all contacts")
        print("4. Search for a contact")
        print("5. Display all contacts") 
        print("6. Exit phonebook")
        # Out of the provided 6 choices, user needs to enter any 1 choice among the 6 case
        # We return the entered choice to the calling function wiz main in our
        choice = int(input("Please enter your choice: "))

        return choice
def add_contact(pb):
        # Adding a contact is the easiest because all you need to do is: # append another list of details into the already existing list 
        dip = []
        for i in range(len(pb[0])):
                if i == 0:
                        dip.append(str(input("Enter name: ")))
                if i == 1:
                        dip.append(int(input("Enter number: ")))
                if i == 2:
                        dip.append(str(input("Enter e-mail address: ")))
                if i == 3:
                        dip.append(str(input("Enter date of birth (dd/mm/yy):")))
                if i == 4:
                        dip.append(str(input("Enter category(Family/Friends/Work/Others): "))) 
                        pb.append(dip)
        # And once you modify the list, you return it to the calling function wiz main, here.
                return pb
def remove_existing(pb):
        #This function is to remove a contact's details from existing phonebook
        query= str(
                input("Please enter the name of the contact you wish to remove: "))
        # We'll collect name of the contact and search if it exists in our phonebook
        temp = 0
        # temp is a checking variable here. We assigned a value to temp.
        for i in range(len(pb)):
                if query == pb[i][0]:
                        temp += 1
                        # Temp will be incremented & it won't be anymore in this function's scope
                        print (pb.pop(i))
                        # The pop function removes entry at index i print("This query has now been removed")
                        # printing a confirmation message after removal.