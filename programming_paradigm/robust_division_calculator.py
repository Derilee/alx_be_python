def safe_divide(numerator, denominator):
    try:
        if numerator != 0 or denominator != 0:
            result = float(numerator)/float(denominator)
            return (f"The result of the division is {result}")
    except ZeroDivisionError:
        return ("Error: Cannot divide by zero.") 
    except ValueError:
        return ("Error: Please enter numeric values only.")
