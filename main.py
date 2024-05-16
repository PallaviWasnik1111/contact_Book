#main.py
from contact import Contact
from contact_book import ContactBook
def main():
    contact_book=ContactBook()
    while True:
        print("\n contact book menu")
        print("1. Add contact")
        print("2 Display all contacts")
        print("3. search contact")
        print("4. exit")
        choice=input("enter your choice(1/2/3/4):")
        if choice=='1':
            name=input("enter name")
            phone=input("enter phone number")
            email=input("enter email")
            new_contact=Contact(name,phone,email)
            contact_book.add_contact(new_contact)
            print("contact add succesfully!")
        elif choice=='2':
            print("\n All contacts")
            contact_book.display_all_contacts()
        elif choice=='3':
            name_to_search=input("enter name to serch")
            found_contact=contact_book.search_contact(name_to_search)
            if found_contact:
                print("\n contact found")
                found_contact.display_contact()
            else:
                print("contact not found.")
        elif choice=='4':
            print("exiting contactbook.Goodbye")
            break
        else:
            print("invalid choice.please enter a valid choice")
main()

