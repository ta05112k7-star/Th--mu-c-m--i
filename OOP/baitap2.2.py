#1
import math 
r=5
volume= (4/3) * math.pi * r**3
print("Volume of sphere:", volume)
#2
cover_price = 24.95
discount = 0.40
copies = 60
price_after_discount = cover_price * (1 - discount)
book_cost = price_after_discount * copies
shipping = 3 + (copies - 1) * 0.75
total_cost = book_cost + shipping
print("Total wholesale cost:", total_cost)
#3
start_hour = 6
start_minute = 52
easy_pace = 8 * 60 + 15
tempo_pace = 7 * 60 + 12
total_run_time = easy_pace + 3 * tempo_pace + easy_pace
hours = total_run_time // 3600
minutes = (total_run_time % 3600) // 60
seconds = total_run_time % 60
finish_minutes = start_minute + minutes
finish_hours = start_hour + finish_minutes // 60
finish_minutes = finish_minutes % 60
print("Breakfast time:", finish_hours, ":", finish_minutes)