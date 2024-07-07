FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


from fns_and_dsa import convert_to_celsius, convert_to_fahrenheit
Temperature = float(input("Enter the temperature to convert: "))
scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if scale == "C":
    result = convert_to_fahrenheit(Temperature)
    print(f"{Temperature}°C is {result}°F")
elif scale == "F":
    result = convert_to_celsius(Temperature)
    print(f"{Temperature}°F is {result}°C")
else:
    print("Invalid temperature. Please enter a numeric value")
