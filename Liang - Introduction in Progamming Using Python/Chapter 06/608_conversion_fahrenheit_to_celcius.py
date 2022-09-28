# define conversion Fahrenheit to Celcius
def fahrenheitToCelcius(fahrenheit1):
    celsius1 = (5 / 9) * (fahrenheit1 - 32)
    return celsius1

# define conversion Celsius to Fahrenheit
def celsiusToFahrenheit(celsius2):
    fahrenheit2 = (9 / 5) * celsius2 + 32
    return fahrenheit2

# define main function
def main():
    print("==============================================================")
    print("||", format("Celsius", "10s"), "|", "Fahrenheit", "||", "Fahrenheit", "|", format("Celsius", "10s"), "||")
    print("--------------------------------------------------------------")
    celsius = 40.0
    fahrenheit = 120.0
    while celsius > 29.0 and fahrenheit > 20.0:
        print("||", format(celsius, "10.1f"), "|", format(celsiusToFahrenheit(celsius), "10.1f"), "||", format(fahrenheit, "10.1f"), "|", format(fahrenheitToCelcius(fahrenheit), "10.1f"), "||")
        celsius -= 1
        fahrenheit -= 10
    print("--------------------------------------------------------------")
# invoke main function
main()