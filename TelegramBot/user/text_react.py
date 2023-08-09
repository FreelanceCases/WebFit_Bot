import requests

import additional.markup as m
import additional.net as net
import functional_package.additional_to_marking as add_to_mark
import functional_package.dbforuser as dbforuser
import message_formater as mf
from additional import info as i
from database_package import db_get_interface as dgi, db_set_interface as dsi
from database_package.database import Con
from trainings_checker import TrainAcces
from functional_package.additional_to_marking import get_last_ex



def send_message(message, bot):
    chat_id = message.from_user.id
    if message.text == "/start":
        i.start_text(bot,chat_id)
    elif message.text == "/number":
        i.number_text(bot,chat_id)
    elif message.text == "Информация":
        i.number_text(bot, chat_id)
    elif message.text[1::].isnumeric() and len(message.text[1:]) >= 10:
        bot.send_message(chat_id, text ='Для авторизации, пожалуйста, нажмите на кнопку \'Send phone\'')
    else:
        checkAuth(chat_id,message,bot)



def checkAuth(chat_id, message,bot):
        permission=False
        permission = dgi.get_approved(chat_id)
        if permission:
                listner(chat_id, message, bot)
        else:
                bot.send_message(chat_id, "Вы еще не авторизованы")
def listner(chat_id,message,bot):
    if message.text == "Диета":
         i.diete_text(bot,chat_id)
    elif message.text == "Отчитаться о тренировке":
        list=m.list_markup(dgi.get_number(chat_id))
        if list == None:
            bot.send_message(chat_id,"На эту неделю ваши тренировки закончены :(",reply_markup=m.menu_markup())
        else:
            dsi.set_lasttext("Тренировка",chat_id)
            dsi.set_plus("required",chat_id)
            bot.send_message(chat_id, "Выберете упражнение ", reply_markup=list)

    elif message.text == "Не выполнил заданное число":
        dsi.set_plus(dgi.get_lasttext(chat_id), chat_id)
        dsi.set_lasttext("Не выполнил заданное число значение", chat_id)
        bot.send_message(chat_id, "Пожалуйста, напишите сколько вы выполнили")

    elif (message.text == "Отмена"):
        last_text = dgi.get_lasttext(chat_id)
        dsi.set_plus("null", chat_id)
        if (last_text != 'Тренировка'):
            err = dgi.get_exception(chat_id)
            dsi.set_plus("null", chat_id)
            add_to_mark.errorBlake(last_text, err, dgi.get_number(chat_id))
        dsi.set_lasttext(message.text, chat_id)
        bot.send_message(chat_id, "Отменил", reply_markup=m.menu_markup())
    elif message.text=="Получить тренировку":
        bot.send_message(chat_id, "Одну секунду...")
        resp="Err"
        # try:
        if TrainAcces(chat_id) == True:
            print(net.standarturl+"getTrain/"+dgi.get_googleforms(chat_id)+"/"+dgi.get_number(chat_id));
            res = requests.get(net.standarturl+"getTrain/"+dgi.get_googleforms(chat_id)+"/"+dgi.get_number(chat_id)).text.split(",")
            print(res);
            res1=res[0][2:-1:]
            res2=res[1][1:-2:]
            print(res1+"   and      "+res2)
            bot.send_message(
                chat_id,
                text=mf.training_message(
                    mf.get_training_number(chat_id),
                    mf.training_message_data_formatter_v2(mf.get_training_message_data(number=dgi.get_number(chat_id))),res1,res2),
                reply_markup=m.menu_markup(),
                parse_mode="HTML"
            )
        else:
            bot.send_message(
                chat_id,
                text="Превышен лимит тренировок за неделю",
                reply_markup=m.menu_markup()
            )
        # except:
        #       bot.send_message(chat_id,text=resp,reply_markup=m.menu_markup())
    else:
        Checking_last_message(chat_id,message,bot)

