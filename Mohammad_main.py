import Kitap_transactions
import Member_Transactions

while True:
    print("\nLibrary:")
    print("1. Members")
    print("2. Books")
    print("3. Exit")
    choice = input("Choose: ")
    if choice == '1':
        Member_Transactions.handle_members()
    elif choice == '2':
        Kitap_transactions.handle_books()
    elif choice == '3':
        print("Bye!")
        break
    else:
        print("Wrong.")