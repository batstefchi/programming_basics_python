one_package_chemical = 5.80
one_package_markers = 7.20
preparation_per_liter = 1.20

packages_chemicals = int(input()) * one_package_chemical
packages_markers = int(input()) * one_package_markers
preparation = int(input()) * preparation_per_liter

total_price = (packages_chemicals + packages_markers + preparation)
discount = int(input()) / 100

total_price_with_discount = total_price - (total_price * discount)

print(total_price_with_discount)