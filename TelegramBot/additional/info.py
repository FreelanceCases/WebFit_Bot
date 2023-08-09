from additional import markup as m
from database_package import db_get_interface as dgi

approved_values = ["0", "1", "2", "3", "+"]
def start_text(bot,chat_id):
    bot.send_message(chat_id,"Наберите команду /number, чтобы авторизоваться")

def diete_text(bot,chat_id):
    bot.send_message(chat_id, "Ваша диета: "+dgi.get_diete(chat_id),reply_markup=m.menu_markup())
def info_text(bot,chat_id):
    bot.send_message(chat_id, "Not yet")

def number_text(bot,chat_id):
    bot.send_message(chat_id, 'Отправьте номер телефона для авторизации. Для этого нажмите на кнопку \'Send Phone\'.',reply_markup=m.phone_number_markup())

