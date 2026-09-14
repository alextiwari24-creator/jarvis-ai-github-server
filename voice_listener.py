import speech_recognition as sr
import pyttsx3
import threading
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class VoiceListener:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.listening = False
        
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
        
    def listen_for_wake_word(self):
        with sr.Microphone() as source:
            try:
                audio = self.recognizer.listen(source, timeout=5)
                text = self.recognizer.recognize_google(audio).lower()
                if 'jarvis' in text or 'hey' in text:
                    self.speak('Yes, I am here')
                    return True
            except:
                pass
        return False
    
    def listen_for_command(self):
        with sr.Microphone() as source:
            try:
                audio = self.recognizer.listen(source, timeout=5)
                command = self.recognizer.recognize_google(audio).lower()
                return command
            except:
                return None
    
    def start_listening(self, callback):
        self.listening = True
        thread = threading.Thread(target=self._listening_loop, args=(callback,), daemon=True)
        thread.start()
        
    def _listening_loop(self, callback):
        while self.listening:
            if self.listen_for_wake_word():
                cmd = self.listen_for_command()
                if cmd:
                    callback(cmd)
