total_pages = int(input())
pages_per_hour = int(input())
days = int(input())

total_hours_need = total_pages // pages_per_hour
hours_per_day_needed = total_hours_need / days

print(int(hours_per_day_needed))