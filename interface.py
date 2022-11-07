import exceptions as e
import rational as r
import complex as c
import logger as l
import main as m

from telegram import ReplyKeyboardRemove
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)


def r_value_1(update, _):
    update.message.reply_text('Введите первое число: ')
    choice = update.message.text
    return choice


def r_value_2(update, _):
    update.message.reply_text('Введите второе число: ')
    choice = update.message.text
    return choice


def c_value_1(update, _):
    update.message.reply_text('Введите действительную часть первого числа: ')
    valid = update.message.text
    update.message.reply_text('Введите мнимую часть первого числа: ')
    imaginary = update.message.text
    return tuple([valid, imaginary])


def c_value_2(update, _):
    update.message.reply_text('Введите действительную часть второго числа: ')
    valid = update.message.text
    update.message.reply_text('Введите мнимую часть второго числа: ')
    imaginary = update.message.text
    return tuple([valid, imaginary])


def sqrt_value(update, _):
    update.message.reply_text('Введите число: ')
    choice = update.message.text
    return choice


def for_rat(choice, update, _):
    if choice == "8":
        num = sqrt_value(update, _)
        if e.check_num(num):
            r.init(eval(num), 0)
            res = r.do_it(choice)
            update.message.reply_text(f"Результат: {res}")
            l.log(num, 0, res, choice)
            m.cancel(update, _)
        else:
            update.message.reply_text("Некорректный ввод\n")
    else:
        num_1 = r_value_1(update, _)
        num_2 = r_value_2(update, _)
        if e.check_num(num_1) and e.check_num(num_2):
            if choice in ['4', '5', '6'] and num_2 == '0':
                update.message.reply_text("На 0 делить нельзя\n")
            else:
                num_1, num_2 = eval(num_1), eval(num_2)
                r.init(num_1, num_2)
                res = r.do_it(choice)
                update.message.reply_text(f"Результат: {res}\n")
                l.log(num_1, num_2, res, choice)
                m.cancel(update, _)
        else:
            update.message.reply_text("Некорректный ввод\n")


def menu_rat(update, _):
    txt = """Введите
        для сложения: 1
        для вычитания: 2
        для умножения: 3
        для обычного деления: 4
        для деления с остатком: 5
        для деления нацело: 6
        для возведения в степень: 7
        для извлечения из квадратного корня: 8
        для выхода: q
        для возврата в предыдущее меню: r"""
    update.message.reply_text(txt)
    update.message.reply_text("Ввод: ")
    choice = update.message.text
    if e.check_rat(choice):
        for_rat(choice, update, _)
    elif e.check_back(choice):
        return
    elif e.check_exit(choice):
        m.cancel(update, _)
    else:
        update.message.reply_text("Некорректный ввод\n")


def for_comp(choice, update, _):
    num_1 = c_value_1(update, _)
    num_2 = c_value_2(update, _)
    if e.check_num(num_1[0]) and e.check_num(num_1[1]) and \
            e.check_num(num_2[0]) and e.check_num(num_2[1]):
        c.init_x(eval(num_1[0]), eval(num_1[1]))
        c.init_y(eval(num_2[0]), eval(num_2[1]))
        res = c.do_it(choice)
        update.message.reply_text(f"Результат: {res}\n")
        l.log(c.x, c.y, res, choice)
        m.cancel(update, _)
    else:
        update.message.reply_text("Некорректный ввод\n")


def menu_comp(update, _):
    txt = """Введите
        для сложения: 1
        для вычитания: 2
        для умножения: 3
        для обычного деления: 4
        для выхода: q
        для возврата в предыдущее меню: r"""
    update.message.reply_text(txt)
    update.message.reply_text("Ввод: ")
    choice = update.message.text
    if e.check_comp(choice):
        for_comp(choice, update, _)
    elif e.check_back(choice):
        return
    elif e.check_exit(choice):
        m.cancel(update, _)
    else:
        update.message.reply_text("Некорректный ввод\n")


def choice_num(update, _):
    choice = update.message.text
    if choice == '1':
        return m.CHOICE_2
    elif choice == '2':
        return m.CHOICE_3
    elif e.check_exit(choice):
        m.cancel(update, _)
    else:
        update.message.reply_text("Некорректный ввод")
        m.start(update, _)
