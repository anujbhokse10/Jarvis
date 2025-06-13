import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init('sapi5') 
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    print(voices)
    engine.say(text)
    engine.runAndWait() 
    
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
        print("Recognizing...")
        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query
        except Exception as e:
            print("Sorry, I did not understand that.")
            return None
        
text = takecommand()

if text:
    speak(text)