import os
import csv
import psycopg2
from dotenv import load_dotenv
from tqdm import tqdm 

load_dotenv()
conn_str = os.getenv('DATABASE_URL')
conn = None
progress_bar = tqdm(total=210594)

def create_access_csv(file_path, data_path):
    with open(file_path, mode='w', newline='', encoding='utf-8') as output_file, \
        open(data_path, mode='r', encoding='utf-8') as input_file:
        reader = input_file.readlines()
        for line in reader:
            if line[0] != ':': # 'P' is for the "Power Outage variable" to avoid empty log lines >> check for end cases
                writer = csv.writer(output_file)
                data = str.split(line)
                writer.writerow([data[0], data[1], data[2][1:], data[3][1:-1],' '.join(data[4:])])
                # attacking_ip, target_ip, timestamp, timezone, attack
    print(">> Access log formatted to CSV <<")


def upload_to_db(access_path):
    print(">> Connecting to database <<")
    try:
        with psycopg2.connect(conn_str) as conn:
            print("Connection established")
            # need to create properly formated data to allow to go into database
            # timestamp, timezone, attacking_ip, target_ip
            with conn.cursor() as cur:
                cur.execute("DROP TABLE IF EXISTS accesslog")
                cur.execute("""
                    CREATE TABLE accesslog (
                        id SERIAL PRIMARY KEY,
                        attacking_ip TEXT NOT NULL,
                        target_ip TEXT DEFAULT '',
                        timestmp TEXT NOT NULL DEFAULT NOW(),
                        timezone TEXT DEFAULT '0500',
                        attack TEXT DEFAULT ''
                        );
                """)
                print("Table created, inserting data...")
                # Insert data line by line manually
                with open(access_path, mode='r', newline='', encoding='utf-8') as access_file:
                    for row in csv.reader(access_file):
                        cur.execute("""
                                insert into accesslog (attacking_ip, target_ip, timestmp, timezone, attack) values (%s, %s, %s, %s, %s); """,
                                (row[0], row[1], row[2], row[3], row[4])
                            )
                        progress_bar.update(1)
            print(">> Data uploaded to database <<")
    except Exception as e:
        print('Connection failed')
        print(e)

def log_to_db(access_path, access_log):
    # access_path = data\access.log
    # access_log = data\access.csv
    create_access_csv(access_path, access_log)
    # now that it is formatted, it can be uploaded to the database and analyzed
    upload_to_db(access_path)