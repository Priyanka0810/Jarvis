import speech_recognition as sr
import pyttsx3
import pyjokes 
import webbrowser
import os
from datetime import datetime
import wikipedia
import pygetwindow as gw


assis_name = "Jarvis"
boss_name = "Priyanka"

def say(text):
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice',voice[0].id)
    engine.setProperty('rate',130)
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            text = r.recognize_google(audio,language='en-in')
            print(f"User said : {text}\n")
        except Exception as e:
            print(e)
            print("can not recognize your voice")
            return "None"
        return text
    
def tell_joke():
    joke = pyjokes.get_joke()
    return joke

def close_edge_tabs(title):
    for window in gw.getWindowsWithTitle(title):
        window.close()
    
def respond(text):
    if 'hello' in text or 'hai' in text:
        say("Hello MAM")
    elif 'who are you' in text:
        say(f"I am {assis_name}, your personal voice assistant. How can I assist you today?")
    elif 'good morning' in text:
        say("A warm" + text)
        say(f"how are you {boss_name}")
    elif 'I am fine' in text:
        say("I'm glad to hear that!")
    elif 'who I am' in text:
        say("You are my user and friend")
    elif 'see you' in text:
        say("see you later, take care")
    elif 'who is your boss' in text:
        say(f"my boss is {boss_name} and she is super cool")
    elif 'how are you' in text:
        say("I'm doing well, thank you for asking!")
    elif 'tell me joke' in text:
        enginge2 = pyttsx3.init()
        enginge2.setProperty('rate',130)
        enginge2.say(tell_joke())
        enginge2.runAndWait()
    elif 'open' in text:
        text=text.replace("open","").strip()
        if 'notepad' in text.lower():
            os.startfile('C:\\Program Files\\Notepad++\\notepad++.exe')
        elif 'youtube' in text.lower():
            webbrowser.open('https://www.youtube.com')
        elif 'google' in text.lower():
            webbrowser.open('https://www.google.com')

    elif 'close' in text:
        text = text.replace("close", "").strip()
        if 'notepad' in text.lower():
            os.system("TASKKILL /F /IM notepad++.exe")
        elif 'youtube' in text.lower():
            close_edge_tabs('YouTube')
        elif 'google' in text.lower():
            close_edge_tabs('Google')

    elif 'time' in text:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        say(f"The current time is {current_time}")

    elif 'search wikipedia' in text.lower():
        query = text.lower().replace('search wikipedia', '').strip()
        try:
            say("Searching Wikipedia...")
            summary = wikipedia.summary(query, sentences=2)
            say(summary)
        except wikipedia.exceptions.DisambiguationError as e:
            say(f"There are multiple results for {query}. Please be more specific.")
        except wikipedia.exceptions.PageError:
            say(f"I could not find any results for {query}.")
        except wikipedia.exceptions.WikipediaException as e:
            say(f"An error occurred while searching Wikipedia: {e}")

    elif "play music" in text:
            music_dir = r"E:\songs"
            try:
                songs = os.listdir(music_dir)
                print(songs)
                if songs:
                    os.startfile(os.path.join(music_dir, songs[0]))
                else:
                    say( "No songs found in the directory.")
            except FileNotFoundError:
                say( "Music directory not found.")

    elif 'stop' in text or 'bye' in text:
        say("Goodbye!")
        return False
    return True

        


say("Hi, I'm Jarvis Please tell me how may I assist you")    

while True:
    text = takecommand()
    if text == "None":
        continue
    if not respond(text):
        break
    
