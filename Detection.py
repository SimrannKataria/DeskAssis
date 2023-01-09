import speech_recognition as sr
import pyquark


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
			return "Sorry I couldn't understand that"
			
		return query.lower()
		
while True:
	wake_up = takecommand()
	if 'wake up' in wake_up:
		pyquark.filestart("/Users/simrankataria/Desktop/DeskAssis/test.py")
		
	else:
		print("Could not access the file")