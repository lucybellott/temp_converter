temp_value = int(input("What's the temperature value that you would like to convert?\n"))
temp_unit = input("What unit is this temperature in?\nFor Fahrenheit choose (f)\nFor Celsius choose (C)\nFor Kelvin choose (K)\n")

def convert_temp(temp_value, temp_unit):
    if temp_unit == "f":
        Celsius = ((temp_value - 32) / 1.8)
        print(f"Farenheit temp: {temp_value}\nto Celsius: {Celsius}")
        Kelvin = ((temp_value + 459.67) / 1.8)
        print(f"Farenheit temp: {temp_value}\nto Kelvin: {Kelvin}")
    elif temp_unit == "C":
        Farenheit = ((temp_value * 1.8) + 32)
        print(f"Celsius temp: {temp_value}\nto Farenheit: {Farenheit}")
        Kelvin = (temp_value - 273.15)
        print (f"Celsius temp: {temp_value}\nto Kelvin: {Kelvin}")
    elif temp_unit == "K":
        Fahrenheit = ((temp_value * 1.8) - 459.67)
        print(f"Kelvin temp: {temp_value}\nto Farenheit: {Farenheit}")
        Celsius = (temp_value - 273.15)
        print(f"Kelvin temp: {temp_value}\nto Celsius: {Celsius}")
    else:
        print("Sorry, I couldn't process that. Please input a number value for the temperature that you would like to input.")  


convert_temp(temp_value, temp_unit)
