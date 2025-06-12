def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        return num / denom
    
    except ValueError:
        return "Error: Invalid Input (Non-numeric)."
    
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        
    finally:
        print("Execution completed.")
        