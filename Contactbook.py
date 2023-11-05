Contact ={}

def View_contact():
    print ("Name\tContact number\tEmail\tAddress")
    
    for key in Contact:
        print("{}\t\t{}".format(key,Contact.get(key)))


while True:
    choice = int(input(" 1. Add new contact \n 2. Search contact \n 3. View contact \n 4. Update contact \n 5. Delete contact \n Enter your choice " ))
    if choice ==1:
        name= input("Enter the contact name:")
        phone= input("Enter the mobile number:")
        email= input("Enter the email:")
        address= input("Enter the address:")
        Contact[name] =phone, email, address
        
        print("Print successfully.")
    elif choice == 2:
        search_name = input("Enter the contact name")
        if search_name in Contact:
            print (search_name,"s Contact number is ", Contact[search_name])
        else:
            print ("The name is not found in contact book")
    elif choice == 3: 
        if not Contact:
            print("Empty contact book")
        else:
            View_contact()
    elif choice == 4:
        update_contact = input ("Enter the contact to be updated")
        if update_contact in Contact:
            phone = input("Enter mobile no")
            Contact[update_contact]=phone
            print("contact updated")
            View_contact()
        else:
            print("The name is not found in contact book")
    elif choice == 5:
        del_contact = input("Enter the contact to be deleted")
        if del_contact in Contact:
              Contact.pop(del_contact)
        View_contact()
    else:
        print("The name is not found in contact book")

