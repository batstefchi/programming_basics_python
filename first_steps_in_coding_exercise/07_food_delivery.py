chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15
delivery_price = 2.50
price_of_the_dessert = 20 / 100

numbers_of_chicken_menus = int(input()) * chicken_menu
numbers_of_fish_menus = int(input()) * fish_menu
numbers_of_vegetarian_menus = int(input()) * vegetarian_menu

total_price_from_menus = numbers_of_chicken_menus + numbers_of_fish_menus + numbers_of_vegetarian_menus

total_price_for_the_dessert = total_price_from_menus * price_of_the_dessert

total_price = total_price_from_menus + total_price_for_the_dessert + delivery_price

print(total_price)