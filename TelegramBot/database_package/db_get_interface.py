from database_package import database as db


def get_chat_id(value_p,finder):
    value=str(value_p)
    query="SELECT chat_id from mishabot WHERE "+finder+" = '"+value+"';"
    return db.Execute(query)


def get_number(value_p,finder="chat_id"):
    value = str(value_p)
    query = "SELECT number from mishabot WHERE " + finder + " = '" + value + "';"
    return db.Execute(query)


def get_lasttext(value_p,finder="chat_id"):
    value = str(value_p)
    query = "SELECT lasttext from mishabot WHERE " + finder + " = '" + value + "';"
    return db.Execute(query)


def get_googleforms(value_p,finder="chat_id"):
    value = str(value_p)
    query = "SELECT googleforms from mishabot WHERE " + finder + " = '" + value + "';"
    return db.Execute(query)


def get_diete(value_p,finder="chat_id"):
    value = str(value_p)
    query = "SELECT diete from mishabot WHERE " + finder + " = '" + value + "';"
    return db.Execute(query)


def get_date(value_p,finder="chat_id"):
    value = str(value_p)
    query = "SELECT date from mishabot WHERE " + finder + " = '" + value + "';"
    return db.Execute(query)


def get_approved(value_p,finder="chat_id"):
    value = str(value_p)
    query = "SELECT approved from mishabot WHERE " + finder + " = '" + value + "';"
    print(query)
    k= db.Execute(query)=="yes"
    print(k)
    return k


def get_payment(value_p,finder="chat_id"):
    value = str(value_p)
    query = "SELECT payment from mishabot WHERE " + finder + " = '" + value + "';"
    return db.Execute(query)


def get_exception(value_p,finder="chat_id"):
    value = str(value_p)
    query = "SELECT exception from mishabot WHERE " + finder + " = '" + value + "';"
    return db.Execute(query)


def get_plus(value_p,finder="chat_id"):
    value = str(value_p)
    query = "SELECT plus from mishabot WHERE " + finder + " = '" + value + "';"
    return db.Execute(query)


def get_balance(value_p, finder="chat_id"):
    query = f"SELECT balance FROM mishabot WHERE {finder} = '{str(value_p)}'"
    return db.Execute(query)


def get_tariff(value_p, finder="chat_id"):
    query = f" SELECT tariff FROM mishabot WHERE {finder} = '{str(value_p)}'"
    return db.Execute(query)