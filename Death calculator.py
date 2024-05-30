# score = 0
# height = 1.8
# isWinning = True

# #f-string

# print(f"your score is {score}\n  your height is {height}\n you are winning is {isWinning}\n")

age = input("What is your current age? ")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left."
print(message)