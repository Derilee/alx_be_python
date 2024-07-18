def safe_divide(numerator, denominator):
    try:
        if numerator == 0 or denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        elif numerator != 0 or denominator !=0:
            result = float(numerator)/float(denominator)
            print(f"The result of the division is {result}")
    except ValueError:
        print("Error: Please enter numeric values only.")
