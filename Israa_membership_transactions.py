import json
import os 
from datetime import datetime,timedelta
import Israa_book_transactions

members_file='members.json'
tracking_file='tracking.json'

def load_members():
    if os.path.exists(members_file):
        with open(members_file,'r') as file:
            try:
                data = json.load(file)
                return data if isinstance(data, list) else []
            except json.JSONDecodeError:
                return []
    return []

def save_members(members):
    with open(members_file,'w') as file:
       json.dump(members, file, indent=4)


def add_member(name):
    members=load_members()
    members.append({'name':name})
    print('Added member is succesfully')
    save_members(members)

def delete_member(name):
    members = load_members()
    member_exists = any(member["name"] == name for member in members)
    if member_exists:
        members = [member for member in members if member["name"] != name]
        save_members(members)
        print(f'Member "{name}" has been deleted successfully.')
    else:
        print(f'Member "{name}" not found.')

def check_member(name):
    members = load_members()
    if any(member["name"] == name for member in members):
        print(f'Member "{name}" exists.')
    else:
        print(f'Member "{name}" not found.')

def save_tracking(tracking_data):
    existing_tracking = []
    if os.path.exists(tracking_file):
        with open(tracking_file, "r") as file:
            try:
                existing_tracking = json.load(file)
                if not isinstance(existing_tracking, list): 
                    existing_tracking = []
            except json.JSONDecodeError:
                existing_tracking = []
    existing_tracking.append(tracking_data)
    with open(tracking_file, "w") as file:  
        json.dump(existing_tracking, file, indent=4)

def lend_book(member_name, book_title):
    books = Israa_book_transactions.load_books()
    members = load_members()
    if not any(member['name'] == member_name for member in members):
        return "Member not found."
    book = next((book for book in books if book.get("title") == book_title), None)
    if not book:
        return "Book not found."



    # Calculate loan and return dates
    loan_date = datetime.now()
    return_date = loan_date + timedelta(weeks=2)

    tracking_data = {
        "member": member_name,
        "book": book_title,
        "loan_date": loan_date.strftime("%d-%m-%Y"),
        "return_date": return_date.strftime("%d-%m-%Y")
    }

    # Save tracking data
    save_tracking(tracking_data)
    books = [book for book in books if book.get("title") != book_title]
    Israa_book_transactions.save_books(books)

    print(f'Book "{book_title}" loaned to "{member_name}". Return by {return_date.strftime("%d-%m-%Y")}')


tracking_file = "taksi.json"
books_file = "Israa_kitap.json"

def load_json(filename):
    """ Load JSON data safely from a file """
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                data = json.load(file)
                return data if isinstance(data, list) else []
            except json.JSONDecodeError:
                return []
    return []

def save_json(filename, data):
    """ Save data to JSON file """
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def return_book(member_name, book_title):
    tracking = load_json(tracking_file)
    books = load_json(books_file)
    # Find the loan record
    loan_record = next((entry for entry in tracking if entry["member"] == member_name and entry["book"] == book_title), None)
    if not loan_record:
        print(f'No loan record found for "{book_title}" under "{member_name}".')
        return
    # Remove from tracking records
    tracking = [entry for entry in tracking if not (entry["member"] == member_name and entry["book"] == book_title)]
    save_json(tracking_file, tracking)
    # Add book back to Israa_kitap.json
    books.append({"title": book_title})
    save_json(books_file, books)
    print(f'Book "{book_title}" has been successfully returned by "{member_name}".')


def main():
    while True:
        print("\nMembership Transactions")
        print("1. Add Member")
        print("2. Lend Book")
        print('3.Delete Member')
        print("4. Check Member")
        print('5.Return Book')
        print('6.Exit')

        choice = input("Please select an option: ")

        if choice == '1':
            name = input("Enter member name: ")
            add_member(name)
        elif choice == '2':
            member_name = input("Enter member name: ")
            book_title = input("Enter book title to lend: ")
            result=lend_book(member_name, book_title)
            print(result)
        elif choice=='3':
            name=input('Enter member name to delete: ')
            delete_member(name)
        elif choice =='4':
            name=input('Enter member name to check: ')
            check_member(name)
        elif choice=='5':
            member_name = input("Enter member name: ")
            book_title = input("Enter book title to return: ")
            return_book(member_name, book_title)
        elif choice == '6':
            print("Exiting membership transactions.")
            break
        else:
            print("Invalid choice, please try again!")