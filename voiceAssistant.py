# -*- coding: utf-8 -*-

import speech_recognition as sr
import pyttsx3 
import wolframalpha
import datetime
import tkinter
import pyjokes
import time
import webbrowser
import os
import wikipedia
from ecapture import ecapture as ec
import pyautogui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
folder = "C:\\Users\\student\\Pictures\\Screenshots"

class scoreboard:
    def __init__(self, x, y):
        self.X = x
        self.O = y
    def update(self):
        if player == "X":
            self.X += 1
        elif player == "O":
            self.O += 1
    def show(self):
        print(f"{self.X}:{self.O}")
    def reset(self):
        self.X = 0
        self.O = 0
score = scoreboard(0, 0)     
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)    
        print("Unable to Recognize your voice.")  
        return "None"
     
    return query
def sayHello():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")   
  
    else:
        speak("Good Evening Sir !")  
  
    assname =("Jarvis 1 point o")
    speak("I am your Assistant")
    speak(assname)
     


if __name__ == '__main__':
    clear = lambda: os.system('cls')
    
    sayHello()

    query = takeCommand().lower() 
    #takes the commands and coverts to lwercase for easy comparison
    if "hello" in query:
        pos = str(takeCommand())
        print(pos)
    elif "calculate" in query: 	
        id = "G8E7YE-77PKYVVLKH"
        client = wolframalpha.Client("G8E7YE-77PKYVVLKH")
        indx = query.lower().split().index('calculate') 
        query = query.split()[indx + 1:] 
        res = client.query(' '.join(query)) 
        answer = next(res.results).text
        print("The answer is " + answer) 
        speak("The answer is " + answer) 
    elif 'joke' in query:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)
    elif "write a note" in query:
        speak("What should I write, sir")
        note = takeCommand()
        file = open('jarvis.txt', 'w')
        speak("Sir, should I include date and time")
        snfm = takeCommand()
        if 'yes' in snfm or 'sure' in snfm:
            Time = datetime.datetime.now().strftime("% H:% M:% S")
            file.write(Time)
            file.write(" :- ")
            file.write(note)
            file.close()
        else:
            file.write(note)
            file.close()
    elif "show note" in query:
        speak("showing notes")
        file = open("jarvis.txt", "r")
        
        note = file.read()
        print(note)
        speak(note)
    elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            print(strTime)
            speak(f"Sir, the time is {strTime}")
    elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
    elif 'search' in query or 'play' in query:
        query = query.replace("search ", "") 
        query = query.replace("play", "")		 
        webbrowser.open(query) 
    elif 'open google' in query:
        speak("Here you go to Google\n")
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
        speak("Here you go to Stack Over flow.Happy coding")
        webbrowser.open("stackoverflow.com")
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 3)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif "where is" in query:
        query = query.replace("where is", "")
        location = query
        speak("User asked to Locate")
        speak(location)
        webbrowser.open("https://www.google.nl/maps/place/" + location + "")

    elif "camera" in query or "take a photo" in query:
        ec.capture(0, "Jarvis Camera ", "img.jpg")
    elif "screenshot" in query:
        image = pyautogui.screenshot()
        file_name = "\\" + str(time.strftime("%H_%M_%S")) + ".png"
        image.save(folder + file_name)

    elif "tic-tac-toe" in query:
        blank_board = """
  1   2   3
1   |   |  
 --- --- ---
2   |   | 
 --- --- ---
3   |   |  
"""
        speak("Do you want to reset scores? Please Answer YES or No")
        takeCommand()
        
        if "yes" in query:
            print("Resetting...")
            score.reset()
            
        name   = input("What is your name? ")
        print("Welcome to Tic Tac Toe, " + name + ". Here is our playing board:")
        print(blank_board)
        
        # tic-tac-toe positions
        b = [
          [" "," "," "],
          [" "," "," "],
          [" "," "," "]
        ]
        
        
        player = "X"
        played = set() #to save already occupied positions
        
        # Loop for each turn
        play_on = True
        while play_on:
          print("It's " + player + "'s turn")
          #position = input("Enter a position (i.e., 1,1): ")
          pos = {'one':"1",'two':"2",'three':"3"}
          try:
              pos1 = takeCommand().split(" ")
              if pos1[0].isnumeric() and pos1[2].isnumeric():
                  position = f"{pos1[0]},{pos1[2]}"
              else:
                  position = f"{pos[pos1[0]]},{pos[pos1[2]]} "
              # Check the position is valid
              #if len(position) == 3:
              valid = position[0].isnumeric() and position[1] == "," and position[2].isnumeric()
              #else:
                #print("invalid position")
                #continue
              if valid:
                row = int(position[0])
                col = int(position[2])
                if row <= 3 and col <= 3:
                  valid = True
                else:
                  print("invalid position")
                  continue
              else:
                print("invalid position")
                continue
          except:
                continue
          # Update the correct variable based on the position entered
          if position in played: #check if the position is already taken
               print("already taken position")
               speak("already taken position. Pick another.")
               continue
          else:
              b[row - 1][col - 1] = player
              played.add(position.strip())
              print(played)
          
          new_board = f"""
            1   2   3
          1 {b[0][0]} | {b[0][1]} | {b[0][2]}
           --- --- ---
          2 {b[1][0]} | {b[1][1]} | {b[1][2]}
           --- --- ---
          3 {b[2][0]} | {b[2][1]} | {b[2][2]}
          """
          
          print(new_board)
          #check the rows
          for i in b:
            if i[0] == i[1] == i[2] == player:
              print('The Winner is ', player)
              speak(f"The Winner is {player}")
              score.update()
              play_on = False
            
            
        # Check the columns
        
          for i in range(3):
            if b[0][i] == b[1][i] == b[2][i] == player:
              print('The Winner is ', player)
              speak(f"The Winner is {player}")
              score.update()
              play_on = False
          
        # Check the diagonals
          if b[0][0] == b[1][1] == b[2][2] == player:
            print('The Winner is ', player)
            speak(f"The Winner is {player}")
            score.update()
            play_on = False
          elif b[0][2] == b[1][1] == b[2][0] == player:
            print('The Winner is ', player)
            speak(f"The Winner is {player}")
            score.update()
            play_on = False
        #check full board
          counter = 0
          for list in b:
            counter += 1
            if list[0] == ' ':
              break
            elif list[1] == ' ':
              break
            elif list[2] == ' ':
              break
            else:
              if counter == 3:
                play_on = False
                print("Game Over. It is a draw!!!")
                speak("Game Over. It is a draw!!!")
         
              
                  
          # Update Player
          if player == "X":
            player = "O"
          else:
            player = "X"
        score.show()  