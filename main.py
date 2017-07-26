#-*- coding: utf-8 -*-
import telebot
import constantsss
import dialogs
import os
import random
bot = telebot.TeleBot(constantsss.token)

print(bot.get_me())

@bot.message_handler(content_types=["text"])

def reply_message(message):

    if ", а?"  in message.text.lower():
            answer = "хуй на"
            (message, answer)
            bot.send_message(message.chat.id,answer)
    elif ",а?"  in message.text.lower():
            answer = "хуй на"
            (message, answer)
            bot.send_message(message.chat.id,answer)
    elif "пиздуль" in message.text.lower():
        bot.send_sticker(message.chat.id, constantsss.template_sticker_idpizd)
    elif "я русский" in message.text.lower():
        bot.reply_to(message,  random.choice(dialogs.but))
    elif "!чашка" in message.text.lower():
        bot.reply_to(message, random.choice(dialogs.chuska))
    elif ",рейт" in message.text.lower():
        bot.reply_to(message, random.choice(dialogs.reit))
    elif ", рейт" in message.text.lower():
        bot.reply_to(message, random.choice(dialogs.reit))
    elif "рейт ми" in message.text.lower():
        bot.reply_to(message, random.choice(dialogs.reit))
    elif " рейт" in message.text.lower():
        bot.reply_to(message, random.choice(dialogs.reit))
    elif "Рейт " in message.text.title():
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
    elif "!хелп" in message.text.lower():
       bot.reply_to(message, random.choice(dialogs.coms))
    elif "андрей"  in message.text.lower():
        bot.send_sticker(message.chat.id, constantsss.template_sticker_idandr)
    elif "стрида" in message.text.lower():
        bot.reply_to(message, random.choice(dialogs.str))
    elif "ежжи" in message.text.lower():
        bot.send_sticker(message.chat.id, constantsss.template_sticker_idejje)
    elif "фишер-пидор" in message.text.lower():
        bot.send_sticker(message.chat.id, constantsss.template_sticker_idfish)
    elif "пидора ответ" in message.text.lower():
        bot.reply_to(message,  random.choice(dialogs.pidor))
    elif "я видел" in message.text.lower():
        bot.send_sticker(message.chat.id, constantsss.template_sticker_idvas)
    elif "!рулетка" in message.text.lower():
        bot.reply_to(message,  random.choice(dialogs.russrullet))





















bot.polling(none_stop=True)