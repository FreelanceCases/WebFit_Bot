from database_package import database as DB

# Так, я изначально тут реализовал форматирование сообщение для любых данных
# РУКОВОДСТВО: при выводе сообщения должен быть аргумент parseMode="HTML"
# Сделано это для жирного текста, во всем остальном проблем нет
# Плюсом решилась проблема подходов (При форматировании значения none, просто пропускаются)





numbers_emoji = ('1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟')
max_length = 50


# Сделано для удобства форматирования
class _cycle:
    def __init__(self, number, color):
        self.number = number,
        self.color = color


class exercise:
    def __init__(self, title, weight,t, cycles=[]):
        self.weight = weight,
        self.title = title,
        self.cycles = cycles,
        self.t = t


def isVideoNeeded(color):
    return color is not None and color == 7



def get_training_message_data(number="79164009726"):
    query = f"SELECT * FROM f{number}"
    cursor = DB.Con()
    cursor.execute(query)
    return cursor.fetchall()


def get_training_number(chat_id):
    query = f"SELECT * FROM mishabot WHERE chat_id=\'{chat_id}\'"
    cursor = DB.Con()
    cursor.execute(query)
    arr = cursor.fetchall()
    return arr[0][5]




def training_message_data_formatter_v2(data):
    result = []
    print(data)
    for ex in data:
        result.append(
            exercise(
                title=ex[0],
                weight=ex[1],
                cycles=[
                    _cycle(ex[2], ex[3]),
                    _cycle(ex[4], ex[5]),
                    _cycle(ex[6], ex[7]),
                    _cycle(ex[8], ex[9]),
                    _cycle(ex[10], ex[11]),
                    _cycle(ex[12], ex[13]),
                    _cycle(ex[14], ex[15]),
                    _cycle(ex[16], ex[17]),
                ],
                t=ex[18]
            )
        )
    return result




def training_message(number, exercises, first, last):
    print(first, last)
    result = f"<b>ТРЕНИРОВКА №{str(number)}</b>\n\n"
    # result += str(first).upper() + "\n\n"
    # TODO: EDIT this
    result += "РАЗМИНКА" + "\n\n"
    index = 0
    for ex in exercises:
        if ex.t[0] == 'c':
            if ex.title[0] != 'f':
                result += numbers_emoji[index]
                result += f' <b>{str(ex.title[0]).upper()}</b>\n'
                if ex.weight is not None:
                    result += f'<b>вес - {str(ex.weight[0])} кг</b>\n\n'
                i = 0
                for cycle in ex.cycles[0]:
                    if cycle.number[0] is not None and int(cycle.number[0]) >= 0:
                        if cycle.number[0] is not None:
                            if isVideoNeeded(cycle.color) is False:
                                result += f'{i + 1} подход - {str(cycle.number[0])} повторений \n'
                            else:
                                result += f'{i + 1} подход - {str(cycle.number[0])} повторений  \n<b>СНЯТЬ ВИДЕО</b>\n'
                    else:
                        if cycle.number[0] is not None:
                            if isVideoNeeded(cycle.color) is False:
                                result += f'{i + 1} подход - {str(cycle.number[0])[1::]} + повторений \n'
                            else:
                                result += f'{i + 1} подход - {str(cycle.number[0])[1::]} + повторений  \n<b>СНЯТЬ ВИДЕО</b>\n'
                    i += 1
                result += '\n\n'
        elif ex.t[0] == 'p':
            if ex.title[0] != 'f':
                result += numbers_emoji[index]
                result += f' <b>{str(ex.title[0]).upper()}</b>\n'
                i = 0
                for cycle in ex.cycles[0]:
                    if cycle.number[0] is not None:

                        if cycle.number[0] is not None and int(cycle.number[0]) >= 0:
                            result += f'{i+1} подход - {str(cycle.number[0])} повторений  <b>СНЯТЬ ВИДЕО</b>  \n ' \
                                      f'<b>вес - {str(cycle.color)} кг</b>\n'
                        else:
                            result += f'{i + 1} подход - {str(cycle.number[0])} + повторений  <b>СНЯТЬ ВИДЕО</b>  \n ' \
                                      f'<b>вес - {str(cycle.color)} кг</b>\n'
                        i += 1
                result += '\n\n'
        index += 1
    result += str(last).upper()
    # result = result.replace('\n', '\r\n')
    # output = ""
    # for x in result.split('\r'):
    #     spaces = (max_length - len(x))//2
    #     x = ' '*spaces + x + ' '*spaces
    #     output += x
    # print(output)
    # result = "".join(result)
    return result

