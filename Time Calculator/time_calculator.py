def add_time(str1,str2,Opt_Day=''):
	time_1 = str1.split()	#Separate hour and time (AM or PM)
	hour_min_1 = (time_1[0]).split(':')	#Separate hour and min the first string
	hour_min_2 = str2.split(':')	#Separate hour and min the second string

	if int(hour_min_1[1])+int(hour_min_2[1])>60:	#If the sum of the minutes are more than 60
		minutes_return = (int(hour_min_1[1])+int(hour_min_2[1]))%60	#Takes mod 60 to write it in minutes
		hour_min_1[0] = int(hour_min_1[0]) + 1 #Sum an hour
	else: 
		minutes_return = int(hour_min_1[1])+int(hour_min_2[1])
	if minutes_return<10:		#This part is to add a '0' to the string in case the minutes is less than 10
		minutes_return = '0' + str(minutes_return)
	minutes_return = str(minutes_return)	#Convert to a string
	x = int(hour_min_1[0])+int(hour_min_2[0])
	count_12 = 0
  #The next thing is to count if it output hour is gonna be AM or PM
	while x>12:
		count_12 = count_12 + 1
		x = x-12
	if x==12:
		count_12 = count_12 + 1
	#Convert everytinh into a string
	x=str(x)
	time_1[1]=str(time_1[1])
	Days = {'Monday': 0, 'Tuesday':1 , 'Wednesday':2, 'Thursday':3, 'Friday':4, 'Saturday':5, 'Sunday':6}
	Days_value = list(Days.keys())
	#Preparing the output
	text=''
	if (count_12)%2==0:		#If count_12%2=0 it means the time is the same (AM or PM)
		text = x + ':' + minutes_return + " " + time_1[1]
		if Opt_Day.capitalize() in Days.keys():	#If it has a day
			text = text + ', ' + Days_value[(int(((Days[Opt_Day.capitalize()]+count_12/2)%7)))]
		if count_12>3:	#More than a day have passed
			return(text + ", (" + str(int(count_12/2)) + ' days later)')
		elif count_12==2:	#Next day
			return(text + ' (next day)')
		else:	#Same day
			return(text)
	else:	#If count_12%2=1 it means the time is differente (AM to PM and viceversa)
		if (time_1[1]=='AM'):	#AM to PM
			text=x + ':' + minutes_return + " PM"
			if Opt_Day.capitalize() in Days.keys():	#If it has a day
				text = text + ', ' + Days_value[(int(((Days[Opt_Day.capitalize()]+count_12/2)%7)))]
			if count_12>3:	#More than a day have passed
				return(text + " (" + str(int(count_12/2)) + ' days later)')
			elif count_12==3:	#Next day
				return(text + ' (next day)')
			else:	#Same day
				return(text)
		else:	#PM to AM
			text=x + ':' + minutes_return + " AM"
			if Opt_Day.capitalize() in Days.keys():	#If it has a day
				text = text + ', ' + Days_value[(int(((Days[Opt_Day.capitalize()]+count_12/2)+1)%7))]
			if count_12>=3:	#More than a day have passed
				return(text + " (" + str(int(count_12/2)+1) + ' days later)')
			elif count_12==1:	#Next day
				return(text + ' (next day)')