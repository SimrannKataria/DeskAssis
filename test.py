import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import pyquark
import pyautogui
import wikipedia
import pyjokes
from PyDictionary import PyDictionary as Diction
import datetime
from playsound import playsound


Assistant= pyttsx3.init('nsss')
voices = Assistant.getProperty('voices')
#print(voices)
Assistant.setProperty('voices',voices[4].id)
Assistant.setProperty('rate', 170)

def Speak(audio):
    print("  ")
    Assistant.say(audio)
    print(f":{audio}")
 
    Assistant.runAndWait()

def takecommand():
	command = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		command.pause_threshold = 1
		audio = command.listen(source)
		
		try:
			print("Give me a second...")
			query = command.recognize_google(audio, language= 'en-in')
			print(f"You said: {query}\n")
			
		except Exception as Error:
			return "Sorry"
			
		return query.lower()

def TaskExe():


	Speak("Hello, I am up")
	Speak("How can I help you")
	
	
	def dictionary():
		Speak("Dictionary mode activated")
		Speak("Tell me the word, make sure you include the word 'meaning','antonym' or 'synonym' in your command")
		word = takecommand()
		
		if 'meaning' in word:
			word = word.replace("what is the", '')
			word = word.replace("meaning", '')
			word = word.replace('of', '')
			word = word.replace('meaning of', '')
			result = Diction.meaning(word)
			Speak(f'The meaning of {word} is {result}')
			
		elif 'synonym' in word:
			word = word.replace("what is the", '')
			word = word.replace("synonym", '')
			word = word.replace('of', '')
			word = word.replace('synonym of', '')
			result = Diction.synonym(word)
			Speak(f'The synonym of {word} is {result}')
			
		elif 'antonym' in word:
			word = word.replace("what is the", '')
			word = word.replace("antonym", '')
			word = word.replace('of', '')
			word = word.replace('antonym of', '')
			result = Diction.antonym(word)
			Speak(f'The antonym of {word} is {result}')
			
	
		
	def openapps():
		if 'whatsapp' in query:
			pyquark.filestart('/Applications/WhatsApp.app')

		elif 'spotify' in query:
			pyquark.filestart('/Applications/Spotify (old).app')
 			
 	#def closeapps():
 		#Speak("Okay, closing your app")
 		
 		#if 'spotify' in query:
 			#sos.system

	def whatsapp():
		Speak("Who do you want to send the message to?")	
		name = takecommand().lower().strip()
		
		
		
		if 'robin' in name:
			Speak("What do you want to say to "+ name)
			msg=takecommand()
			Speak("In how many hours?")
			hour=int(takecommand())
			Speak("In how many minutes")
			time_min= int(takecommand())
			pywhatkit.sendwhatmsg("+919311449797", msg, hour,time_min, 10)
			Speak("okay, I will send the text")
			
		if 'shivansh' in name:
			Speak("What do you want to say to "+ name)
			msg=takecommand()
			Speak("In how many hours?")
			hour=int(takecommand())
			Speak("In how many minutes")
			time_min= int(takecommand())
			pywhatkit.sendwhatmsg("+919811139654", msg, hour,time_min, 10)
			Speak("okay, I will send the text")
			
		if 'peshu' in name:
			Speak("What do you want to say to "+ name)
			msg=takecommand()
			Speak("In how many hours?")
			hour=int(takecommand())
			Speak("In how many minutes")
			time_min= int(takecommand())
			pywhatkit.sendwhatmsg("+919871122240", msg, hour,time_min, 10)
			Speak("okay, I will send the text")
			
		if 'arin' in name:
			Speak("What do you want to say to "+ name)
			msg=takecommand()
			Speak("In how many hours?")
			hour=int(takecommand())
			Speak("In how many minutes")
			time_min= int(takecommand())
			pywhatkit.sendwhatmsg("+15483338795", msg, hour,time_min, 10)
			Speak("okay, I will send the text")
			
		if 'mama' in name:
			Speak("What do you want to say to "+ name)
			msg=takecommand()
			Speak("In how many hours?")
			hour=int(takecommand())
			Speak("In how many minutes")
			time_min= int(takecommand())
			pywhatkit.sendwhatmsg("+919899991817", msg, hour,time_min, 10)
			Speak("okay, I will send the text")
			
		if 'pops' in name:
			Speak("What do you want to say to "+ name)
			msg=takecommand()
			Speak("In how many hours?")
			hour=int(takecommand())
			Speak("In how many minutes")
			time_min= int(takecommand())
			pywhatkit.sendwhatmsg("+919811449797", msg, hour,time_min, 10)
			Speak("okay, I will send the text")
			
		if 'goenka' in name:
			Speak("What do you want to say to "+ name)
			msg=takecommand()
			Speak("In how many hours?")
			hour=int(takecommand())
			Speak("In how many minutes")
			time_min= int(takecommand())
			pywhatkit.sendwhatmsg("+919312250453", msg, hour,time_min, 10)
			Speak("okay, I will send the text")
			

			
		

			
		


	while True:
		query = takecommand()
		
		if 'hello' in query:
			Speak("Hello, I am your personal assistant")
			Speak("How may I help you?")
			
		elif 'how are you' in query:
			Speak("Mai badiya, what about you")
			
		elif 'what\'s up' in query:
			Speak("Bore yaar")
			
		elif 'what is your name' in query:
			Speak("Jethalaal")
			
		elif 'exit' in query:
			Speak("See you later, love")
			break
			
		elif 'bye' in query:
			Speak("See you later, love")
			break
			
		elif 'stupid' in query:
			Speak("No, you're stupid")
			Speak("I am smart")
			
		elif 'youtube' in query:
			Speak("This is what I found on youtube")
			query=query.replace("jarvis","")
			query=query.replace("search on youtube","")
			query=query.replace("on youtube","")
			query=query.replace("youtube","")
			web='https://www.youtube.com/results?search_query='+ query
			webbrowser.open(web)
			Assistant.runAndWait()
			Speak("Action Completed!")
		
		elif 'google' in query:
			Speak("This is what I found on google")
			query = query.replace("jarvis","")
			query=query.replace("on google","")
			query=query.replace("google","")
			query = query.replace("search on google", "")
			pywhatkit.search(query)
			Assistant.runAndWait()
			Speak("Action Completed!")
			
		elif 'open' in query:
			Speak("Okay, Launching...")
			query = query.replace("jarvis","")
			query = query.replace("open website", "")
			query = query.replace('website', '')
			web1 = query.replace("open","")
			web2 =('https://www.' + web1 + '.com').replace(' ','')
			webbrowser.open(web2.strip())
			Assistant.runAndWait()
			Speak("Action Completed!")
			

			
		elif 'netflix' in query:
			Speak("Okay, launching...")
			web2 = 'https://www.netflix.com/browse'
			webbrowser.open(web2)
			Assistant.runAndWait()
			Speak("Action Completed!")
			
		elif 'spotify on web' in query:
			Speak("Okay, launching...")
			web2 = 'https://open.spotify.com'
			webbrowser.open(web2)
			Assistant.runAndWait()
			Speak("Action Completed!")
		
		elif 'wikipedia' in query:
			Speak("Searching on wikipedia...")
			query = query.replace("jarvis","")
			query = query.replace("search on wikipedia", "")
			query=query.replace("wikipedia","")
			wiki = wikipedia.summary(query,2)
			Speak(f"According to Wikipedia: {wiki}")
			
		elif 'who is' in query:
			Speak("Searching on wikipedia...")
			query = query.replace("jarvis","")
			query = query.replace("search on wikipedia", "")
			query=query.replace("wikipedia","")
			query=query.replace("who is","")
			query=query.replace("who","")
			wiki = wikipedia.summary(query,2)
			Speak(f"According to Wikipedia: {wiki}")
			
		elif 'whatsapp message'	in query:
			whatsapp()
			
		elif 'screenshot' in query:
			ss = pyautogui.screenshot()
			ss.save('image','png')
			Speak("Screenshot taken")
			
		elif 'whatsapp' in query:
			openapps()
		
		elif 'spotify' in query:
			openapps()
			
		elif 'joke' in query:
			getj = pyjokes.get_joke()
			Speak(getj)
		
		elif 'repeat my words' in query:
			Speak("Sure, say what you want me to repeat")
			rep = takecommand()
			Speak(f"You said:{rep}")
			
		
		elif 'dictionary' in query:
			dictionary()
		
		elif 'meaning' in query:
			dictionary()
			
		elif 'synonym' in query:
			dictionary()
		
		elif 'antonym' in query:
			dictionary()
			
		elif 'alarm' in query:
			Speak("Do you want to speak or type?")
			word = takecommand()
			if word == 'type':
				Speak("Set the alarm for when?")
				Speak("Example format: 5:30 AM")
				
				time = input("Enter the time:")
				time = time.replace('.',"")
				time = time.upper()
				import MyAlarm
				MyAlarm.alarm2(time)
				
				#while True:
					#Time_Ac = datetime.datetime.now()
					#now = Time_Ac.strftime("%H:%M:%S")
					#Speak(f"You set an alarm for {time}")
						#file = '/Users/simrankataria/Desktop/DeskAssis/Funny alarm tone.mp3'
						#file = file.replace(" ", "%20")
						#playsound(file)
						#Speak("Alarm ends")
						
					#elif now>time:
						#break
						
					
						
			if word == 'speak':
				#Speak("Tell me the hours")
				#time_hour = int(takecommand())
				#Speak("Tell me the minutes")
				#time_min = int(takecommand())
				#Speak("Tell me the seconds")
				#time_sec = int(takecommand())
				#while True:
					#Time_Ac = datetime.datetime.now()
					#now = Time_Ac.strftime("%H:%M:%S")
					
					#str(time_hour) = now.strftime('%H')
					#str(time_min) = now.strfttime('%M')
					#str(time_sec) = now.strfttime('%s')
					
					#if now == time:
						#Speak(f"You set an alarm for {time_hour} hours {time_min} minutes {time_sec} seconds")
						#file = '/Users/simrankataria/Desktop/DeskAssis/Funny alarm tone.mp3'
						#file = file.replace(" ", "%20")
						#playsound(file)
						#Speak("Alarm ends")
						
					#elif now>time:
						#break
						
				Speak("Set the alarm for when?")
				Speak("Example format: 5:30 AM")
				time = takecommand()
				time = time.replace('.',"")
				time = time.upper()
				import MyAlarm
				MyAlarm.alarm(time)
				
 		
			
TaskExe()
			

		
		
			























































