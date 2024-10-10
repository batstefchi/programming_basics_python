b1 = float(input())
b2 = float(input())
h = float(input())

formula_for_the_area_of_a_trapezoid = (b1 + b2) * h / 2
formatted_area = "{:.2f}".format(formula_for_the_area_of_a_trapezoid)

print(formatted_area)