import telebot

bot = telebot.TeleBot("835459204:AAGgwapMBDD3iX1zM3GvoEFd_WHpqKAhGKE")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	bot.send_message(message.chat.id, "Елена, пиздуйте учить экзамен, пожалуйста!")

bot.polling( none_stop = True )