def Checking_last_message(chat_id,message,bot):
    last_text = dgi.get_lasttext(chat_id)
    plus_value = dgi.get_plus(chat_id)
    char=str(message.text)
    query = "SELECT "
    print(f'plus is {dgi.get_plus(chat_id)}')
    if last_text == "Тренировка":
        # try:
        dsi.set_lasttext(message.text, chat_id)
        text = dbforuser.Distributer(message.text, chat_id, dgi.get_number(chat_id), )
        if text=="Упражнение выполнено":
            dsi.set_plus("Null", chat_id)
            bot.send_message(chat_id, text=text, reply_markup=m.menu_markup())
        else:
            ma=m.supply_markup()
            if(dgi.get_plus(chat_id)=="plusrequired"):
                ma=m.cancel_markup()
            bot.send_message(chat_id, text, reply_markup=ma)
        # except:
        #     print("Something Wrong")
        #     dsi.set_lasttext("Отмена", chat_id)
        #     bot.send_message(chat_id, "Либо такого упражнения нет, либо произошла ошибка",reply_markup=i.menu_markup())


    elif (plus_value == "required"):
        number = add_to_mark.get_numerate(dgi.get_lasttext(chat_id), dgi.get_number(chat_id))
        query = f"Select e{number}_color from f{dgi.get_number(chat_id)} where execises = '"+dgi.get_lasttext(chat_id)+"' ;"
        query2=f"Select type from f{dgi.get_number(chat_id)} where execises = '"+dgi.get_lasttext(chat_id)+"' ;"
        query3 = f"Select e{number} from f{dgi.get_number(chat_id)} where execises = '"+dgi.get_lasttext(chat_id)+"' ;"
        print(query)
        cursor = Con()
        cursor.execute(query)
        color = cursor.fetchall()[0][0]
        cursor.execute(query2)
        type=cursor.fetchall()[0][0]
        print(color)
        print(type)

        if (color != None and color == 7) or type=="p":
            if (char in i.approved_values) or type=="p":
                print(char)
                dsi.set_plus(char + "_required", chat_id)
                bot.send_message(chat_id, "Отправьте видео", reply_markup=m.cancel_markup())
            elif char != "Отмена":
                err = dgi.get_exception(chat_id)
                dsi.set_plus("null", chat_id)
                add_to_mark.errorBlake(last_text, err, dgi.get_number(chat_id))
                dsi.set_lasttext(message.text, chat_id)
                bot.send_message(chat_id, "Вы не указали значение из списка", reply_markup=m.menu_markup())
        else:
            if char in i.approved_values:
                print(char)
                ex=dgi.get_lasttext(chat_id)
                net.markGoogleEx(ex, add_to_mark.get_numerate(ex, dgi.get_number(chat_id)), dgi.get_googleforms(chat_id), dgi.get_date(chat_id), message.text)
                text= dbforuser.Distributer(dgi.get_lasttext(chat_id), chat_id, dgi.get_number(chat_id))
                print(f"text issss '{text}'")
                if text == "Упражнение выполнено":
                    dsi.set_plus(chat_id,"null")
                    dsi.set_lasttext(chat_id,"null")
                    bot.send_message(chat_id, text, reply_markup=m.menu_markup())
                else:
                    bot.send_message(chat_id, text)

            elif char != "Отмена":
                err = dgi.get_exception(chat_id)
                dsi.set_plus("null", chat_id)
                add_to_mark.errorBlake(last_text, err, dgi.get_number(chat_id))
                dsi.set_lasttext(message.text, chat_id)
                bot.send_message(chat_id, "Вы не указали значение из списка", reply_markup=m.menu_markup())


    elif dgi.get_lasttext(chat_id) == "Не выполнил заданное число значение":
        number = add_to_mark.get_numerate(dgi.get_plus(chat_id), dgi.get_number(chat_id))
        if (str(message.text).isnumeric()):
            net.send_to_google_tables(dgi.get_plus(chat_id), dgi.get_date(chat_id), dgi.get_googleforms(chat_id),
                                    number, "", str(message.text))
            dsi.set_lasttext("Не выполнил заданное число комментарий", chat_id)
            bot.send_message(chat_id, "Пожалуйста, укажите причину почему вы не смогли сделать это упражнение",
                             reply_markup=m.menu_markup())
        else:
            bot.send_message(chat_id, "Пожалуйста, укажите цифровое значение")

    elif dgi.get_lasttext(chat_id) == "Не выполнил заданное число комментарий":
        number = add_to_mark.get_numerate(dgi.get_plus(chat_id), dgi.get_number(chat_id))
        net.send_to_google_tables(dgi.get_plus(chat_id), dgi.get_date(chat_id), dgi.get_googleforms(chat_id),
                                number, message.text, None)
        dsi.set_plus("null", chat_id)
        dsi.set_lasttext("None", chat_id)
        bot.send_message(chat_id, "Спасибо", reply_markup=m.menu_markup())
    elif dgi.get_plus(chat_id)=="plusrequired" :
        net.send_to_google_tables(dgi.get_lasttext(chat_id),dgi.get_date(chat_id),dgi.get_googleforms(chat_id),add_to_mark.get_numerate(last_text,dgi.get_number(chat_id)),"Пользователь указал столько повторений",message.text)
        dsi.set_plus("1_required",chat_id)
        bot.send_message(chat_id,"Снимите видео")






