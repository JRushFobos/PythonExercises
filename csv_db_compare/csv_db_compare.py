import os
import pyodbc
import csv

'''Скрипт проверки наличия объектов из csv файла в бд'''

script_directory = os.path.dirname(os.path.abspath(__file__))

files = {
    'Crops': 'cropid',
    'Varieties': 'varietyid'
}

username = 'username'
password = 'password'
port = '1433'


сonnection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=servername;"
    "DATABASE=databasename;"
    f"UID={username};"
    f"PWD={password};"
)

crop_query = ("""SELECT id FROM crop_table""")
varieties_query = ("""SELECT id FROM variety_table""")


queries = (crop_query,
           varieties_query,
           )

conn = pyodbc.connect(сonnection_string)

cursor = conn.cursor()

is_saved_fields = []
for query in queries:
    cursor.execute(query)
    obj_in_bd = cursor.fetchall()
    print(f'Записей в БД {len(obj_in_bd)}')
    is_saved_fields.extend([item[0] for item in obj_in_bd])

for file, param in files.items():
    for filename in os.listdir(script_directory):
        if filename.startswith(file) and filename.endswith('.csv'):
            with open(filename, 'r') as input_csv, \
                 open(f"diff_obj_file_{filename}", 'w', newline='') \
                    as output_csv:
                csv_reader = csv.DictReader(input_csv, delimiter=';')
                fieldnames = csv_reader.fieldnames
                csv_writer = csv.DictWriter(output_csv, fieldnames=fieldnames,
                                            delimiter=';')

                # Записываем заголовки в файл вывода
                csv_writer.writeheader()

                # Проходим по каждой строке в исходном файле
                count = 0
                for row in csv_reader:
                    if row[param] not in is_saved_fields:
                        # Записываем строку в файл вывода
                        print(f"{row[param]} нет в БД")
                        count += 1
                        csv_writer.writerow(row)

                print(f"{count} значений из файла {filename}, нет в бд")
