import telebot
import gdshortener
import requests
from user_agent import generate_user_agent
import re
import random

bot = telebot.TeleBot("6532286475:AAFIjc53deB8e03_jZRxmpEjuS2ppYGJd2Q")
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

@bot.message_handler(func=lambda message: message.text == "/start" or "السورس")
def send_source(message):
    url = 'https://t.me/my00002/235' 
    chat_id = message.chat.id
    bot.send_photo(chat_id=chat_id, photo=url, caption="")

    keyboard = InlineKeyboardMarkup(row_width=1)
    channel_button = InlineKeyboardButton("قناة السورس", url="http://t.me/my00002")
    developer_button = InlineKeyboardButton("مطور السورس", url="http://t.me/altaee_z")
    share_button = InlineKeyboardButton("مشاركة البوت 🤖", switch_inline_query="") 
    keyboard.add(channel_button, developer_button, share_button)
                                                      #هنا غير الرساله بس لتشيل ال""
    bot.reply_to(message, """
    اهلا وسهلا بكم {}
    ✓ لمرفة تاريخ اليوم بالتقويم الهجري والميلادي ارسل /today
    ✓ لأختصار الروابط ارسل /link 
    ✓ لمعرفة نوع السيارة ارسل الصورة فقط .
    ✓ لمعرفة تاريخ انشاء حسابك ارسل الايدي خاص بك فقط .
    ♡ شكرا لكم لأستخدام البوت 
    """
    
    
    
    , reply_markup=keyboard) 

#بوت today
import telebot
import datetime
from hijri_converter import convert

@bot.message_handler(commands=['today'])
def send_date(message):
    today = datetime.date.today()
    hijri_date = convert.Gregorian(today.year, today.month, today.day).to_hijri()
    response = f"التاريخ الهجري: {hijri_date}\nالتاريخ الميلادي: {today}"
    bot.reply_to(message, response)


############اختصار الرابط
cookies = {
    'AppSession': '6j35pliejibipiidgqr4kueuv1',
    'csrfToken': '75aa4558310672a8042cc16fcbcdffd5477b8d9c9bf46f91e401c5a532675602c645e04878c56f8ea172da3e837c27734014460b3b55dc1bbce8277162ada3c8',
    'sls': '0',
    'tmz': 'Asia/Jerusalem',
    'ref': 'admin',
    'ab': '2',
    '_ga_6QVVMFTPT3': 'GS1.1.1687605103.1.0.1687605103.0.0.0',
    '_ga': 'GA1.1.1737572540.1687605104',
}

headers = {
    'authority': 'za.gl',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://za.gl',
    'referer': 'https://za.gl/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': generate_user_agent(),
    'x-requested-with': 'XMLHttpRequest',
}

@bot.message_handler(commands=['link'])
def Welcome(message):
 name = message.from_user.first_name
 keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
 keyboard.add(
        telebot.types.InlineKeyboardButton(text='is.gd', callback_data='1'),

    )
    
 bot.reply_to(message,'''مرحبا {}
 اضغط على الزر ادناه ....↓ '''.format(name),reply_markup=keyboard)
 
@bot.callback_query_handler(func=lambda call:True)
def all(call):
 if call.data == '1':
  bot.send_message(call.message.chat.id,'ارسل الرابط لأقوم بأختصار بدومين is.gd')
  bot.register_next_step_handler(call.message, one)
def one(message):
 if re.search("(?P<url>https?://[^\s]+)", message.text):
  s = gdshortener.ISGDShortener()
  a = s.shorten(message.text)[0]
  b = """
  🦋تم بواسطة بوت @Ebdhhdbot 
⚡️قناة المطور : @my00002"""
  bot.reply_to(message,a)
  bot.reply_to(message,b)
  
 else:
  bot.reply_to(message,'sorry ,This is not a link URL')
 
def two(message):
 global cookies
 global headers
 
 data = {
 '_method': 'POST',
 '_csrfToken': '75aa4558310672a8042cc16fcbcdffd5477b8d9c9bf46f91e401c5a532675602c645e04878c56f8ea172da3e837c27734014460b3b55dc1bbce8277162ada3c8',
 'url': message.text,
 'ad_type': '2',
 '_Token[fields]': 'fba2ac211af3a04684cf7ffe3e6afdc452d7f50f%3Aad_type',
 '_Token[unlocked]': 'adcopy_challenge%7Cadcopy_response%7Ccoinhive-captcha-token%7Cg-recaptcha-response',
 }
 response = requests.post('https://za.gl/links/shorten',cookies=cookies,headers=headers, data=data).json()['url']
 if re.search("(?P<url>https?://[^\s]+)", message.text):
    bot.reply_to(message,response)
 else:
  bot.reply_to(message, "sorry ,This is not a link URL")
#####تاريخ انشاء حسابك
headers = {
    'Host': 'restore-access.indream.app',
    'Connection': 'keep-alive',
    'x-api-key': 'e758fb28-79be-4d1c-af6b-066633ded128',
    'Accept': '*/*',
    'Accept-Language': 'ar',
    'Content-Length': '25',
    'User-Agent': 'Nicegram/101 CFNetwork/1404.0.5 Darwin/22.3.0',
    'Content-Type': 'application/x-www-form-urlencoded',
}
@bot.message_handler(func=lambda message: True)
def t7(message):
    data = '{"telegramId":' + str(message.text) + '}'
    response = requests.post('https://restore-access.indream.app/regdate', headers=headers, data=data).json()
    date = response['data']['date']
    if date:
        mej = f"~ الايدي {message.text}\n ~ تاريخ انشاء الحساب {date}"
        bot.reply_to(message, mej)
####التعرف على السيارة
from telebot.types import InlineKeyboardButton as Btn , InlineKeyboardMarkup as Mak
def car(info):
    
    url = "https://carnet.ai/recognize-url"
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://carnet.ai',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    
    data = info
    
    response = requests.post(url,headers=headers, data=data)
    
    return response.json()
    
@bot.message_handler(content_types=['photo'])
def BMW(msg):
 file_id = msg.photo[-1].file_id
 file_info = bot.get_file(file_id)
 file_url = f"https://api.telegram.org/file/bot{bot.token}/{file_info.file_path}"
 info = file_url
 xcar = car(info)
 if 'error' in xcar:
 	bot.reply_to(msg,'لم اتعرف على السيارة!')
 else:
 	carname = xcar['car']['make']
 	carmodel = xcar['car']['model']
 	years = xcar['car']['years']
 	angel = xcar['angle']['name']
 	color = xcar['color']['name']
 	xx = f'''تم التعرف على السيارة 🚧
. مصنع السيارة: {carname} .
. سنة اصدار السيارة: {years} .
. لون السيارة: {color} .
. زاوية تصوير السيارة : {angel} .
. اسم السيارة (موديلها) : {carmodel} .
⎯ ⎯ ⎯ ⎯'''
 	bot.reply_to(msg,xx)
####
print("run")
bot.polling()
