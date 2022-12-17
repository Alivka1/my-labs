import telebot
import requests
bot = telebot.TeleBot('5906689447:AAFqM_zPPlmNE8pEkuzM9GBuHbl2M2UYd1Q')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Здарова, <b>{message.from_user.first_name} {message.from_user.last_name}</b>, а точнее НУБИК.    '
    helps = f'<u>Чтобы ознакомиться с правилами бота нажми /help , Иначе ты нубик!!!!</u>'
    bot.send_message(message.chat.id, mess + helps, parse_mode='html')
@bot.message_handler(commands=['help'])
def help(message):
    if message.text =='help' or message.text =='/help':
        bot.send_message(message.chat.id,'Чтобы получить фото милого пупсика, воспользуйся командой /murmur')
@bot.message_handler(commands=['murmur'])
def mur(message):
    r = requests.get('http://thecatapi.com/api/images/get?format=src')
    url = r.url
    bot.send_photo(message.chat.id, url, caption='Лови милашку' )
    
@bot.message_handler()
def get_user_text(message):
    if message.text == 'hello' or message.text =='Привет' or message.text =='Здарова' or message.text == 'привет' or message.text == 'здарова':
        bot.send_message(message.chat.id, f'Ещё раз привет,<u>Чтобы ознакомиться с правилами бота нажми /help , Иначе ты нубик!!!!</u>',parse_mode='html')
    else:
        bot.send_message(message.chat.id, 'Ну ты и нубик, напиши /help, а то я не понимаю', parse_mode='html')

bot.polling(none_stop=True)