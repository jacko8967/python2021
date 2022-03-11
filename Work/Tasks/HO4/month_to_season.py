month = input("Input the month (e.g. January, February etc.): ")

if month in ('December', 'January', 'February'):
	season = 'Summer'
if month in ('March', 'April', 'May'):
	season = 'Autumn'
if month in ('June', 'July', 'August'):
	season = 'Winter'
if month in ('September', 'October', 'November'):
	season = 'Spring'
print("Season is: {0}".format(season))