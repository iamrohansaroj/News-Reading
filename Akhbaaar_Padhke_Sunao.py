import requests
import json


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
    speak("News for today..Lets begin")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=81ecc31a12a34dabacbf6052b795d37f"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        print(article['title'])
        speak("Moving on to the next news. Listen Carefully")

    speak("Thanks for Listening")
