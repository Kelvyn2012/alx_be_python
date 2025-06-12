def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        return num / denom
    
    except ValueError:
        return "Error: Please enter numeric values only."
    
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        
    finally:
        print("Execution completed.")
        