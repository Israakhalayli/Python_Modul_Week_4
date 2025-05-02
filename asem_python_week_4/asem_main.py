import asem_book_transactions
import asem_member_transactions
import json

while True:
    print("\n" + "-" * 58)
    print("-        WELCOME TO OUR PUBLIC LIBRARY              -")
    print("-                                                  -")
    print("-     1 - MEMBERSHIP TRANSACTIONS       (Enter 1)  -")
    print("-     2 - BOOK TRANSACTIONS             (Enter 2)  -")
    print("-     3 - EXIT                          (Enter 0)  -")
    print("-" * 58)

    choice = input("Please enter the code of your desired option: ")

    # --- Membership Transactions
    if choice == "1":
        print("\n" + "-" * 58)
        print("- MEMBERS          = 1    =  LEND BOOK        = 5 -")
        print("- ADD MEMBER       = 2    =  RETURN BOOK      = 6 -")
        print("- SEARCH MEMBER    = 3    =  TRACK BOOKS      = 7 -")
        print("- DELETE MEMBER    = 4    =  EXIT             = 0 -")
        print("-" * 58)
        operation = input("Select an operation: ")

        if operation == "1":
            members =  asem_member_transactions.read_members()
            for member in members:
                print(member)

        elif operation == "2":
            name = input("Enter member name: ")
            phone = input("Enter phone number: ")
            address = input("Enter address: ")
            asem_member_transactions.add_member(name, phone, address)

        elif operation == "3":
            search = input("Enter name to search: ")
            asem_member_transactions.search_member(search)

        elif operation == "4":
            delete = input("Enter name to delete: ")
            asem_member_transactions.delete_member(delete)

        elif operation == "5":
            asem_member_transactions.lend_book()

        elif operation == "6":
            asem_member_transactions.return_book()

        elif operation == "7":
            tracking = asem_member_transactions.read_tracking()
            for t in tracking:
                print(t)

        elif operation == "0":
            continue

        else:
            print("Invalid selection in Membership Transactions.")

    # --- Book Transactions
    elif choice == "2":
        print("\n" + "-" * 58)
        print("- BOOKS            = 1                           -")
        print("- ADD BOOK         = 2                           -")
        print("- SEARCH BOOK      = 3                           -")
        print("- DELETE BOOK      = 4        EXIT = 0           -")
        print("-" * 58)
        operation = input("Select an operation: ")

        if operation == "1":
            books = asem_book_transactions.read_books()
            for book in books:
                print(book)

        elif operation == "2":
            title = input("Enter book name: ")
            author = input("Enter author: ")
            publisher = input("Enter publisher: ")
            barcode = input("Enter barcode: ")
            asem_book_transactions.add_book(title, author, publisher, barcode)

        elif operation == "3":
            keyword = input("Enter keyword to search for: ")
            asem_book_transactions.search_book(keyword)

        elif operation == "4":
            barcode = input("Enter barcode to delete: ")
            asem_book_transactions.delete_book(barcode)

        elif operation == "0":
            continue

        else:
            print("Invalid selection in Book Transactions.")

    elif choice == "0":
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid selection. Please try again.")
