import pandas as pd

# Укажите пути к файлам (предполагается формат CSV)
file_paths = [
    './tablitsa1.csv',
    './tablitsa2.csv',
    './tablitsa3.csv'
]

# Инициализируем пустой список для хранения датафреймов
dataframes = []

# Загрузим данные в датафреймы
for file_path in file_paths:
    df = pd.read_csv(file_path)
    dataframes.append(df)

# Инициализируем current_id на 1
current_id = 1

# Обработаем каждый датафрейм, чтобы обновить столбец id
for i, df in enumerate(dataframes):
    df['id'] = range(current_id, current_id + len(df))
    current_id += len(df)
    # Сохраним обновленный датафрейм обратно в CSV (или любой другой требуемый формат)
    df.to_csv(f'./tablitsa4{i+1}.csv', index=False)

# Проверим, что файлы были созданы
for i in range(1, len(dataframes) + 1):
    df = pd.read_csv(f'./tablitsa4{i}.csv')
    print(f"Содержимое файла tablitsa4{i}.csv:")
    print(df)
