from datetime import datetime

birth_date = input("Input your date of birth using this format (Date-M0nth-Year): \n")

date_of_birth = datetime.strptime(birth_date,  "%d-%m-%Y").date()
today = datetime.now().date()
age = today - date_of_birth
years = age.days // 365
months = (age.days % 365) // 30
days = (age.days % 30)
print(f"You were born on {birth_date} and you are {years} years old.")