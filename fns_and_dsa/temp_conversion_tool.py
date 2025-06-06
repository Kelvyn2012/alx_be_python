# temp_conversion_tool.py

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def convert_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def main():
    temp_input = input("Enter the temperature to convert (just the number): ").strip()

    try:
        temperature = float(temp_input)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'F':
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result:.2f}°C")
    elif unit == 'C':
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result:.2f}°F")
    else:
        print("Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
