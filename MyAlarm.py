import datetime
#import winsound
from playsound import playsound
#import test

def alarm(timing):
	alttime = str(datetime.datetime.now().strptime(timing, "%I:%M %p"))
	
	alttime = alttime[11:-3]
	
	horeal= alttime[:2]
	horeal=int(horeal)
	mireal= alttime[3:5]
	mireal=int(mireal)
	print(f'alarm is set for {timing}')
	
	while True:
		if horeal==datetime.datetime.now().hour:
			if mireal==datetime.datetime.now().minute:
				print("alarm is running")
				file = '/Users/simrankataria/Desktop/DeskAssis/Funny alarm tone.mp3'
				file = file.replace(" ", "%20")
				playsound(file)
				
			elif mireal<datetime.datetime.now().minute:
				break
def alarm2(timing):
	alttime = str(datetime.datetime.now().strptime(timing, "%I:%M %p"))
	
	alttime = alttime[11:-3]
	
	horeal= alttime[:2]
	horeal=int(horeal)
	mireal= alttime[3:5]
	mireal=int(mireal)
	print(f'alarm is set for {timing}')
	
	while True:
		if horeal==datetime.datetime.now().hour:
			if mireal==datetime.datetime.now().minute:
				print("alarm is running")
				file = '/Users/simrankataria/Desktop/DeskAssis/Funny alarm tone.mp3'
				file = file.replace(" ", "%20")
				playsound(file)
				
			elif mireal<datetime.datetime.now().minute:
				break
