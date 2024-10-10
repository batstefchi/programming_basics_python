euro_to_bgn = 1.94

price_per_kilograms_of_vegetables = float(input())
price_per_kilograms_of_fruits = float(input())
total_kilograms_of_vegetables = int(input())
total_kilograms_of_fruits = int(input())

vegetables_price = price_per_kilograms_of_vegetables * total_kilograms_of_vegetables
fruits_price = price_per_kilograms_of_fruits * total_kilograms_of_fruits

total_price = vegetables_price + fruits_price
total_price_in_euro = total_price / euro_to_bgn

formatted_price = "{:.2f}".format(total_price_in_euro)

print(formatted_price)