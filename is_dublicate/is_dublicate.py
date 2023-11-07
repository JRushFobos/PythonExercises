import os
import pandas as pd

# Поиск дублей в csv файлах

script_directory = os.path.dirname(os.path.abspath(__file__))

files = {
    'Varieties': 'varietyId',
    'Crops': 'cropId',
    'Fields': 'fieldId',
    'Users': 'email',
    'Products': 'productId',
}

for file, param in files.items():
    for filename in os.listdir(script_directory):
        if filename.startswith(file) and filename.endswith('.csv'):
            df = pd.read_csv(filename, delimiter=';')
            duplicates = df[df.duplicated(subset=[param], keep=False)]
            if not duplicates.empty:
                print(f'Найдены дубликаты в колонке {param}:\n')
                print(duplicates)
                duplicates.to_csv(f'duplicates_{file}.csv', index=False)
                print(
                    f'Файл с дубликатами сохранен как duplicates_{file}.csv\n'
                )
            else:
                print(f'Дубликатов в колонке {file} не найдено.\n')
