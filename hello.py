# Name: Nidhi Kathuria
# Date: 2025-10-8
# Project Title: Daily Calorie Tracker 

print("Daily Calorie Tracker")
print("This program will help you track your calorie intake for the day.")

meals = []
calories = []

num_meals = int(input("How many meals to log? "))

for i in range(num_meals):
    print(f"\nMeal {i+1}")
    meal_name = input("Enter meal name: ")
    
    calorie_amount = float(input(f"Enter calories for {meal_name}: "))
    
    meals.append(meal_name)
    calories.append(calorie_amount)

total_calories = sum(calories)
average_calories = total_calories / num_meals if num_meals > 0 else 0

daily_limit = float(input("\nEnter your daily calorie limit: "))

limit_status = ""
if total_calories > daily_limit:
    limit_status = f"You are {total_calories - daily_limit:.0f} calories OVER your limit."
else:
    limit_status = "You are WITHIN your daily limit."