import csv
from datetime import datetime
import os.path

fields = ["ID", "Title", "Body", "Datetime"]


def get_last_id() -> int:
    with open("notes.csv", "r") as file:
        last_line = file.readlines()[-1]
        try:
            last_id = int(last_line.split(";")[0])
        except:
            last_id = 0
        return last_id


def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    note = {
        "ID": get_last_id() + 1,
        "Title": title,
        "Body": body,
        "Datetime": datetime.now().strftime("%Y-%m-%d, %H:%M"),
    }
    save_note(note)


def save_note(note: dict):
    with open("notes.csv", "a") as file:
        writer = csv.DictWriter(file, fields, restval="Empty", delimiter=";")
        writer.writerows([note])


def get_notes() -> list:
    notes = []
    with open("notes.csv", "r") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            notes.append(row)
    return notes


def get_notes_by_date(date: str) -> list:
    notes = []
    with open("notes.csv", "r") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            if row["Datetime"][:10] == date:
                notes.append(row)
    return notes


def show_notes(date: str = None):
    all_notes = get_notes()
    choice = ""
    cur = 0
    while choice != "q":
        notes = all_notes if date is None else get_notes_by_date(date)
        if cur >= len(notes):
            cur = cur - 5 if cur - 5 > 0 else 0
        elif cur > len(notes) - 5 and cur - 5 >= 0:
            cur = len(notes) - 5
            print("njnjknk")
        next_cur = (
            cur + 5 if cur + 5 < len(notes) else len(notes)
        )  # Правая граница отображения
        print("-" * 20)
        for i in range(cur, next_cur):
            cur = next_cur
            note = notes[i]
            print(f"{note['ID']}. {note['Title']} : {note['Datetime']}")
        print("< - обратно; > - далее; {id} - для выбора заметки; q - меню")
        choice = input("Введите операцию или ID: ")
        if choice == "<":
            cur = cur - 10 if cur - 10 > 0 else 0
        elif choice == ">":
            continue
        elif choice == "q":
            break
        else:
            if choice.isdigit():
                all_notes = read_note(choice, all_notes)


def read_note(note_id: str, notes: list) -> list:
    found_line = -1
    for i, note in enumerate(notes):
        if note["ID"] == note_id:
            found_line = i
            break
    if found_line == -1:
        print("Заметка с таким id не найдена!")
        return notes
    while 1:
        print(f"Заголовок: {note['Title']}")
        print(f"Содержимое: {note['Body']}")
        print("e - изменить; d - удалить; q - закрыть")
        choice = input("Введите операцию: ")
        if choice == "q":
            return notes
        if choice == "d":
            delete_note(found_line, notes)
            print("Удаляем...")
            return get_notes()
        if choice == "e":
            edit_note(found_line, notes)
            print("Изменяем...")
            return get_notes()


def edit_note(line_index: int, notes: list):
    title = input("Новый заголовок: ")
    body = input("Новое содержимое: ")
    if title != "":
        notes[line_index]["Title"] = title
        notes[line_index]["Datetime"] = datetime.now().strftime("%Y-%m-%d, %H:%M")
    if body != "":
        notes[line_index]["Body"] = body
        notes[line_index]["Datetime"] = datetime.now().strftime("%Y-%m-%d, %H:%M")
    if title == "" and body == "":
        return
    while 1:
        choice = input("Сохранить изменения? (Y/n)")
        if choice == "n":
            break
        if choice == "Y":
            update_notes(notes)
            break


def update_notes(notes: list):
    with open("notes.csv", "w") as file:
        writer = csv.DictWriter(file, fields, restval="Empty", delimiter=";")
        writer.writeheader()
        writer.writerows(notes)


def delete_note(line_num: int, notes: list):
    notes.pop(line_num)
    update_notes(notes)


def ui():
    print("Добро пожаловать в заметки!")

    while 1:
        print("-" * 20)
        print("add - добавить заметку")
        print("show - посмотреть все заметки")
        print("show YYYY-mm-dd - показать заметки за введенную дату")
        print("quit - выход")
        choice = input("Введите команду: ")
        if choice == "quit":
            break
        if choice == "add":
            add_note()
        elif choice == "show":
            show_notes()
        elif choice.startswith("show "):
            try:
                params = choice[5:].split("-")
                year = int(params[0])
                month = int(params[1])
                day = int(params[2])
                show_notes(choice[5:])
            except Exception as e:
                print("Вы неправильно ввели дату!")
                continue


if __name__ == "__main__":
    # Создадим файл для заметок, если его нет
    if not os.path.isfile('notes.csv'):
        with open("notes.csv", "w") as file:
            writer = csv.DictWriter(file, fields, restval="Empty", delimiter=";")
            writer.writeheader()
    ui()