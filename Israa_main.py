import Israa_book_transactions
import Israa_membership_transactions

def main():
    while True:
        print('')
        print('Welcome to our puplic library')
        print('1.Book transactions')
        print('2.Membership transactions')
        print('3.Exit')

        choice=input('Please select an option: ')

        if choice=='1':
            Israa_book_transactions.main()
        elif choice=='2':
             Israa_membership_transactions.main()
        elif choice=='3':
            break
        else:
            print('Option is not found. Please try again!')

if __name__ == "__main__":
    main()