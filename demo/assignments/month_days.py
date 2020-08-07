# Display no. of days in the given month

month = int(input("Enter Month [1-12]:"))
if month == 2:
    year = int(input("Enter year :"))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(29)
    else:
        print(28)
elif month in [4, 6, 9, 11]:  # month == 4 or month == 6
    print(30)
else:
    print(31)
