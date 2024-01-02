import psycopg2
import csv


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

csv_file_path = 'output.csv'

with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['Name', 'Part', 'Stand', 'PWR', 'SPD', 'RNG', 'PER', 'PRC', 'DEV'])
    csv_writer.writerows(results)

print(f'Data has been exported to {csv_file_path}')
