#Seth Jones
#Period 1/2
#01/06/2020

import datetime

def get_verified_integer():
    while True:
        userMonth = input("Please enter the month(1-12): ")
        try:
            month = int(userMonth)
            if month >= 1 and month <= 12:
                break
            else:
                print("Please enter a number from 1 to 12.\n")
        except ValueError:
            print("Please enter a valid number.\n")
            continue
        
    while True:
        userDay = input("Please enter the day(1-31): ")
        try:
            day = int(userDay)
            if day >= 1 and day <= 31:
                break
            else:
                print("Please enter a number from 1 to 31.\n")
        except ValueError:
            print("Please enter a valid number.\n")
            continue
        
    while True:
        userYear = input("Please enter the year(2000-2030): ")
        try:
            year = int(userYear)
            if year >= 2000 and year <= 2030:
                break
            else:
                print("Please enter a number from 2000 to 2030.\n")
        except ValueError:
            print("Please enter a valid number.\n")
            continue
    return year, month, day

year,month,day = get_verified_integer()
today = datetime.date(year,month,day)
print("\nThat day is a " + today.strftime("%A"))
    
    
    
