# output format - You have x days, y months and z years left.
# approch - using f string

age_year_currently = int( input( "Enter your age: "))

years_remaining = 90 - age_year_currently
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365

print(f"You have {days_remaining} days, {months_remaining} months and {years_remaining} years ")

# Success in 1 try