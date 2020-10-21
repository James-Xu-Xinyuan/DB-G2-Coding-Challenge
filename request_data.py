# this code tests how to get data down from data generator
import requests
import json

r = requests.get('http://localhost:8080/testservice')
if r.status_code == 200:
    response_json = r.json() #
    print(r.json())
    instrument_name=response_json['instrumentName']
    query = ("SELECT instrument_id FROM instrument WHERE instrument_name= %s AND instrument_id NOT NULL")

else:
    print('fail to get a response')

# r1 = requests.get('http://localhost:8080/streamTest', stream=True)
# def eventStream():
#     for line in r.iter_lines(chunk_size=1):
#         if line:
#             yield 'data:{}\n\n'.format(line.decode())
# return Response(eventStream(), mimetype="text/event-stream")

with requests.get('http://localhost:8080/streamTest', stream=True) as r1:
    for line in r1.iter_lines(chunk_size=1):
        if line:
            # print(type(line))
            # print(type(line.decode()))
            deal = json.loads(line.decode())
            # print(x['cpty'])
            break

cnx=mysql.connector.connect(user='root',password='ppp', host='127.0.0.1', database='db_grad_cs_1917')
cursor = cnx.cursor()
query=("SELECT * FROM deal LIMIT 1")
cursor.execute(query)
for row in cursor:
    print(row)

