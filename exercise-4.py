import telebot

TOKEN = '2122450893:AAH8vcDhyBPkIKYvlSdqqTUSH4kpk4Cvrd8'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda m: True)
def send_len(message):
    count = set("EeYyUuIiOoAa")
    count = set.union(count)
    bot.send_message(message.chat.id,
                     'В сообщении {} повторений гласных.'.format(sum(letter in count for letter in message.text)-1))


bot.polling(none_stop=True)
