import psycopg2
import csv

username = 'postgres'
password = ''
database = 'jojo'
host = 'localhost'
port = '5433'

csv_file_path = "JJBA.csv"

query_delete_stand = '''
DROP TABLE IF EXISTS STAND CASCADE
'''
query_delete_user = '''
DROP TABLE IF EXISTS STAND_USER CASCADE
'''
query_delete_part = '''
DROP TABLE IF EXISTS PART CASCADE
'''
query_stand = '''
CREATE TABLE STAND
(
  id_stand INT GENERATED ALWAYS AS IDENTITY,
  stand_name VARCHAR NOT NULL,
  PWR VARCHAR,
  SPD VARCHAR,
  RNG VARCHAR,
  PER VARCHAR,
  PRC VARCHAR,
  DEV VARCHAR,
  PRIMARY KEY (id_stand)
)
'''
query_user = '''
CREATE TABLE STAND_USER
(
  id_user INT GENERATED ALWAYS AS IDENTITY,
  user_name VARCHAR NOT NULL,
  id_stand INT NOT NULL,
  id_part INT NOT NULL,
  PRIMARY KEY (id_user),
  FOREIGN KEY (id_stand) REFERENCES STAND(id_stand),
  FOREIGN KEY (id_part) REFERENCES PART(id_part)
)
'''
query_part = '''
CREATE TABLE PART
(
  id_part INT GENERATED ALWAYS AS IDENTITY,
  part_num INT NOT NULL,
  PRIMARY KEY (id_part)
)
'''
query_evaluate_stand = '''
INSERT INTO STAND (stand_name, PWR, SPD, RNG, PER, PRC, DEV) VALUES (%s, %s, %s, %s, %s, %s, %s);
'''
query_evaluate_user = '''
INSERT INTO STAND_USER (user_name, id_stand, id_part) VALUES (%s, %s, %s)
'''
query_evaluate_part = '''
DO $$
BEGIN
    FOR i IN 1..8 LOOP
    	INSERT INTO PART (part_num) VALUES (i);
    END LOOP;
END $$;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()
    cur.execute(query_delete_stand)
    cur.execute(query_delete_user)
    cur.execute(query_delete_part)
    cur.execute(query_part)
    cur.execute(query_stand)
    cur.execute(query_user)

    with open(csv_file_path, 'r') as p:
        reader = csv.DictReader(p)
        cur.execute(query_evaluate_part)
        for idx, row in enumerate(reader):
            stand_stats = (row['Stand'], row['PWR'], row['SPD'], row['RNG'], row['PER'], row['PRC'], row['DEV'])
            cur.execute(query_evaluate_stand, stand_stats)
            user_stats = (row['Name'], idx+1 ,row['Part'])
            cur.execute(query_evaluate_user, user_stats)
    
    conn.commit()