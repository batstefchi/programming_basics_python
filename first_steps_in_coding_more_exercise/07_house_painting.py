x = float(input())
y = float(input())
h = float(input())

window = 1.5 * 1.5
side_wall = 2 * (x * y) - 2 * window
back_side = 2 * (x * x) - 1.2 * 2
basis_size = side_wall + back_side

roof_area = 2 * (x * y) + 2 * (0.5 * x * h)

green_paint_needed = basis_size / 3.4
red_paint_needed = roof_area / 4.3

print(f'{green_paint_needed:.2f}')
print(f'{red_paint_needed:.2f}')