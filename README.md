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
