#Program calculates the difference between 2 user inputted dates
#Written by Ishaan Bahl/Illusion
#Uses the python datetime module
#Runs in terminal

import datetime

print("Welcome to the date difference calculator!")

while True: 
    userInput = input("Do you want to use this program? Type yes or no: ").lower()

    if userInput == "no":
        print("Closing Program...")
        break
    
    if userInput != "yes" and userInput != "no":
        print("Please type in a valid anwser")
        continue

    dateEntry_One = input("Enter a date using the YYYY-MM-DD format: ") #Gets Date 1 
    year1, month1, day1 = map(int, dateEntry_One.split('-')) #Splits values into year, month, day
    dateOne = datetime.datetime(year1, month1, day1) #combines it all

    dateEntry_Two = input("Enter the second date using the YYYY-MM-DD format: ") #Gets Date 2
    year2, month2, day2 = map(int, dateEntry_Two.split('-')) #Splits values into year, month, day
    dateTwo = datetime.datetime(year2, month2, day2) #combines it all

    timeBetween = dateTwo - dateOne #subtracts dates

    print(f"The difference between date one ({dateOne.strftime('%Y-%m-%d')}) and date two ({dateTwo.strftime('%Y-%m-%d')}) is: {timeBetween.days} days.")
    print("Thank you for using this program.")

