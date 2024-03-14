"""
by means of @DF_GD_D
Channel : @T62RS
""" 
import telebot  #مكتبة

private = "6436588079:AAFUS6vefmPvMX6VYyQQEJfQIL2iOsD3Cro"#توكنك
bot = telebot.TeleBot(private)
is_bot_active = True #التشغيل 
bot.set_my_commands([telebot.types.BotCommand("/start", " 🤖 𝗦𝗧𝗔𝗥𝗧 𝗕𝗢𝗧 ")]) 
#الكوماند
@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message,f"""
    🌺 مرحباً بك عزيزي في بوت قراءة الملفات بصيغة ( txt ) وارسال النص في البوت الرجاء ارسال الملف للقراءة ✍ 📨

*البوت لا يدعم ملفات PDF
قناة التحديثات : @my00002
""")
    
@bot.message_handler(content_types=["document"])
def handle_document(message):
   file_info = bot.get_file(message.document.file_id)
   downloaded_file = bot.download_file(file_info.file_path)
   file_name = message.document.file_name
   text = downloaded_file.decode("utf-8")
   bot.reply_to(message, "• النـص داخـل الـمـلف  {} هـو => \n\n {}".format(file_name, text))

print("تم✅") 
bot.polling(none_stop=True)
"""
by means of @re_file_bot
dev : @altaee_z
Channel : @my00002
""" 
