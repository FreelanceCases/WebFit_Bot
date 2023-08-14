from functional_package import additional_to_marking as ad_to_mark
from database_package import database, db_set_interface
from trainings_checker import is_cell_is_purple


def classical_training(title,weight,execies,colors,lastchar,mobile,chatid,resting):#add
    greeting="Подход № "+str((lastchar+1))+"\n\nВыполните упражнение "+title+" c весом:"+weight+"\nИ отправьте количество запаса\n"\
             "\nВаша цель: "+str(execies[lastchar])+"\n"+is_cell_is_purple(colors[lastchar])+"\n Отдых: "+resting#и здесь
    ad_to_mark.set_exeption_and_finish_ex(execies[int(lastchar)],mobile,str(lastchar+1),title,chatid)
    return greeting


def plus_training(title,execies,colors,lastchar,mobile,chatid,resting):
    text=str(execies[lastchar])+".\nУказать запас\nИ снять видео"
    print(execies[lastchar])
    print(colors[lastchar])
    if(execies[lastchar]<0):
        text="выполнить более "+str(abs(execies[lastchar]))+"\nОтправить новое количество\nИ снять видео"+"\n Отдых: "+resting#и здесь
        db_set_interface.set_plus("plusrequired", chatid)
        print('заменено на plusplusrequired')
    text=title+"\nПодход № "+str(lastchar+1)+'\nВес: '+str(colors[lastchar])+"\nВаша задача: "+text
    ad_to_mark.set_exeption_and_finish_ex(execies[int(lastchar)], mobile, str(lastchar+ 1), title, chatid)
    return text


def Distributer(execise,chatid,number):
    cursor = database.Con()
    SelectAll = "SELECT * FROM " + str("f") + number + " WHERE execises = '" + execise + "'"
    cursor.execute(SelectAll)
    line=cursor.fetchall()[0]
    # rest=line[-1]
    # TODO: EDIT this
    rest="2 минуты"
    # TODO: Надо определиться, будет ли графа отдыха в каждой таблице 
    type=line[-1]
    line=line[0:-1]
    title=line[0]
    weight=line[1]
    execises=ad_to_mark.get_execises_and_colors(line)[0]
    colors=ad_to_mark.get_execises_and_colors(line)[1]
    print(execises)
    print(colors)
    ex_number=ad_to_mark.get_last_ex(execises)
    print(f"ex_number is {ex_number}")

    if ex_number==None or ex_number == len(execises)-1:
        return ad_to_mark.mark_done(cursor,number,execise,chatid)
    else:
        print("type is " + str(type))
        if (type == "c"):
            return classical_training(title,weight,execises,colors,ex_number,number,chatid,rest)
        elif (type == "p"):
            return plus_training(title,execises,colors,int(ex_number),number,chatid,rest)
        elif (type == "h"):
            print("hst")
        else:
            print("I don't know")

