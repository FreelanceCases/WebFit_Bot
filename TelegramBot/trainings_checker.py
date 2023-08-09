from database_package.database import Con
from message_formater import isVideoNeeded


def get_count_of_exercises(title, number):
    query = f"SELECT * FROM f"+number+" WHERE execises = '"+title+"'"
    cursor = Con()
    cursor.execute(query)
    arr = cursor.fetchall()[0][2::]
    counter = 0
    for i in range(len(arr)):
        if arr[i] is not None and i % 2 == 0:
            counter += 1
    return counter



def is_cell_is_purple(color):
    if isVideoNeeded(color) is True:
        t = " СНЯТЬ ВИДЕО "
        return t
    else:
        t = ""
        return t



def TrainAcces(chat_id):
    query = f"SELECT balance FROM mishabot WHERE chat_id='{chat_id}'"
    cursor = Con()
    cursor.execute(query)
    a = cursor.fetchall()[0][0]
    return a > 0



