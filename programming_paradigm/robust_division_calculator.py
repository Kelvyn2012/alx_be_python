def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        return num / denom
    
    except ValueError:
        return "Error: Invalid Input (Non-numeric)."
    
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        
    finally:
        print("Execution completed.")
        