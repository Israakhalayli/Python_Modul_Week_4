import json
import os


# books_file='books.json'
books_file='Israa_kitap.json'

def load_books():
    if os.path.exists(books_file):
        with open(books_file,'r') as file:
            try:
                data = json.load(file)
                return data if isinstance(data, list) else []
            except json.JSONDecodeError:
                return []


def save_books(books):
    with open(books_file,'w') as file:
        json.dump(books,file,indent=4)

def add_book(title, author, year,barcode):
    books = load_books()
    if books is None:
        books = []  # Ensure it's always a list
    books.append({"title": title, "author": author, "year": year,'Barcode':barcode})
    save_books(books)

def delete_book(title):
    books = load_books()
    book_exists = any( book.get('title' ) == title for book in books)
    if book_exists:
        books = [book for book in books if  book.get('title' ) != title]
        save_books(books)
        print(f'Book "{title}" has been deleted successfully.')
    else:
        print(f'Book "{title}" not found.')

def search_book(title):
    books=load_books()
    return next((book for book in books if book.get('title' )== title),None)

def list_books():
    books = load_books()
    if books:
        for book in books:
            print(f"Title: { book.get('Title' )}  -  Author: {book.get('Author' )}")
    else:
        print("No books available.")

def main():
    while True:
        print('Welcome in Book transactions')
        print('1.add book')
        print('2.Search book')
        print('3.delete book ')
        print('4.List book')
        print('5.Exit')
        choice=input('Please select an option: ')

        if choice=='1':
            title=input('Enter book title: ')
            author=input('Enter book author: ')
            year=input('Enter book year: ')
            barcode=input('Enter book barcode: ')
            add_book(title,author,year,barcode)
            print("Book added successfully!")
        elif choice=='2':
            title=input('Enter book title to search: ')
            book=search_book(title)
            if book:
                print(f"Book found! Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
            else:
                print("Book not found.")
        elif choice=='3':
            title=input('Enter book title to delete : ')
            delete_book(title)
        elif choice=='4':
            list_books()
        elif choice=='5':
            break
        else:
            print('Invalid choise , please try again!')
