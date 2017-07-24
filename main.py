import telebot
import constantsss
import dialogs
import os
import random
bot = telebot.TeleBot(constantsss.token)

print(bot.get_me())

@bot.message_handler(content_types=["text"])

def reply_message(message):

    if "а?"  in message.text.lower():
            answer = "хуй на"
            (message, answer)
            bot.send_message(message.chat.id,answer)
    elif "пиздуль" in message.text.lower():
        bot.send_sticker(message.chat.id, constantsss.template_sticker_id)
    elif "!бутылка" in message.text.lower():
        bot.reply_to(message,  random.choice(dialogs.but))
    elif "!чашка" in message.text.lower():
        bot.reply_to(message, random.choice(dialogs.chuska))
    elif "рейт" in message.text.lower():
        bot.reply_to(message, random.choice(dialogs.reit))
    elif "харитон" in message.text.lower():

        bot.reply_to(message, random.choice(dialogs.khar))
    elif "!ролл" in message.text.lower():
        bot.reply_to(message, random.choice(dialogs.roll))
    elif "двачую" in message.text.lower():
       bot.reply_to(message, random.choice(dialogs.dvachuy))
    elif "зря" in message.text.lower():
       bot.reply_to(message, random.choice(dialogs.zrya))
    elif "вася!!!" in message.text.lower():
       bot.reply_to(message, random.choice(dialogs.vasya))
    elif "жека!!!" in message.text.lower():
       bot.reply_to(message, random.choice(dialogs.jek))
    elif "фишер!!!" in message.text.lower():
       bot.reply_to(message, random.choice(dialogs.fish))
    elif "костя!!!" in message.text.lower():
       bot.reply_to(message, random.choice(dialogs.kost))
    elif "еее" in message.text.lower():
       bot.reply_to(message, random.choice(dialogs.eeee))
    elif "плюсики" in message.text.lower():
       bot.reply_to(message, random.choice(dialogs.plc))
    elif "/help_bike" in message.text.lower():
       bot.reply_to(message, random.choice(dialogs.coms))
    elif "андрей"  in message.text.lower():
        bot.send_sticker(message.chat.id, constantsss.template_sticker_id7)
    elif "стрида" and "страйда" in message.text.lower():
        bot.reply_to(message, random.choice(dialogs.str))














bot.polling(none_stop=True)