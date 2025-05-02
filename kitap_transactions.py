

import json
import os

BOOK_FILE = 'books.json'

def read_books():
    try:
        with open(BOOK_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error reading books file.")
        return []

def save_books(books):
    with open(BOOK_FILE, 'w', encoding='utf-8') as f:
        json.dump(books, f, indent=4, ensure_ascii=False)

def add_book():
    books = read_books()
    barcode = input("Enter Book Barcode: ")
    title = input("Enter Book Title: ")
    author = input("Enter Book Author: ")
    publisher = input("Enter Book Publisher: ")
    price = input("Enter Book Price: ")
    books.append({"Barcode": barcode, "Title": title, "Author": author, "Publisher": publisher, "Price": price})
    save_books(books)
    print("Book added.")

def delete_book():
    barcode_to_delete = input("Enter Barcode of book to delete: ")
    books = read_books()
    updated_books = [book for book in books if book['Barcode'] != barcode_to_delete]
    if len(updated_books) < len(books):
        save_books(updated_books)
        print("Book deleted.")
    else:
        print("Book not found.")

def search_books():
    search_term = input("Enter search term: ")
    books = read_books()
    results = [book for book in books if
               search_term.lower() in book['Barcode'].lower() or
               search_term.lower() in book['Title'].lower() or
               search_term.lower() in book['Author'].lower() or
               search_term.lower() in book['Publisher'].lower()]
    if results:
        print("\nSearch Results:")
        for book in results:
            print(f"Barcode: {book['Barcode']}, Title: {book['Title']}, Author: {book['Author']}, Publisher: {book['Publisher']}, Price: {book['Price']}")
    else:
        print("Book not found.")

def list_books():
    books = read_books()
    if books:
        print("\nAll Books:")
        for book in books:
            print(f"Barcode: {book['Barcode']}, Title: {book['Title']}, Author: {book['Author']}, Publisher: {book['Publisher']}, Price: {book['Price']}")
    else:
        print("No books in the library.")

def handle_books():
    while True:
        print("\nBook Actions:")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Search Books")
        print("4. List Books")
        print("9. Back")
        choice = input("Choose: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            delete_book()
        elif choice == '3':
            search_books()
        elif choice == '4':
            list_books()
        elif choice == '9':
            break
        else:
            print("Wrong choice.")