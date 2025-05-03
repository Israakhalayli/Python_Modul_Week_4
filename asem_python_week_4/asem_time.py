from datetime import datetime, timedelta

def get_dates():
    now = datetime.now()
    return_date = now + timedelta(days=14)

    formatted_now = now.strftime("%d-%m-%Y, %H:%M")
    formatted_return = return_date.strftime("%d-%m-%Y")

    return {
        "borrow_date": formatted_now,
        "return_date": formatted_return
    }


if __name__ == "__main__":
    result = get_dates()
    print("Borrow Date:", result["borrow_date"])
    print("Return Date:", result["return_date"])
