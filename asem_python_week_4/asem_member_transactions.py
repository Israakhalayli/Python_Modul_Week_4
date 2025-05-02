import json
import os
from datetime import datetime, timedelta


MEMBER_FILE = 'member.json'
TRACK_FILE = 'tracking.json'
BOOK_FILE = 'kitap.json'


def read_members():
    if not os.path.exists(MEMBER_FILE):
        return []
    with open(MEMBER_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)


def update_members(member_list):
    with open(MEMBER_FILE, 'w', encoding='utf-8') as file:
        json.dump(member_list, file, ensure_ascii=False, indent=4)


def add_member(name, phone, address):
    members = read_members()
    new_id = 1
    if members:
        new_id = max(member["id"] for member in members) + 1
    new_member = {
        "id": new_id,
        "name": name,
        "phone": phone,
        "address": address
    }
    members.append(new_member)
    update_members(members)
    print("Member added successfully.")


def search_member(query):
    members = read_members()
    for member in members:
        if query.lower() in member["name"].lower():
            print("Member found:", member)
            return member
    print("Member not found.")
    return None


def delete_member(name_to_delete):
    members = read_members()
    updated_list = [member for member in members if member["name"].lower() != name_to_delete.lower()]
    update_members(updated_list)
    print("Member deleted if existed.")


import json

def read_tracking():
    try:
        with open("tracking.json", "r", encoding="utf-8", errors="replace") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []



def save_tracking(data):
    tracking = read_tracking()
    tracking.append(data)
    with open(TRACK_FILE, 'w',encoding="utf-8") as file:
        json.dump(tracking, file, ensure_ascii=False, indent=4)


def lend_book():
    if not os.path.exists(BOOK_FILE):
        print("Book file not found.")
        return

    with open(BOOK_FILE, 'r',encoding="utf-8") as file:
        books = json.load(file)

    members = read_members()

    barcode = input("Enter the barcode of the book to lend: ")
    member_name = input("Enter member name: ")

    member = next((m for m in members if m["name"].lower() == member_name.lower()), None)
    if not member:
        print("Member not found.")
        return

    for i, book in enumerate(books):
        if str(book["Barkod"]) == barcode:
            now = datetime.now()
            return_date = now + timedelta(days=14)
            loan_entry = {
                "barcode": barcode,
                "member_name": member["name"],
                "phone": member["phone"],
                "address": member["address"],
                "book_title": book["Kitap_Adi"],
                "author": book["Yazar"],
                "publisher": book["Yayinevi"],
                "price": book.get("Fiyat", "N/A"),
                "language": book.get("Dil", "N/A"),
                "loan_date": now.strftime("%d-%m-%Y, %H:%M"),
                "return_date": return_date.strftime("%d-%m-%Y")
            }
            save_tracking(loan_entry)
            books.pop(i)
            with open(BOOK_FILE, 'w', encoding='utf-8') as f:
                json.dump(books, f, ensure_ascii=False, indent=4)
            print("Book has been lent successfully.")
            return

    print("Book not found.")

# Return a book
def return_book():
    books = []
    if os.path.exists(BOOK_FILE):
        with open(BOOK_FILE, 'r', encoding='utf-8') as file:
            books = json.load(file)

    title = input("Enter the title of the book to return: ")
    author = input("Enter author: ")
    publisher = input("Enter publisher: ")
    barcode = input("Enter barcode: ")

    returned_book = {
        "Kitap_Adi": title,
        "Yazar": author,
        "Yayinevi": publisher,
        "Barkod": barcode
    }
    books.append(returned_book)
    with open(BOOK_FILE, 'w', encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False, indent=4)

    print("Book returned and added back to the library.")
