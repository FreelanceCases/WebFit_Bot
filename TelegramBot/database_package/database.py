import psycopg2

from additional import parcer as DataFromFile


def Con():
    cred=DataFromFile.read_database_creditians()
    # TODO: EDIT for work with environment
    conn = psycopg2.connect(dbname='webfitness2', user=cred[0][0:-1],password=cred[1][0:-1], host=cred[2])
    conn.autocommit = True
    cursor = conn.cursor()
    # TODO: EDIT this 
    # query = "GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO gen_user"
    # cursor.execute(query)
    return cursor


def Execute(query, type="r"):
    try:
        cursor = Con()
        cursor.execute(query)
        if type=="r":
            return str(cursor.fetchall()[0][0])
        else:
            return "Успех"
    except:
        print("The err in DataBase")
        return "!"


def CreateNewUser(chatid,number):
    if number[0] == "+": number = number[1::]
    querry = "SELECT chat_id FROM mishabot WHERE number = '" + number + "'"
    querry2 = "INSERT INTO mishabot VALUES ('" + chatid + "', '" + number + "', null, null, null, 0,null,null,null,null,2)"
    print('works')
    try:
        cursor=Con()
        print('works')
        cursor.execute(querry)
        print("here")
        size= len(cursor.fetchall())
        if(size>1): return "User is already added"
        elif (size==1): return "User is already registered"
        else:
            print("here")
            cursor.execute(querry2)
            print('ffff')
            create_f_table(number)
            # TODO добавлено создание таблицы f{number}
            return "User Created"
    except:
        return "!"


def balance_decrement(chat_id):
    query = f"UPDATE mishabot SET balance=balance-1 WHERE chat_id='{chat_id}'"
    cursor = Con()
    cursor.execute(query)


def create_f_table(number):
    query = f"CREATE TABLE f{number} " \
            f"( " \
            f"execises text," \
            f"weight   text," \
            f"e1       integer," \
            f"e1_color integer," \
            f"e2       integer," \
            f"e2_color integer," \
            f"    e3       integer," \
            f"e3_color integer," \
            f"e4       integer," \
            f"e4_color integer," \
            f"e5       integer," \
            f"e5_color integer," \
            f"e6       integer," \
            f"e6_color integer," \
            f"e7       integer," \
            f"e7_color integer," \
            f"e8       integer," \
            f"e8_color integer," \
            f"type     char"\
            f")"
    cursor = Con()
    cursor.execute(query)
    c=Con()
    quer ="INSERT INTO f"+str(number)+" VALUES ('f',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null);"
    print(quer)
    c.execute(quer)

