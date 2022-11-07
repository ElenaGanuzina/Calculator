import interface as i

from telegram import ReplyKeyboardRemove
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

# Определяем константы этапов разговора
# fld = list(range(1, 10))
# x = chr(10060)
# o = chr(11093)
# count = 9
# player = x
CHOICE_1 = 0
CHOICE_2 = 1
CHOICE_3 = 2
CHOICE_4 = 3


# функция обратного вызова точки входа в разговор
def start(update, _):
    txt = '''Введите
            для работы с рациональными числами: 1
            для работы с комплексными числами: 2
            для выхода: q'''
    update.message.reply_text(txt)
    update.message.reply_text("Ввод: ")
    return CHOICE_1


def choice(update, _):
    # move = update.message.text
    # move = int(move)
    # update.message.reply_text(f"Некорректный ввод{chr(9940)}\nПопробуйте еще раз")
    i.choice_num(update, _)


def cancel(update, _):
    update.message.reply_text('Пока', reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater("TOKEN")
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOICE_1: [MessageHandler(Filters.text & ~Filters.command, choice)],
            CHOICE_2: [MessageHandler(Filters.text & ~Filters.command, i.menu_rat)],
            CHOICE_3: [MessageHandler(Filters.text & ~Filters.command, i.menu_comp)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dispatcher.add_handler(conv_handler)

    print('server start')

    updater.start_polling()
    updater.idle()
