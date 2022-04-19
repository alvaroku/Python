import pyttsx3  
#con internet
from gtts import gTTS
from playsound import playsound
def conInterner():
    s = gTTS("Sample Text")
    s.save('sample.mp3')
    playsound('sample.mp3')


s = pyttsx3.init()  
data = "Sample Text"  
s.say(["hola","roberto"])  
s.say("nada") 
s.runAndWait()   