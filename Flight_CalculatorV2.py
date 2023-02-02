from Flight_Calculator_Functions import *

def menu():
    print("Choose an option, Conversions, Calculators, STD, or Stop")
    userInput = input()
    if userInput == "Conversions":
        conversions()
        menu()
    elif userInput == "Calculators":
        calculators()
        menu()
    elif userInput == "STD":
        STD()
        menu()
    elif userInput == "Stop":
        print("Stopping")
        quit()
    else: 
        print("Please enter a valid option.")
        menu()

def conversions():
    print("Choose an option, Temperature, Speed, or Distance")
    userInput = input()
    if userInput == "Temperature" or "Temp":
        temperature()
        menu()
    elif userInput == "Speed":
        speed()
        menu()
    elif userInput == "Distance":
        conv_distance()
        menu()
    else:
        print("Please enter a valid option.")

def temperature():
    print("Choose an option, Fahrenheit to Celsius or Celsius to Fahrenheit")
    userInput = input()
    if userInput == "Fahrenheit to Celsius":
        f_to_c()
        menu()
    elif userInput == "Celsius to Fahrenheit":
        c_to_f()
        menu()
    else:
        print("Please enter a valid option.")

def speed():
    print("Choose an option, Knots to MPH or MPH to Knots")
    userInput = input()
    if userInput == "Knots to MPH":
        knot_to_mph()
        menu()
    elif userInput == "MPH to Knots":
        mph_to_knot()
        menu()
    else:
        print("Please enter a valid option.")

def conv_distance():
    print("Choose an option, NM to Mile or Mile to NM")
    userInput = input()
    if userInput == "NM to Mile":
        nm_to_mile()
        menu()
    elif userInput == "Mile to NM":
        mile_to_nm()
        menu()
    else:
        print("Please enter a valid option.")

def calculators():
    print("Choose an option, Top of Decent or Altitude Density")
    userInput = input()
    if userInput == "Top of Decent" or "TOD":
        tod()
        menu()
    elif userInput == "Altitude Density":
        altitude_density()
        menu()
    else:
        print("Please enter a valid option.")

def STD():
    print("Choose an option, Speed, Time, or Distance")
    userInput = input()
    if userInput == "Speed":
        speed()
        menu()
    elif userInput == "Time":
        time()
        menu()
    elif userInput == "Distance":
        distance()
        menu()
    else:
        print("Please enter a valid option.")

if __name__ == "__main__":
    menu()