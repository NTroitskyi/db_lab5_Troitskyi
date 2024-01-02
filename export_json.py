import psycopg2
import json

username = 'postgres'
password = ''
database = 'jojo'
host = 'localhost'
port = '5433'

sql_query = '''
SELECT
  STAND_USER.user_name AS Name,
  PART.part_num AS Part,
  STAND.stand_name AS Stand,
  STAND.PWR,
  STAND.SPD,
  STAND.RNG,
  STAND.PER,
  STAND.PRC,
  STAND.DEV
FROM
  STAND_USER
JOIN
  STAND ON STAND_USER.id_stand = STAND.id_stand
JOIN
  PART ON STAND_USER.id_part = PART.id_part;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn.cursor() as cursor:
    cursor.execute(sql_query)
    results = cursor.fetchall()

json_file_path = 'output.json'

data_list = []
columns = ['Name', 'Part', 'Stand', 'PWR', 'SPD', 'RNG', 'PER', 'PRC', 'DEV']
for row in results:
    data_list.append(dict(zip(columns, row)))

with open(json_file_path, 'w') as json_file:
    json.dump(data_list, json_file, indent=2)

print(f'Data has been exported to {json_file_path}')