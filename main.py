import telebot
import requests
import pyttsx3
from googletrans import Translator

bot = telebot.TeleBot('')
engine = pyttsx3.init()
t = Translator()



def translate(text):
      return t.translate(text,dest='ru').text



def get_fact() -> str:
    url = 'https://uselessfacts.jsph.pl/api/v2/facts/random'
    response = requests.get(url)

    if response.status_code == 200:
            return response.json().get('text','мема не будет')
    else:
            return 'смешных фактов не'



def speak(text: str):
    # engine.say(text)
    engine.save_to_file(text, "file.mp3")
    engine.runAndWait()

@bot.message_handler(commands=['start','help'])
def start(message):
    bot.send_message(message.chat.id, '''привет hiii,я рассказываю интересные факты\n\nнапиши /fact''')


@bot.message_handler(commands=['fact'])
def fact(message):
    s = get_fact()
    s = translate(s)
    speak(s)

    with open("file.mp3", "rb") as f:
            bot.send_voice(message.chat.id, f)





bot.polling()