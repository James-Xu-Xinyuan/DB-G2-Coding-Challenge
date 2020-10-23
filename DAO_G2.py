import mysql.connector


def user_auth(username, password):
    cnx = mysql.connector.connect(user='root', password='ppp', host='127.0.0.1', database='db_grad_cs_1917')
    cursor1 = cnx.cursor()
    query = ("SELECT user_pwd FROM users WHERE user_id='" + str(username) + "'")
    cursor1.execute(query)
    response = cursor1.fetchone()

    if response:
        user_pwd = response[0]
        if user_pwd == password:
            cursor1.close()
            cnx.close()
            return True
        else:
            print("invalid username or password")
            cursor1.close()
            cnx.close()
            return False
        # potentially add login record
    else:
        print("invalid username or password")
        cursor1.close()
        cnx.close()
        return False


# get the latest and aggregate deal data for an instrument
def get_instrument_latest_avg(instrument_name):
    cnx = mysql.connector.connect(user='root', password='ppp', host='127.0.0.1', database='db_grad_cs_1917')
    cursor2 = cnx.cursor()
    cursor3 = cnx.cursor()

    query = ("SELECT instrument_id FROM instrument WHERE instrument_name='" + instrument_name + "'")
    cursor2.execute(query)
    response = cursor2.fetchone()
    if response:
        instrument_id = response[0]
        print(instrument_id)
    else:
        cursor2.close()
        cnx.close()
        return "cant find this instrument"

    query = ("SELECT MAX(deal_id) FROM deal ")
    cursor3.execute(query)
    latest_deal_id = cursor3.fetchone()[0] - 100
    print(latest_deal_id)

    query = ("SELECT AVG(deal_amount) FROM deal" + " WHERE deal_type='B' " +
             " AND deal_instrument_id=" + str(instrument_id) + " AND deal_id>" + str(latest_deal_id))
    cursor2.execute(query)
    avg_buy = cursor2.fetchone()[0]
    print(avg_buy)

    query = ("SELECT AVG(deal_amount) FROM deal" + " WHERE deal_type='S' " +
             " AND deal_instrument_id=" + str(instrument_id) + " AND deal_id>" + str(latest_deal_id))
    cursor3.execute(query)
    avg_sell = cursor3.fetchone()[0]
    print(avg_sell)

    cursor2.close()
    cursor3.close()
    cnx.close()
    return (avg_sell, avg_buy)


# get the lastest (approximatly 10 to 20) deals from databse
def get_latest_deals():
    cnx = mysql.connector.connect(user='root', password='ppp', host='127.0.0.1', database='db_grad_cs_1917')
    cursor4 = cnx.cursor()
    cursor5 = cnx.cursor()
    deal_data = []

    query = ("SELECT MAX(deal_id) FROM deal ")
    cursor4.execute(query)
    latest_deal_id = cursor4.fetchone()[0] - 10
    print(latest_deal_id)
    query = ("SELECT * FROM deal WHERE deal_id>" + str(latest_deal_id))
    cursor5.execute(query)
    # how should return data be formated
    for row in cursor5:
        deal_data.append(row)

    cursor4.close()
    cursor5.close()
    cnx.close()
    return deal_data


def insert_test_user():
    cnx = mysql.connector.connect(user='root', password='ppp', host='127.0.0.1', database='db_grad_cs_1917')
    cursor6 = cnx.cursor()
    query = ("INSERT INTO users (user_id, user_pwd)" "VALUES ('hello', 'world')")
    cursor6.execute(query)
    query = ("INSERT INTO users (user_id, user_pwd)" "VALUES ('admin', '123456')")
    cursor6.execute(query)
    query = ("INSERT INTO users (user_id, user_pwd)" "VALUES ('James', '987@Xu')")
    cursor6.execute(query)
    cnx.commit()
    cursor6.close()
    cnx.close()