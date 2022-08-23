year = int(input("Input year"))
if year % 4 ==0 and year % 100 == 0 or year%400==0:
	print('Leap year')
else:
	print('Year is not a leap year')
	