from database_package import database as db


def set_chat_id(set_p,value_p,finder):
    set=str(set_p)
    value=str(value_p)
    query = "UPDATE mishabot Set chat_id = '" +set+ "' WHERE " +finder+" = '"+value+"';"
    db.Execute(query,"w")


def set_number(set_p,value_p,finder="chat_id"):
    set = str(set_p)
    value = str(value_p)
    query = "UPDATE mishabot Set number= '" + set + "' WHERE " + finder + " = '" + value + "';"
    db.Execute(query, "w")


def set_lasttext(set_p,value_p,finder="chat_id"):
    set = str(set_p)
    value = str(value_p)
    query = "UPDATE mishabot Set lasttext = '" + set + "' WHERE " + finder + " = '" + value + "';"
    db.Execute(query, "w")


def set_googleforms(set_p,value_p,finder="chat_id"):
    set = str(set_p)
    value = str(value_p)
    query = "UPDATE mishabot Set googleforms = '" + set + "' WHERE " + finder + " = '" + value + "';"
    db.Execute(query, "w")


def set_diete(set_p,value_p,finder="chat_id"):
    set = str(set_p)
    value = str(value_p)
    query = "UPDATE mishabot Set diete = '" + set + "' WHERE " + finder + " = '" + value + "';"
    db.Execute(query, "w")


def set_date(set_p,value_p,finder="chat_id"):
    set = str(set_p)
    value = str(value_p)
    query = "UPDATE mishabot Set date = '" + set + "' WHERE " + finder + " = '" + value + "';"
    db.Execute(query, "w")


def set_approved(set_p,value_p,finder="chat_id"):
    set = str(set_p)
    value = str(value_p)
    query = "UPDATE mishabot Set approved = '" + set + "' WHERE " + finder + " = '" + value + "';"
    db.Execute(query, "w")


def set_payment(set_p,value_p,finder="chat_id"):
    set = str(set_p)
    value = str(value_p)
    query = "UPDATE mishabot Set payment = '" + set + "' WHERE " + finder + " = '" + value + "';"
    db.Execute(query, "w")


def set_exception(set_p,value_p,finder="chat_id"):
    set = str(set_p)
    value = str(value_p)
    query = "UPDATE mishabot Set exception = '" + set + "' WHERE " + finder + " = '" + value + "';"
    db.Execute(query, "w")


def set_plus(set_p,value_p,finder="chat_id"):
    set = str(set_p)
    value = str(value_p)
    query = "UPDATE mishabot Set plus = '" + set + "' WHERE " + finder + " = '" + value + "';"
    db.Execute(query, "w")