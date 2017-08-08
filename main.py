#-*- coding: utf-8 -*-
import telebot
import constantsss
import dialogs
import os
import random
from flood_meter import FloodMeter


bot = telebot.TeleBot(constantsss.token)
flood_meter = FloodMeter()


@bot.message_handler(content_types=["text"])
def reply(message):

    flood_meter.check_message()

    commands = {
        u", а?" : (bot.send_message, "хуй на"),
        u",а?" : (bot.send_message, "хуй на"),
        u"пиздуль" : (bot.send_sticker, message.chat.id, constantsss.template_sticker_idpizd),
        u"я русский" : (bot.reply_to, message, random.choice(dialogs.but)),
        u"!чашка" : (bot.reply_to, message, random.choice(dialogs.chuska)),
        u"рейт" : (bot.reply_to, message, random.choice(dialogs.reit)),
        u"харитон" : (bot.reply_to, message, random.choice(dialogs.khar)),
        u"!ролл" : (bot.reply_to, message, random.choice(dialogs.roll)),
        u"двачую" : (bot.reply_to, message, random.choice(dialogs.dvachuy)),
        u"зря" : (bot.reply_to, message, random.choice(dialogs.zrya)),
        u"вася!!!" : (bot.reply_to,message,  random.choice(dialogs.vasya)),
        u"жека!!!" : (bot.reply_to, message, random.choice(dialogs.jek)),
        u"фишер!!!" : (bot.reply_to, message, random.choice(dialogs.fish)),
        u"костя!!!" : (bot.reply_to, message, random.choice(dialogs.kost)),
        u"еее" : (bot.reply_to, message, random.choice(dialogs.eeee)),
        u"плюсики" : (bot.reply_to, message, random.choice(dialogs.plc)),
        u"!хелп" : (bot.reply_to, message, random.choice(dialogs.coms)),
        u"андрей" : (bot.send_sticker, message.chat.id, constantsss.template_sticker_idandr),
        u"стрида" : (bot.reply_to, message, random.choice(dialogs.str)),
        u"ежжи" : (bot.send_sticker, message.chat.id, constantsss.template_sticker_idejje),
        u"фишер-пидор" : (bot.send_sticker, message.chat.id, constantsss.template_sticker_idfish),
        u"пидора ответ" : (bot.reply_to, message, random.choice(dialogs.pidor)),
        u"я видел" : (bot.send_sticker, message.chat.id, constantsss.template_sticker_idvas),
        u"!рулетка" : (bot.reply_to, message, random.choice(dialogs.russrullet)),
        u"mamu" : (bot.reply_to, message, u"ЕБАЛ")
    }

    if flood_meter.flood_rate <= constantsss.flood_limit:
        for i in commands:
            if i in message.text.lower():
                commands[i][0](commands[i][1], commands[i][2])

bot.polling(none_stop=True)
