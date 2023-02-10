# Outdated - mplement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list.
# Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again.

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:

    date = input("Date: ").strip()

    try:
        date_amend = date.replace(" ", "/").replace(",", "")
        (m, d, y) = date_amend.split("/")

        if int(d) > 31:
            pass
        elif m in months:
            if "," in date:
                print(int(y), f"{int(list(months).index(m)) + 1:02}", f"{int(d):02}", sep="-")
                break
            else:
                pass
        else:
            if int(m) > 12:
                pass
            else:
                print(int(y), f"{int(m):02}", f"{int(d):02}", sep="-")
                break

    except ValueError:
        pass
