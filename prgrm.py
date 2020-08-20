import pyttsx3
import datetime
import os
import random
import webbrowser
import wikipedia
import datetime

engine = pyttsx3.init() # object creation
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 180)     # setting up new voice rate

voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)   #changing index, changes voices.


pyttsx3.speak("Welcome to my program. I am happy to HELP you!!")
print('''=======>> Welcome to my program <<=======  ''')
pyttsx3.speak("Welcome to my program. I am happy to HELP you!!")


def wish():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour<12:
        pyttsx3.speak("Good Morning. I am your personal digital Assistant - Anu")
    elif hour>=12 and hour<18:
        pyttsx3.speak("Good Afternoon. I am your personal digital Assistant - Anu") 
    else:
        pyttsx3.speak("Good Evening. I am your personal digital Assistant - Anu") 

def speak(audio):  #here audio is var which contain text
    engine.say(audio)
    engine.runAndWait()

wish()
thank = ("Thank You Vimal Daga Sir,        for this oppurtunity.    I have got to LEARN many things from YOU.")
while True:
    pyttsx3.speak("How can I help you ?")
    print("                    ")
    print("Enter the application you want to run :- ",end='')
    pyttsx3.speak("Or I  can  be your friend.   You can talk to me !")
    ip=input().lower()

    if (("run" in ip) or ("launch") or ("open")) and ( ("chrome" in ip) or ("google" in ip)):
        engine= pyttsx3.init()
        engine.say("Opening Google Chrome with a new tab.")
        engine.runAndWait()
        os.system("chrome")

    
    elif (("run" in ip) or ("launch") or ("open")) and ( ("whatsapp" in ip) ):
        speak("Opening Whatsapp for you ")
        os.system("WhatsApp")


    elif (("run" in ip) or ("launch") or ("open")) and ( ("edge" in ip) or ("microsoftedge" in ip)):
        speak("okay!, Opening Microsoft Edge")
        os.system("microsoftedge")

    elif (("run" in ip) or ("open" in ip) or ("launch" in ip)) and ("browser" in ip):
        speak("Two browsers detected. Google Chrome and Microsoft Edge. Which one to open?")
        print("1. Chrome \t 2.Edge \t :- ", end='')
        editor=input().lower()
        if ("1" in editor) or ("chrome" in editor) or("google chrome" in editor):
            speak("Opening Google Chrome with a new tab.")
            os.system("chrome")
        elif ("2" in editor) or ("edge" in editor) or ("microsoft edge" in editor) or ("microsoftedge" in editor):
          speak("okay!, Opening Microsoft Edge")
          os.system("microsoftedge")
        else:
            speak("Sorry, I don't understand")
            print("Sorry, Invalid input")

    elif (("run" in ip) or ("open" in ip) or ("launch" in ip)) and (("notepad" in ip) or ("notepad-editor" in ip)):
        speak("Opening a blank Notepad for you!")
        os.system("notepad")

    elif (("run" in ip) or ("open" in ip) or ("launch" in ip)) and (("wordpad" in ip) or ("wordpad-editor" in ip)):
        speak("Opening a unsaved Wordpad.")
        os.system("wordpad")

    elif (("run" in ip) or ("open" in ip) or ("launch" in ip)) and (("editor" in ip) or ("text" in ip)):
        speak("Two editors detected. Notepad and Wordpad. Which one to open?")
        print("1. Notepad \t 2.Wordpad \t :- ", end='')
        editor=input().lower()
        if ("1" in editor) or("notepad" in editor):
            speak("Opening Notepad")
            os.system("notepad")
        elif ("2" in editor) or("wordpad" in editor):
            speak("Opening Wordpad")
            os.system("wordpad")
        else:
            speak("Sorry, I don't understand")
            print("Sorry, Invalid input")
      		
    elif (("run" in ip) or ("open" in ip) or ("launch" in ip)) and (("media" in ip) or ("player" in ip)):
        speak("Opening Windows Media Player")
        os.system("wmplayer")
 
    elif (("run" in ip) or ("open" in ip) or ("launch" in ip)) and (("media" in ip) or ("player" in ip) or ("vlc" in ip)):
        speak("Opening VLC Player")
        os.system("vlc")

    elif (("run" in ip) or ("open" in ip) or ("launch" in ip)) and (("mediaplayer" in ip) or ("media" in ip) or ("player" in ip)):
        speak("Two media players detected. VLC and Windows Media Player. Which one to open?")
        print("1. VLC\t 2.Windows Media Player \t :- ", end='')
        editor=input().lower()
        if ("1" in editor) or ("vlc" in editor) or("VLC" in editor):
            speak("Opening VLC Player")
            os.system("vlc")
        elif ("2" in editor) or ("windows" in editor) or("windowsmediaplayer" in editor):
            speak("Opening Windows Media Player")
            os.system("wmplayer")
        else:
            speak("Sorry, I don't understand")
            print("Sorry, Invalid input")

    elif (("run" in ip) or ("open" in ip) or ("launch" in ip)) and (("python" in ip) or ("prompt" in ip)):
        speak("Opening Python Prompt")
        os.system("python")
 
    #elif (("run" in ip) or ("open" in ip) or ("launch" in ip)) and (("xampp" in ip) or ("xampp-control" in ip)):
       # speak("Opening Xampp Controller")
        #os.system("xampp-control")

    #elif (("say" in ip) or ("tell" in ip) and ("date" in ip) or ('''today's''' in ip)):
    #  date=os.system.date
    #  speak(date)

    elif (("run" in ip) or ("launch") or ("open")) and ( ("skype" in ip) ):
        speak("You would like me to open Skype for you?   Here you go.")
        os.system("Skype")

    elif (("run" in ip) or ("open" in ip) or ("launch" in ip)) and (("candycrush" in ip) or ("candy" in ip) or ("crush" in ip)):
        speak("Opening the candy crush game application for you!")
        os.system("Candy Crush Saga")

    elif ("hi" in ip) or ("hello" in ip):
      speak('Hi there ! I\'m your digital friend.')    

    elif("how are you" in ip ):  
      stMsgs = [  'I am Good and full of energy','I am fine!','I am super cool!']     
      ans_q = random.choice(stMsgs)
      speak(ans_q)
      speak('Thank you')
      speak('How are you ?')
      print('How are you ? ',end='')
      resp=input().lower()
      if ("happy" in resp) or ("cool" in resp) or ("super" in resp) or ("fantastic" in resp) or ("fine" in resp)  or ("good" in resp):
        speak("Wow, that\'s great !")
      elif ("sad" in resp) or ("not" in resp) or ("upset" in resp) or ("disappoint" in resp) or ("no" in resp):
        speak("ohh oo.. i'm Sorry")
      else:
        speak('Okay Good')     


    elif ("who are you" in ip) or ("about you" in ip) or ("your details" in ip) or ("something about you" in ip):
      about = ("I am a computer program based on Artificial Intelligence.      I am here to help you to browse the web applications you love to visit frequently, also I can be our close friend who just listen to our commands.              HAVE A GREAT DAY!!")
      print("I am a computer program based on Artificial Intelligence." "I am here to help you to browse the web applications you love to visit frequently, also I can be your close friend who just listen to your commands.","HAVE A GREAT DAY!!")
      speak(about)

    elif("play song" in ip) or ("songs" in ip):
        speak("Wow!, I am opening Spotify,    Enjoy yourself!")
        os.system("Spotify")

                
    #elif "wikipedia" in ip:
     #       speak("Searching....")
      #      ip.replace("wikipedia","")
      #      results = wikipedia.summary(ip,sentences=2)
       #     print(results)
        #    speak(results)  

    elif (("exit" in ip) or ("close" in ip) or ("stop" in ip) or ("quit" in ip)  or ("abort" in ip)  or ("bye" in ip)):
      speak(thank)
      speak("I'm going to take exit for now.                  STAY HYDRATED.                          TAKE CARE .             By Bye")
      print("Bye.")
      break

   

    elif (("shutdown" in ip) or ("turnoff" in ip)) and  (("pc" in ip) or ("computer" in ip)):
      speak(thank)
      speak("Shutting Down.")
      os.system("shutdown -s")

    elif ("math" in ip):
        speak("These are the mathematical operation I can help you with:")
        print("1. Sum of numbers",'\n', "2. Maximun item of the list","\n", "3. Minimum item of the list","\n","4. Power of a number","\n", "5. Reversed Iterator of a sequence","\n", "6. Sorting of given iterable")
        speak("Give your choice")
        ch = int(input())
        if (ch == 1):
            speak("Enter the numbers which you want to add")
            a = set(map(int, input().split()))
            speak("Here is your result")
            print(sum(a))
        
        elif (ch == 2):
            speak("Enter the numbers in the list")
            b = set(map(int, input().split()))
            speak("Here is your result")
            print(max(b))
        
        elif (ch == 3):
            speak("Enter the numbers in the list")
            c = set(map(int, input().split()))
            speak("Here is your result") 
            print(min(c))

        elif (ch == 4):
            speak("Provide the base and power in order")
            x = int(input())
            y = int(input())
            speak("Here is your result")
            print(pow(x,y))

        elif(ch == 5):
            speak("Provide the iterator")
            i = list(map(int, input().split()))
            speak("Here is your result")
            print(list(reversed(i)))

        elif( ch == 6):
            speak("Can I have the elments")
            ele = set(map(int, input().split()))
            speak("Here is your result")
            print(sorted(ele, key = None , reverse = False))

        else:
            speak("Sorry we, do not do that here")
            print("Invalid Input, sorry")

    else:
      temp = ip.replace(' ','+')
      geturl="https://www.google.com/search?q="    
      res_g = 'Sorry! I did not understand, but I will take you internet to give you the best possible answer !'
      print(res_g)
      speak(res_g)
      webbrowser.open(geturl+temp) 
      break


