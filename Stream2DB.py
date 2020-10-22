import requests
import json
import mysql.connector

def start_Stream2DB():
    print("fetching data from 8080 stream and inject deals into databse")
    with requests.get('http://localhost:8080/streamTest', stream=True) as r1:
        for line in r1.iter_lines(chunk_size=1):
            if line:
                deal = json.loads(line.decode())
                # print(deal)
                instrument_name = deal['instrumentName']
                counterparty_name = deal['cpty']
                price = round(deal['price'],2)
                deal_type = deal['type']
                quantity = deal['quantity']
                time = deal['time']
                # print((price, deal_type,quantity, time))

                # connect to SQL server
                cnx = mysql.connector.connect(user='root', password='ppp', host='127.0.0.1',
                                              database='db_grad_cs_1917')
                cursor1 = cnx.cursor(buffered=True)
                # instruemnt: check if exist: get id or insert
                # instrument_name = '13:01'
                query = ("SELECT instrument_id FROM instrument WHERE instrument_name='" + instrument_name + "'")
                # print(query)
                cursor1.execute(query)
                response = cursor1.fetchone()
                if response:
                    instrument_id = response[0]
                    # print('instrument found: id = ' + str(instrument_id))
                else:
                    # insert new instrument
                    # print('instrument not found: ' + instrument_name)
                    query = ("SELECT MAX(instrument_id) FROM instrument")
                    cursor1.execute(query)
                    instrument_id = cursor1.fetchone()[0] + 1
                    # print(instrument_id)
                    query = ("INSERT INTO instrument (instrument_id, instrument_name) VALUES ("
                             + str(instrument_id) + ", '" + instrument_name + "' ) ")
                    # print(query)
                    cursor1.execute(query)
                    cnx.commit()
                cursor1.close()
                # end of handling instrument

                # counterparty: check if exist: get id or insert
                # counterparty_name = 'james'
                cursor2 = cnx.cursor()
                query = ("SELECT counterparty_id FROM counterparty WHERE counterparty_name='" + counterparty_name + "'")
                # print(query)
                cursor2.execute(query)
                response = cursor2.fetchone()
                if response:
                    counterparty_id = response[0]
                    # print('counterparty found: id = ' + str(counterparty_id))
                else:
                    # insert new counterparty
                    # print('counterparty not found: ' + counterparty_name)
                    query = ("SELECT MAX(counterparty_id) FROM counterparty")
                    cursor2.execute(query)
                    counterparty_id = cursor2.fetchone()[0] + 1
                    query = ("INSERT INTO counterparty (counterparty_id, counterparty_name) VALUES ("
                             + str(counterparty_id) + ", '" + counterparty_name + "' ) ")
                    # print(query)
                    cursor2.execute(query)
                    cnx.commit()
                cursor2.close()
                # end of handling cpty

                # print((price, deal_type,quantity, time))
                cursor3 = cnx.cursor()
                query = ("SELECT MAX(deal_id) FROM deal")
                cursor3.execute(query)
                deal_id = cursor3.fetchone()[0] + 1
                # print('deal_id: ' + str(deal_id))
                query = ("INSERT INTO deal " +
                         "(deal_id, deal_amount, deal_type, deal_quantity, deal_time, " +
                         "deal_counterparty_id, deal_instrument_id) " +
                         " VALUES (" + str(deal_id) + ", "+ str(price) + ", '" + deal_type + "', "
                         + str(quantity) + ", '" + time + "', " + str(counterparty_id) + ", "
                         + str(instrument_id) +") ")
                # print(query)
                # print(type(time))
                cursor3.execute(query)
                cnx.commit()
                cursor3.close()
                # end of handling deal data

                # break

if __name__ == '__main__':
     start_Stream2DB()

