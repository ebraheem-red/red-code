import telepot
from telepot.loop import MessageLoop
import google.generativeai as genai

chats = {}


genai.configure(api_key="AIzaSyBvofZTfRS1nZH8bWcNEf62F844wCs4v48")
model = genai.GenerativeModel('gemini-pro', generation_config=genai.GenerationConfig(max_output_tokens=2000,temperature=0))
#chat = model.start_chat(history=[])

def handle(msg):
    chat_id = msg['chat']['id']
    text = msg['text']

    if chat_id not in chats:
        chats[chat_id]= model.start_chat(history=[])

    chat = chats[chat_id]
    response = chat.send_message(text)
    bot.sendMessage(chat_id,response.text)

bot = telepot.Bot('7195108723:AAEefyn-ygqqmP1YwfRSa6qfIeZey4qrF1s')
MessageLoop(bot, handle).run_forever()
print('Listening ...')
