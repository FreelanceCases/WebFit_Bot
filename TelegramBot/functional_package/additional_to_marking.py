import database_package.database as db


def mark_done(cursor,number,execise,chatid):
    print("Отмечаю полностью выполненное упражнение")
    all_is_finished = True
    cursor.execute(f"UPDATE f{number} SET execises" + " = 'f' " + "WHERE execises = '" + str(execise) + "'")
    SelectAll = "SELECT execises FROM " + str("f") + number
    cursor.execute(SelectAll)
    a = cursor.fetchall()
    d = [x[0] for x in a]
    for name in d:
        if (name != "f"):
            all_is_finished = False
    if all_is_finished == True:
        db.balance_decrement(chatid)
    return "Упражнение выполнено"


def get_execises_and_colors(line):
    execies = []
    colors = []
    for e in range(2, len(line), 2):
        execies.append(line[e])
    for c in range(3, len(line), 2):
        colors.append(line[c])
    execies = [e for e in execies if e != None]
    colors = [c for c in colors]
    return [execies,colors]

def get_last_ex(execies):
    lastchar = None
    for i in range(len(execies) - 1, -1, -1):
        val = execies[i]
        if (val != 0):
            lastchar = i
    if(lastchar==None):
        return None
    print (lastchar)
    return int(lastchar)


def set_exeption_and_finish_ex(value,number,current,title,chatid):
    cursor=db.Con()
    querry = "UPDATE mishabot SET exception = " + str(value) + " WHERE chat_id = '" + str(chatid) + "';"
    cursor.execute(f"UPDATE f{number} SET e" + str(current) + " = " + "0 " + "WHERE execises = '" + title+ "';")
    cursor.execute(querry)


def errorBlake(execise,value, number = "79164009726"):
    try:
        cursor = db.Con()
        SelectAll = "SELECT * FROM " + str("f") + number + " WHERE execises = '" + execise + "'"
        cursor.execute(SelectAll)
        massive = []
        for row in cursor:
            for e in row:
                if (e != None):
                    massive.append(e)
        errfinished = massive.count(0)
        cursor.execute(
            f"UPDATE f{number} SET e" + str(errfinished) + " = " + str(value) + " WHERE execises = '" + execise + "';")
    except:
        print("error")


def get_numerate(execise,number):
    cursor = db.Con()
    SelectAll = "SELECT * FROM " + str("f") + number + " WHERE execises = '" + execise + "'"
    cursor.execute(SelectAll)
    massive = []
    for row in cursor:
        for e in row:
            if (e != None):
                massive.append(e)
    return massive.count(0)