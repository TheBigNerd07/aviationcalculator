import math

def tod():
    #Top of Decent Calculator
    current_altitude_input = int(input('Current Altitude '))
    airport_elevation_input = int(input('Airport Elevation '))
    tod_answer = (current_altitude_input - airport_elevation_input) * 3 / 1000
    print(str(tod_answer) + " Nautical Miles")

def f_to_c():
    #Temp Fahrenheit to Celsius
    fahrenheit_input = int(input('Temp in Fahrenheit '))
    celsius_answer = int(round((fahrenheit_input - 32) * 5 / 9))
    print(str(celsius_answer) + " Celsius")

def c_to_f():
    #Temp Celsius to Fahrenheit
    celsius_input = int(input('Temp in Celsius '))
    fahrenheit_answer = int(round((celsius_input * 9/5) + 32))
    print(str(fahrenheit_answer) + " Fahreheit")

def knot_to_mph():
    #Knot to MPH
    knot_input = int(input('Knots '))
    mph_answer = float(knot_input * 1.15078)
    print(str(mph_answer) + " MPH")

def mph_to_knot():
    #MPH to Knot
    mph_input = int(input('MPH '))
    knot_answer = float(mph_input / 1.15078)
    print(str(knot_answer) + " Knots")

def nm_to_mile():
    #NM to Mile
    nm_input = int(input('Nautical Mile '))
    mile_answer = float(nm_input * 1.15078)
    print(str(mile_answer) + " Miles")

def mile_to_nm():
    #Mile to NM
    mile_input = int(input('Mile '))
    nm_answer = float(mile_input / 1.15078)
    print(str(nm_answer) + " Nautical Miles")

def altitude_density():
    #Altitude Density "IN THE WORKS"
    current_altitude_input = int(input('Current Altitude '))
    current_barometic_pressure_input = float(input('Current Barometic Pressure '))
    current_pressure_altitude = float(((29.92 - current_barometic_pressure_input) * 1000) + current_altitude_input)
    current_oat_celsius_input = int(input('Current Out Side Air Temp in Celsius '))
    current_isa_temp = 15 - ((current_altitude_input/1000) * 2)
    current_isa_temp_deviation = current_oat_celsius_input - current_isa_temp
    current_density_altitude = float(current_pressure_altitude + (120 * (current_oat_celsius_input - current_isa_temp_deviation)))
    print(str(current_density_altitude) + " Feet")

def std_distance():
    speed_input = int(input('Speed '))
    time_input = int(input('Time '))
    distance_answer = speed_input * time_input
    print(str(distance_answer) + " Units")

def std_speed():
    distance_input = int(input('Distance '))
    time_input = int(input('Time '))
    speed_answer = distance_input / time_input
    print(str(speed_answer) + " Units")

def std_time():
    distance_input = int(input('Distance '))
    speed_input = int(input('Speed '))
    time_answer = distance_input / speed_input
    print(str(time_answer) + " Units")