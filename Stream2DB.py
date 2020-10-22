import requests
import json
import mysql.connector

# connect to SQL server
cnx=mysql.connector.connect(user='root',password='ppp', host='127.0.0.1', database='db_grad_cs_1917')

cursor1 = cnx.cursor()
r = requests.get('http://localhost:8080/testservice')
if r.status_code == 200:
    response_json = r.json() #
    # print(r.json())
    instrument_name=response_json['instrumentName']
    # instrument_name = 'Celestial1115'

    # check if this instrument exist
    query = ("SELECT instrument_id FROM instrument WHERE instrument_name='" + instrument_name + "'")
    print(query)
    cursor1.execute(query)
    response = cursor1.fetchone()
    if response:
            instrument_id = response[0]
            print('instrument found: id = '+str(instrument_id))
    else:
        #insert new instrument
        print('instrument not found: ' + instrument_name)
        query = ("SELECT MAX(instrument_id) FROM instrument")
        cursor1.execute(query)
        instrument_id = cursor1.fetchone()[0]+1
        print(instrument_id)
        query= ("INSERT INTO instrument (instrument_id, instrument_name) VALUES ("
                + str(instrument_id) + ", '" +instrument_name+ "' ) ")
        print(query)
        cursor1.execute(query)
        cnx.commit()

else:
    print('fail to get a response')