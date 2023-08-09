import requests


# TODO: EDIT 
# standarturl="http://134.0.118.41:3000/"
standarturl="http://127.0.0.1:3000/"


def send_to_google_tables(lasttext,date,googleforms,number,comm,newVal):
    print(f'данные отправлены в тбалицу: {lasttext}, {date}, {googleforms}, {number}, {comm}, {newVal}')
    try:
        requests.post(standarturl+"commentere",
                      json={'ex': lasttext, 'googlesheets': googleforms, 'date': date, "comm": comm,"exnum": number,
                            "newval":newVal})
    except:
        print("Not yet implemented")


def markGoogleEx(lasttext,number,googleforms,date,mestext):
    try:
        print('number isssss')
        print(number)
        requests.post(standarturl+"markex",
                      json={'ex': lasttext, 'googlesheets': googleforms, 'date': date, "exnum":number,"col":mestext})
    except:
        print("Ошибка")
