import json
import Zaman

MEMBER_FILE = 'members.json'

def load_members():
    try: return json.load(open(MEMBER_FILE, 'r'))
    except: return []

def save_members(members):
    json.dump(members, open(MEMBER_FILE, 'w'), indent=4)

def add_member():
    ms = load_members(); i = input("ID: "); n = input("Name: "); ms.append({'Id': i, 'Name': n, 'Borrowed': []}); save_members(ms); print("Added.")

def del_member():
    ms = [m for m in load_members() if m['Id'] != input("ID to delete: ")]; save_members(ms); print("Deleted.")

def show_member():
    for m in load_members():
        if m['Id'] == input("ID to show: "): print(m); return
    print("Not found.")

def borrow_book():
    mid = input("Member ID: "); bid = input("Book ID: "); ms = load_members()
    for m in ms:
        if m['Id'] == mid: m['Borrowed'].append({'BookId': bid, 'Date': Zaman.get_current_datetime_str(), 'Due': Zaman.get_due_date()}); save_members(ms); print("Borrowed."); return
    print("Member not found.")

def return_book():
    mid = input("Member ID: "); bid = input("Book ID to return: "); ms = load_members()
    for m in ms:
        if m['Id'] == mid and any(b['BookId'] == bid for b in m['Borrowed']):
            m['Borrowed'] = [b for b in m['Borrowed'] if b['BookId'] != bid]; save_members(ms); print("Returned."); return
    print("Member or book not found.")

def handle_members():
    while True:
        print("\nMembers:")
        print("1. Add")
        print("2. Delete")
        print("3. Show")
        print("4. Borrow")
        print("5. Return")
        print("9. Back")
        c = input("Choose: ")
        if c == '1': add_member()
        elif c == '2': del_member()
        elif c == '3': show_member()
        elif c == '4': borrow_book()
        elif c == '5': return_book()
        elif c == '9': break
        else: print("Wrong.")