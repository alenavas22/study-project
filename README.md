# study-project

Репозиторий содержит проект по анализу базы данных атомных координат и структурных параметров металлоорганических каркасных структур (MOFs) на основе набора данных **[High-Throughput Comp. Screening of MOFs](https://www.kaggle.com/datasets/thedevastator/high-throughput-comp-screening-of-mofs)**, взятого с сайта kaggle.com.

Датасет содержит геометрические и физико-химические параметры металлоорганических каркасных структур. Данные могут быть применены для оценки потенциала MOFs в задачах:
* разделения и очистки веществ;
* катализа;
* создания функциональных материалов.

Размер датасета: 1,8 МБ
Ссылка на датасет: [Датасет на Google Диске](https://drive.google.com/drive/folders/12avKEntdcJpG_2k6-46-FIl8Dmhc478W?usp=drive_link)

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/alenavas22/study-project.git
   cd study-project
   ```

2. Разверните окружение и установите зависимости из файла:
   ```bash
   uv sync --frozen
   ```

3. Запустите скрипт:
   ```bash
   uv run data_loader.py
   ```
## Запуск скрипта `data_loader.py` 

1. Cкачивает исходный файл `dataset.csv` с Google Диска (если он отсутствует локально).
2. Выводит первые 10 строк датасета.
3. Считывает таблицу и приводит столбцы к правильным типам данных (`str`, `float32`, `category`, `bool`) для уменьшения занимаемой памяти.
4. Сохраняет DataFrame в формат `.parquet` (если файл `dataset.parquet` ещё не создан).