age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
cal_week = int(age)
ex_age = 90
weeks_year = 52
days_year = 365

week_left = (ex_age - cal_week) * weeks_year
days_left = (ex_age - cal_week) * days_year
print(f"you have {week_left} weeks left")
print(f"you have {days_left} days left")


