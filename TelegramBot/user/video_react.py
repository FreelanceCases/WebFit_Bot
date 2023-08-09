import database_package.db_get_interface as dgi
import additional.info as i
import functional_package.additional_to_marking as add_to_mark
import additional.markup as m
import database_package.db_set_interface as dsi
import functional_package.dbforuser as dbforuser
import pathlib
from pathlib import Path


def video_checker(message,bot):
    chat_id = str(message.chat.id)
    lasttext = str(dgi.get_lasttext(chat_id))
    plus = str(dgi.get_plus(chat_id)).split("_")
    k=int(add_to_mark.get_numerate(lasttext,dgi.get_number(chat_id)))
    print(message.json["video"])
    ex = "." + message.json['video']['mime_type'].split("/")[-1]
    exv=0
    text="n"
    if (len(plus)==2):
        text = dbforuser.Distributer(lasttext, str(message.chat.id), dgi.get_number(chat_id))
        if text=="Упражнение выполнено":
            exv=k
        else:
            exv=int(text.split('\n')[0][-1])-1
        print(exv)
        dir_path = pathlib.Path.cwd()

        # Объединяем полученную строку с недостающими частями пути
        path = Path(dir_path, "Trainings", "TrainingsVideos")
        file_name = str(path) + "/" + str(dgi.get_number(chat_id)) + "_" + str(lasttext).replace(" ", "") \
                    + "_ex_" + str(exv) + str("_plus_") + plus[0] + ex
        print('CHECK', file_name)
        file_info = bot.get_file(message.video.file_id)
        display = text

        with open(file_name, "wb") as f:
            file_content = bot.download_file(file_info.file_path)
            f.write(file_content)
        if text== "Упражнение выполнено":
            dsi.set_plus("null", chat_id)
            bot.send_message(message.chat.id, "Упражнение выполнено", reply_markup=m.menu_markup())
        else:
            if dgi.get_plus(chat_id) != "plusrequired":
                dsi.set_plus("required", chat_id)
            bot.send_message(message.chat.id, display, reply_markup=m.supply_markup())
