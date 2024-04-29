import requests
import json
import os
import psycopg2
from datetime import date
from dotenv import load_dotenv


date_now = date.today()

base_url = "https://v6.exchangerate-api.com/v6/b16f5b6c6877b44c1b9e98ee/latest/USD"
params = {
    "access_key": 'b16f5b6c6877b44c1b9e98ee'
}
response = requests.get(url=base_url, params=params)

# print(response.text)

data = json.loads(response.text)

print(data['conversion_rates']['MYR'], data['conversion_rates']['KZT'],  data['conversion_rates']['KGS'],
      data['conversion_rates']['UZS'], data['conversion_rates']['AZN'])

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

cursor = connection.cursor()
insert_query = """INSERT INTO exchange_1fit(date, country_id, currency, rate) VALUES (%s, %s, %s, %s)"""
records_to_insert = [(date_now, 6, 'MYR', data['conversion_rates']['MYR']),
                     (date_now, 1, 'KZT', data['conversion_rates']['KZT']),
                     (date_now, 4, 'KGS', data['conversion_rates']['KGS']),
                     (date_now, 3, 'UZS', data['conversion_rates']['UZS']),
                     (date_now, 5, 'AZN', data['conversion_rates']['AZN']), ]

cursor.executemany(insert_query, records_to_insert)
connection.commit()
cursor.close()
connection.close()