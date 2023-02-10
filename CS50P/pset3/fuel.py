# Fuel Gauge - plement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. 
# And if 99% or more remains, output F instead to indicate that the tank is essentially full.

while True:
    try:
        fraction = input("Fraction: ").split("/")
        (x,y) = fraction
        if not x.isdigit() or y.isdigit():
            pass
        x = int(x)
        y = int(y)
        if x > y or y == 0:
            pass

        else:
            percentage = (x / y) * 100
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(round(percentage), "%", sep="")
            break
        
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
