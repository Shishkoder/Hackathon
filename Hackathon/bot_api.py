import datetime

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import telebot

from parser import parse_schedule, get_classroom

# Константы
API_KEY = '5137893848:AAH0K5bzz8l6KYzXD9APzvsg-E8VcGqKSEs'

now = datetime.datetime.today()
next_day_to_update = datetime.timedelta(seconds=10)
day_update = now + next_day_to_update
print(now, next_day_to_update, day_update, sep='\n')
bot = telebot.TeleBot(API_KEY)


# # Отправка запроса на парсинг к скрипту (Используется модуль Schedule
# def send_activation():
#     parse_schedule()


# every().sunday.at("00:00").do(send_activation())
#
# while True:
#     run_pending()
while True:
    if datetime.datetime.today() > day_update:
        parse_schedule()
        now = datetime.datetime.today()
        next_day_to_update = datetime.timedelta(seconds=10)
        day_update = now + next_day_to_update
        print(now, next_day_to_update, day_update, sep='\n')

    All_id = [None, None, None]


    def gen_markup():
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("пн", callback_data="cb_1"),
                   InlineKeyboardButton("вт", callback_data="cb_2"), InlineKeyboardButton("ср", callback_data="cb_3"),
                   InlineKeyboardButton("чт", callback_data="cb_4"), InlineKeyboardButton("пт", callback_data="cb_5"),
                   InlineKeyboardButton("сб", callback_data="cb_6"))
        return markup


    def gen_markup_DNI():
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("Здание_1", callback_data="cb_1_1"),
                   InlineKeyboardButton("Здание_2", callback_data="cb_2_2"),
                   InlineKeyboardButton("Здание_3", callback_data="cb_3_3"),
                   InlineKeyboardButton("Здание_4", callback_data="cb_4_4"),
                   InlineKeyboardButton("Здание_5", callback_data="cb_5_5"),
                   InlineKeyboardButton("Здание_6", callback_data="cb_6_6"),
                   InlineKeyboardButton("Здание_7", callback_data="cb_7_7"),
                   InlineKeyboardButton("Здание_8", callback_data="cb_8_8"),
                   InlineKeyboardButton("КСК КАИ ОЛИМП", callback_data="cb_0_0"),
                   InlineKeyboardButton("Вернуться", callback_data="cb_reset"))
        return markup


    @bot.callback_query_handler(func=lambda call: True)
    def callback_query(call):
        try:
            if call.message:
                if call.data == "cb_1":
                    All_id[1] = "1"

                    bot.send_message(call.message.chat.id, 'Выберете здание.', reply_markup=gen_markup_DNI())

                elif call.data == "cb_2":
                    All_id[1] = "2"
                    bot.send_message(call.message.chat.id, 'Выберете здание.', reply_markup=gen_markup_DNI())

                elif call.data == "cb_3":
                    All_id[1] = "3"
                    bot.send_message(call.message.chat.id, 'Выберете здание.', reply_markup=gen_markup_DNI())

                elif call.data == "cb_4":
                    All_id[1] = "4"
                    bot.send_message(call.message.chat.id, 'Выберете здание.', reply_markup=gen_markup_DNI())
                elif call.data == "cb_5":
                    All_id[1] = "5"
                    bot.send_message(call.message.chat.id, 'Выберете здание.', reply_markup=gen_markup_DNI())
                elif call.data == "cb_6":
                    All_id[1] = "6"
                    bot.send_message(call.message.chat.id, 'Выберете здание.', reply_markup=gen_markup_DNI())

                elif call.data == "cb_1_1":
                    All_id[2] = "1"
                    bot.send_message(call.message.chat.id,
                                     get_classroom(week_number=All_id[1], build_number=All_id[2], classroom=All_id[0]))

                elif call.data == "cb_2_2":
                    All_id[2] = "2"
                    bot.send_message(call.message.chat.id,
                                     get_classroom(week_number=All_id[1], build_number=All_id[2], classroom=All_id[0]))
                    # print(All_id)
                elif call.data == "cb_3_3":
                    All_id[2] = "3"
                    bot.send_message(call.message.chat.id,
                                     get_classroom(week_number=All_id[1], build_number=All_id[2], classroom=All_id[0]))
                elif call.data == "cb_4_4":
                    All_id[2] = "4"
                    bot.send_message(call.message.chat.id,
                                     get_classroom(week_number=All_id[1], build_number=All_id[2], classroom=All_id[0]))
                elif call.data == "cb_5_5":
                    All_id[2] = "5"
                    bot.send_message(call.message.chat.id,
                                     get_classroom(week_number=All_id[1], build_number=All_id[2], classroom=All_id[0]))
                elif call.data == "cb_6_6":
                    All_id[2] = "6"
                    bot.send_message(call.message.chat.id,
                                     get_classroom(week_number=All_id[1], build_number=All_id[2], classroom=All_id[0]))
                elif call.data == "cb_7_7":
                    All_id[2] = "7"
                    bot.send_message(call.message.chat.id,
                                     get_classroom(week_number=All_id[1], build_number=All_id[2], classroom=All_id[0]))

                elif call.data == "cb_8_8":
                    All_id[2] = "8"
                    bot.send_message(call.message.chat.id,
                                     get_classroom(week_number=All_id[1], build_number=All_id[2], classroom=All_id[0]))
                elif call.data == "cb_0_0":
                    All_id[2] = "КСК КАИ ОЛИМП"
                    All_id[0] = "КСК КАИ ОЛИМП"
                    bot.send_message(call.message.chat.id,
                                     get_classroom(week_number=All_id[1], build_number=All_id[2], classroom=All_id[0]))
                elif call.data == "cb_reset":
                    All_id[1] = None
                    bot.send_message(call.message.chat.id, 'Выберете день.', reply_markup=gen_markup())
                # if All_id:
                #     bot.send_message(call.message.chat.id,
                #                      get_classroom(week_number=All_id[2], build_number=All_id[1], classroom=All_id[0]))
        except:
            resultats = get_classroom(week_number=All_id[1], build_number=All_id[2], classroom=All_id[0])
            for x in range(0, len(resultats), 4096):
                    bot.send_message(call.message.chat.id, resultats[x:x + 4096])


    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, f'Здравствуйте, <strong>{message.from_user.first_name}</strong>, напишите пожалуйста номер аудитории', parse_mode='html')


    @bot.message_handler(func=lambda message: True)
    def message_handler(message):
        All_id[0] = message.text
        bot.send_message(message.chat.id, "Выберете день", reply_markup=gen_markup())


    bot.polling(none_stop=True)
