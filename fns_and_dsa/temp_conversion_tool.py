FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


from fns_and_dsa import convert_to_celsius, convert_to_fahrenheit
try:
    Temperature = float(input("Enter the temperature to convert: "))
    scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if scale == "C":
        result = convert_to_fahrenheit(Temperature)
        print(f"{Temperature}°C is {result}°F") 
    elif scale == "F":
        result = convert_to_celsius(Temperature)
        print(f"{Temperature}°F is {result}°C") 
    else:
        print("invalid selection. Please enter C or F")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
