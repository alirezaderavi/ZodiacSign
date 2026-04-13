# -*- coding: utf-8 -*-

import pandas as pd
from datetime import datetime

# Function to determine zodiac sign
def get_zodiac_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"

# Take input
name = input("Enter your name: ")
birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")

# Convert string to date
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")

# Extract day and month
day = birthdate.day
month = birthdate.month

# Get zodiac sign
zodiac_sign = get_zodiac_sign(day, month)

# Create DataFrame
data = {
    "Name": [name],
    "Birthdate": [birthdate_str],
    "Zodiac Sign": [zodiac_sign]
}

df = pd.DataFrame(data)

# Save to file
df.to_csv("zodiac_data.csv", index=False)

print(f"{name}, your Zodiac sign is: {zodiac_sign}")
print("Data saved to zodiac_data.csv")

