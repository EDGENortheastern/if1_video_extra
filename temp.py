def celsius_to_far(celsius_temp):
    return celsius_temp*9/5 +32

user_input = input("Enter temperature in Celsius: ")

try:
    celsius = float(user_input)
    fahrenheit = celsius_to_far(celsius)
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
except ValueError:
    print("Please enter a valid number.")
