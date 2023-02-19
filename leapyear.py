year = int(input("Which year do you want to check "))
yearStr = str(year)

if year % 4 == 0:
	if year % 100 == 0:
		if year % 400:
			print(yearStr + " is surely going to be a leap year")
		else:
			print(yearStr + "is not a leap year")
	else:
		print(yearStr + "is surely going to be a leap year")
else:
	print(yearStr + " is not a leap year")
