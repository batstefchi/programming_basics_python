price_of_mackerel_per_kilograms = float(input())
price_of_pikeperch_per_kilograms = float(input())
kilograms_palamud = float(input())
kilograms_safrid = float(input())
kilograms_mussels = int(input())

price_of_palamud = price_of_mackerel_per_kilograms * 1.60
price_of_safrid = price_of_pikeperch_per_kilograms * 1.80

total_cost = (price_of_palamud * kilograms_palamud) + (price_of_safrid * kilograms_safrid) + (kilograms_mussels * 7.50)

print(f"{total_cost:.2f}")