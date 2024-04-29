# import argparse
#
# parser = argparse.ArgumentParser(description="Простое CLI-приложение на Python")
# parser.add_argument("input", help="Введите текст, который вы хотите вывести на экран")
# args = parser.parse_args()
#
# print(args.input)


import sys
import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os
from datetime import datetime

# print("Got args: ", sys.argv)

# a = int(sys.argv[1])
# b = int(sys.argv[2])

a = sys.argv[1]
b = sys.argv[2]

load_dotenv()
db_name = os.getenv("DB_NAME")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

connection = psycopg2.connect(
    host=db_host,
    database=db_name,
    user=db_user,
    password=db_password
)
# print(a, b)

b_date = datetime.strptime(b, '%Y-%m-%d').date()
df = pd.read_sql_query("SELECT * FROM exchange_1fit", connection)
# datetime.strptime(b, '%Y-%d-%m')
value = df[(df['currency'] == a.upper()) & (df['date'] == b_date)]['rate'].iloc[0]
print(value)