x = int(input('Please enter the MARK : '))
#if 75 > x & x >= 40:
 #   print('Bagan')
#elif 10 < x & x < 40:
 #   print('Beach')
#elif 10 >= x & x > 0:
#	print('KG')
#else:
 #   print('Unlisted')

if x == 100:
	print ('Scholar')

elif 100 < x and x <= 70:
	print ('Distinction')

elif x < 70 and x > 50:
	print ('Excellent')

elif x < 50 and x >= 40 :
	print ('Pass')

elif x < 34 and x > 10:
	print ('Fail')

elif x <= 10 and x >= 0:
	print ('Warining')

elif x > 34 and x < 40:
	if x == 35:
		print ('x = 35 + 5 and pass')
	elif x == 36:
		print ('x = 36 + 4 and pass')
    elif x == 37:
		print ('x = 37 + 3 and pass')
	elif x == 38:
		print ('x = 38 + 2 and pass')
	else:
		print ('x = 39 + 1 and pass')

else:
	print ('invalid')