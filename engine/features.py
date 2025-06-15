import os
from playsound import playsound 
import eel

from engine.command import speak
from engine.config import ASSISTANT_NAME

#playing assistant sound function

@eel.expose 
def playAssistantsound():
    music_dir = "C:\\Users\\Anuj\\OneDrive\\Desktop\\Jarvis\\www\\assets\\audio\\www_assets_audio_start_sound.mp3"
    playsound(music_dir)
    
    
def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()
    
    if query!= "":
        speak("opening " + query)
        os.system("start " + query)
    else:
        speak("not found")
    