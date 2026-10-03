import csv
import gdown


def show_data(file):
    print("Первые 10 строк датасета")
    with open(file, "r") as f:
        reader = csv.reader(f)
        for i in range(10):
            line = next(reader)
            print(line)


if __name__ == "__main__":
    link = "https://drive.google.com/file/d/1VtPmObnfUbxaKAvi0SEaLBdVvYJSNMHV/view?usp=drive_link"
    file_name = "dataset.csv"

    gdown.download(link, file_name)

    show_data(file_name)
