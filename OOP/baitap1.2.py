#How many seconds are there in 42 minutes and 42 seconds?
minutes=42
seconds=42
total_seconds=minutes*60+seconds
print("1.There are", total_seconds, "seconds in 42 minutes and 42 seconds.")
#How many miles are there in 10 kilometers? 
kilometers=10
miles=kilometers*0.621371
print("2.There are", miles, "miles in 10 kilometers.")
#If you run a 10 kilometer race in 42 minutes and 42 seconds, what is your average pace (time per mile in minutes and seconds)?
time_hours= total_seconds /3600
speed = miles / time_hours
print("3. Average speed (mph):", speed)
pace_seconds = total_seconds / miles
pace_minutes = int(pace_seconds // 60)
pace_remaining_seconds = int(pace_seconds % 60)
print("Average pace:", pace_minutes, "minutes", pace_remaining_seconds, "seconds per mile")