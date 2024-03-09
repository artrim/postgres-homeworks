"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2

conn_params = {
  "host": "localhost",
  "database": "north",
  "user": "postgres",
  "password": "123"
}


with psycopg2.connect(**conn_params) as conn:
    with open('north_data/customers_data.csv') as file:
        file_reader = csv.reader(file)
        next(file_reader)
        with conn.cursor() as cur:
            for row in file_reader:
                cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", row)
conn.close()

with psycopg2.connect(**conn_params) as conn:
    with open('north_data/employees_data.csv') as file:
        file_reader = csv.reader(file)
        next(file_reader)
        with conn.cursor() as cur:
            for row in file_reader:
                cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", row)
conn.close()

with psycopg2.connect(**conn_params) as conn:
    with open('north_data/orders_data.csv') as file:
        file_reader = csv.reader(file)
        next(file_reader)
        with conn.cursor() as cur:
            for row in file_reader:
                cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", row)
conn.close()
