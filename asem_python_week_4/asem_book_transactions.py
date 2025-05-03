import json
import os

BOOK_FILE = "kitap.json"


def read_books():
    if os.path.exists(BOOK_FILE):
        with open(BOOK_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        return []


def save_books(book_list):
    with open(BOOK_FILE, "w", encoding="utf-8") as file:
        json.dump(book_list, file, ensure_ascii=False, indent=4)


def add_book(title, author, publisher, barcode):
    books = read_books()


    for book in books:
        if book["Barkod"] == barcode:
            print("A book with this barcode already exists.")
            return

    new_book = {
        "Barkod": barcode,
        "Kitap_Adi": title,
        "Yayinevi": publisher,
        "Yazar": author
    }

    books.append(new_book)
    save_books(books)
    print("Book added successfully.")


def delete_book(barcode_to_delete):
    books = read_books()
    updated_books = [book for book in books if book["Barkod"] != barcode_to_delete]

    if len(books) == len(updated_books):
        print("Book not found.")
    else:
        save_books(updated_books)
        print("Book deleted.")


def search_book(search_term):
    books = read_books()
    found = False
    for book in books:
        if search_term.lower() in book["Kitap_Adi"].lower():
            print(f"\n Found Book: {book}")
            found = True
    if not found:
        print("No match found.")


if __name__ == "__main__":
    print("Book transactions module loaded.")
