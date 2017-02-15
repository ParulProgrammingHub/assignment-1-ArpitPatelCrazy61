days = input("enter the days : ")

year = days / 360
month = ( days / 30 ) - (12 * year)
days = days % 30

print(str(year) + " year " + str(month) + " month and " + str(days) + " days")
