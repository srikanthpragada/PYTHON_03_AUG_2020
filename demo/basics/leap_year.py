# Take year and display whether it is leap year

year = input("Enter year :")
year = int(year)  # Convert string to int

if year % 4 == 0:
    print("Leap Year")
else:
    print("Not a leap year")

