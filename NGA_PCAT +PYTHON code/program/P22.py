# Define a list of temperatures for each day of the week
temperatures = [32, 28, 30, 34, 33, 31, 35]

# Calculate the average  temprature
average_temp = sum(temperatures) / len(temperatures)

print(f"Avarage Temparature for the  Week: {average_temp} C" )


# find  day with  temprature above  the  average

above_average_days = []
for index, temp in enumerate(temperatures):
 if temp >average_temp:
  above_average_days.append(index)

# Print  day with  temprature above the  average
if above_average_days:
 print("Days with  Temprature Above Average: ")
 for day_index in above_average_days:
  day_name = ""
  if day_index == 0:
   day_name = "Monday"
  elif day_index == 1:
   day_name  = "Tuesday"
  elif day_index == 2:
   day_name = "Wednesday"
  elif day_index == 3:
   day_name = "Thrusday"
  elif day_index == 4:
   day_name = "Friday"
  elif day_index == 5:
   day_name = "Saturday"
  elif day_index == 6:
   day_name = "Sunday"
  
  print(f"{day_name}: {temperatures[day_index]} C")
else:
 print("NO day with  tempratures above")
