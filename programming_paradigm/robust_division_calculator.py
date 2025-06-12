def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        return f"The result of the division is {result}"
    
    except ValueError:
        return "Error: Please enter numeric values only."
    
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        
    finally:
        print("Execution completed.")
        