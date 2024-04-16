
temperature = float(input("Enter temperature in degrees: "))
convert_to = input("Enter temperature to what you want to convert ('c' or 'f'): ")

def convert_to_f(temperature: int or float) -> float:
    return temperature * 1.8 + 32

def convert_to_c(temperature: int or float) -> float:
    return (temperature - 32) * 5/9

if convert_to == 'c':
    print(convert_to_c(temperature))
elif convert_to == 'f':
    print(convert_to_f(temperature))
else:
    raise ValueError("Must enter either 'c' or 'f')")




