from datetime import datetime,timedelta
def get_lending_period():

    loan_date = datetime.now()
    return_date = loan_date + timedelta(weeks=2)
    return loan_date.strftime("%Y-%m-%d"), return_date.strftime("%Y-%m-%d")

get_lending_period()