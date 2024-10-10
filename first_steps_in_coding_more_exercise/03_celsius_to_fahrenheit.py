celsius = float(input())

formula_for_temperature_measurement_units = celsius * 1.8 + 32
formatted_fahrenheit = "{:.2f}".format(formula_for_temperature_measurement_units)

print(formatted_fahrenheit)