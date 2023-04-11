import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyaudio
import pyjokes
import time

def sp_text():
	while True:
		recognizer = sr.Recognizer()
		with sr.Microphone() as source:
			print("Speek Us the Command")
			recognizer.adjust_for_ambient_noise(source)
			audio = recognizer.listen(source, timeout=1, phrase_time_limit=10)
			try:
				print("Recognizing....")
				data = recognizer.Recognize_google(audio)
				return data
			except sr.UnknownValueError:
				print("Speech Not Recognizable")

def speech_txt(x):
	engine = pyttsx3.init()
	voices = engine.getProperty("voices")
	engine.setProperty("voice", voices[1].id)
	rate = engine.getProperty("rate")
	engine.setProperty("rate", 150)
	engine.say(x)
	engine.runAndWait()
	speech_txt("Hello Welcome to MeLappy")

if __name__ == '__main__':

	if "Hey Peter" in sp_text().lower():
		while True:
			data1 = sp_text().lower()
			if "your name" in data1:
				name = "my name is peter"
				speech_txt(name)
			elif "old are you" in data1:
				age = "i am two years old"
				speech_txt(age)
			elif "Time" in data1:
				time = datetime.datetime.now().strftime("%I%M%p")
				speech_txt(time)
			elif "youtube" in data1:
				webbrowser.open("https://www.youtube.com/watch?v=S1bVRoiwoZQ")
			elif "jokes" in data1:
				joke_1 = pyjokes.get_joke(language="en", catagory="neutral")
				speech_txt(joke_1)
			elif "play song" in data1:
				add = "pass"
				listsong = os.listdir(add)
				print(listsong)
				os.startfile(os.path.join(add, listsong[0]))
			elif "exit" in data1:
				speech_txt("Thank you")
				break
			time.sleep(15)
	else:
		print("Thanks")	