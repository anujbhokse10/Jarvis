from playsound import playsound 
import eel

#playing assistant sound function

@eel.expose 
def playAssistantsound():
    music_dir = "C:\\Users\\Anuj\\OneDrive\\Desktop\\Jarvis\\www\\assets\\audio\\www_assets_audio_start_sound.mp3"
    playsound(music_dir)