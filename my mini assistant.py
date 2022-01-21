import pyttsx3
import datetime
import webbrowser
import os
import json
import requests
import calendar
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#you can change voice of female to male here
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("hello sir i am your mini assistant !what's your name!")
print("please enter your name")
name = input()
def news():
    #url = "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=(please enter your api key here)"
    #enter api for news
    data = requests.get(url).text
    news = json.loads(data)
    p = news["articles"]
    for i in p:
        print(i["title"])
        speak(i["title"])
def today():
    p = datetime.datetime.now()
    r = p.strftime("%d-%m-%y")
    d, m, y = p.strftime("%d-%m-%y").split("-")
    p = calendar.day_name[calendar.weekday(int(y), int(m), int(d))]
    q = p.upper()
    print(f"DATE:-{r} , DAY:-{q}")
    speak(f"today is {q}")
def weather():
    print("Enter city name")
    inp = input().lower()
    city = inp.capitalize()
    #key = "(please enter your api key here)"
    #enter api for weather
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
    data = requests.get(url).text
    weather = json.loads(data)
    w = weather['main']
    print("TEMPRATURE:-", "{:.2f}".format((w['temp'] - 273.15)), "Celcius")
    print("HUMIDITY:-", w['humidity'], "%")
    print("PRESSURE:-", w['pressure'], "hPa")
    s = weather['wind']
    print("SPEED OF WIND:-", s['speed'], "Km/h")
    print(20*"_")
def game():
    speak("WELCOME TO SNAKE,WATER,GUN GAME")
    i=1
    c=0
    u=0
    t=0
    speak("RULE is you have to press w for water, g for gun and s for snake")
    while(i<11):
        import random
        list = ["s", "g", "w"]
        v = random.choice(list)
        speak(f"Attempt number {i}")
        print(f"Attempt number {i}")
        print("(press s to choose snake,g for gun and w for water)")
        j=input()
        if(j=="s" and v=="w"):
            print("I choose",v)
            print("You won in this attempt")
            speak("You won this attempt")
            u=u+1
        if (j =="s" and v =="s"):
            print("I choose", v)
            print("Tie in this attempt")
            speak("game Tied in this attempt")
            t=t+1
        if (j =="s" and v =="g"):
            print("I choose", v)
            print("I won in this attempt")
            speak("I won this attempt")
            c = c + 1
        if (j=="w" and v =="g"):
            print("I choose", v)
            print("You won in this attempt")
            speak("You won this attempt")
            u = u + 1
        if (j=="w" and v=="w"):
            print("I choose", v)
            print("game Tied in this attempt")
            speak("Tied")
            t = t + 1
        if (j=="w" and v =="s"):
            print("I choose", v)
            print("I won in this attempt")
            speak("I won this attempt")
            c = c + 1
        if (j=="g" and v=="s"):
            print("I choose", v)
            print("You won in this attempt")
            speak("You won this attempt")
            u = u + 1
        if (j=="g" and v=="g"):
            print("I choose", v)
            print("Tie in this attempt")
            speak("game Tied in this attempt")
            t = t + 1
        if (j=="g" and v=="w"):
            print("I choose", v)
            print("I won in this attempt")
            speak("I won this attempt")
            c = c + 1
        i=i+1
        print(75*"-")
    print("I won ",c,"attempt,you won ",u,"attempt and game tied",t, "times")
    speak(f"I won {c} attempt,you won {u} attempt and game tied {t} times")
    print(70*"*",end="\n")
    if(u<c):
        print("FINALLY I WON")
        speak(" computer won")
    elif(u>c):
        print("FINALLY YOU WON")
        speak(f"congratulation {name} you won this game")
    elif(u==c):
        print("EQUALLY WINNER :)")
        speak("both of us won ")
def greetings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak(f"Please tell me {name} how may I help you")
def order():
    print("please enter number which you want to perform\n"" 1 wikipedia \n 2 open youtube \n"
          " 3 open google \n 4 play music \n 5 the time \n 6 today(date and day)  \n 7 weather"
          " \n 8 news headlines\n 9 want to play snake,water,gun game\n")
    try:
        command = input()
        speak(f"okay {name}")
    except Exception as e:
        speak("sorry,i can't do this")
        return "None"
    return command
if __name__ == "__main__":
    greetings()
    while True:
        command = order()
        if '1' in command:
            webbrowser.open("https://www.wikipedia.org/")
        elif '2' in command:
            webbrowser.open("youtube.com")
        elif '3' in command:
            webbrowser.open("google.com")
        elif '4' in command:
            music_dir = 'D:\\song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif '5' in command:
            nowtimeis = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{name}, the time is {nowtimeis}")
            print(f"the time is {nowtimeis}")
        elif '6' in command:
            today()
        elif '7' in command:
            weather()
        elif '8' in command:
            speak("headlines are!")
            news()
        elif '9' in command:
            game()



