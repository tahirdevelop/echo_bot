import telebot
import config

bot = telebot.TeleBot(config.TELEGRAM_TOKEN)


@bot.message_handler(content_types=["text"])
def reply_message(message):
    bot.send_message(chat_id=message.from_user.id, text=message.text)


@bot.message_handler(content_types=['photo'])
def reply_photo(message):
    bot.send_photo(chat_id=message.from_user.id, photo=message.photo[2].file_id)


@bot.message_handler(content_types=['video'])
def reply_video(message):
    bot.send_video(chat_id=message.from_user.id, data=message.video.file_id)


@bot.message_handler(content_types=['audio'])
def reply_audi(message):
    bot.send_audio(chat_id=message.from_user.id, audio=message.audio.file_id)


@bot.message_handler(content_types=['sticker'])
def reply_sticker(message):
    bot.send_sticker(chat_id=message.from_user.id, data=message.sticker.file_id)


@bot.message_handler(content_types=['document'])
def reply_document(message):
    bot.send_document(chat_id=message.from_user.id, data=message.document.file_id)


if __name__ == '__main__':
    bot.polling(none_stop=True)
