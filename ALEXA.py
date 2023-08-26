import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import imdb
engine=pyttsx3.init('sapi5') #microsoft speech API(uses inbuilt voices of Windows)
voices=engine.getProperty('voices')
#print(voices[1].id) #we have 2 voices by default 'David' and 'Zira'
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)  #audio is a string
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("GOOD MORNING sir")
    elif(hour>=12 and hour<18):
        speak("GOOD AFTERNOON sir")
    else:
        speak("GOOD EVENING sir")
    speak("I am ALEXA, please tell me how may i help you")
def sendmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("bauraiayush733@gmail.com","rcmxoubuovzxtedk")
    server.sendmail("bauraiayush733@gmail.com",to,content)
    server.close()
def takeCommand(): #takes microphone input from user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1  #seconds of non listening before a phrase is considered complete
        r.phrase_threshold=0.4 #minimum seconds before an audio is considered a phrase
        #r.energy_threshold=300 #loudness in your speech to cancel out background noises
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please..")
        return "None"
    return query
wishme()
#takeCommand()
while True:
    query=takeCommand().lower()
    if 'wikipedia' in query:
        speak('searching wikipedia sir..')
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=5)
        speak("according to wikipedia ")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        print("opening youtube..")
        speak("opening youtube sir")
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        print("opening Google...")
        speak("opening google for you sir")
        webbrowser.open("google.com")
    elif 'play music' in query:
        music='E:\\Songs'
        songs=os.listdir(music)
        print(songs)
        os.startfile(os.path.join(music,songs[0]))
    elif 'the time' in query:
        time=datetime.datetime.now().strftime("%H:%M:%S")
        print(time)
        speak(f"Sir The time is- {time}")
    elif 'open code' in query:
        path="C:\Microsoft VS Code\Code.exe"
        os.startfile(path)
    elif 'send mail' in query:
        try:
            speak('what should i say')
            content=takeCommand()
            li = ['kkbaurai8@gmail.com','bauraiayush733@gmail.com','bauraiaditya7@gmail.com']
            length=len(li)
            for i in range (length):
                to=li[i]
                sendmail(to,content)
            print("mail sent successfully!")
            speak("mail has been sent successfully!")
        except Exception as e:
            print(e)
            speak("There has been an error in sending the mail!")
    elif 'search movie' in query:
        moviesdb = imdb.IMDb() #gathering information from imdb
        speak("What is the title of the movie you want to search sir")
        movie_title=takeCommand()
        movies = moviesdb.search_movie(movie_title)
        for movie in movies:
            info=movie.getID()
            movie = moviesdb.get_movie(info)
            title = movie['title']
            year = movie['year']
            rating = movie['rating']
            plot = movie['plot outline']
            if year < int(datetime.datetime.now().strftime("%Y")):
                print(f'{title} was released in {year} has IMDB rating of {rating}.\nThe plot summary of movie is{plot}')
                speak(f'{title}was released in {year} has IMDB rating of {rating}The plot summary of movie is{plot}')
            else:
                print(f'{title}will release in {year} has IMDB rating of {rating}.\nThe plot summary of movie is{plot}')
                speak(f'{title}will release in {year} has IMDB rating of {rating}.The plot summary of movie is{plot}')
    elif 'alexa stop' in query:
        exit()