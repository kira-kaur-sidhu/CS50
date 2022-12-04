#Tip Calculator - convert dollar amount and percentage from str to float

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Remove the $ sign and convert to float
    d = d.strip("$")
    return float(d)

def percent_to_float(p):
    # Remove the % sign and convert to float
    p = int(p.strip("%"))
    pl = p / 100
    return float(pl)


main()
