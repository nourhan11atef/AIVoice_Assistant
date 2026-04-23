import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime

r = sr.Recognizer()

def speak(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(command)
    engine.runAndWait()

def commands():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("I am listening... you can ask")
            audioin = r.listen(source)
            my_text = r.recognize_google(audioin)
            my_text = my_text.lower()
            print(my_text)
            # ask to play video
            if 'play' in my_text:
                my_text = my_text.replace('play', '')
                speak('playing ' + my_text)
                pywhatkit.playonyt(my_text)
            #Ask date
            elif 'date' in my_text:
                today = datetime.date.today()
                speak(str(today))
            #Ask Time
            elif 'time' in my_text:
                timenow = datetime.datetime.now().strftime('%I:%M')
                speak(timenow)
            #Ask Details about any topic
            elif 'tell me about' in my_text:
                topic = my_text.replace('tell me about', '')
                info = wikipedia.summary(topic, 1)
                speak(info)
            else:
                speak("Please ask correct question")
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")

while True:
    commands()
