deposit_amount = float(input())
deposit_mouths = int(input())
annual_interest_rate = float(input()) / 100

final_amount = deposit_amount + deposit_mouths * ((deposit_amount * annual_interest_rate) / 12)

print(final_amount)