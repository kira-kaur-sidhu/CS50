# Meal Time - lement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time

def main():
    time = input("What time is it? ")
    t = float(convert(time))

    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes) / 60
    return hours + minutes

if __name__ == "__main__":
    main()
