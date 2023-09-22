import csv
from datetime import datetime

fields = ['ID', 'Title', 'Body', 'Datetime']
last_id = 1

def get_last_id() -> int:
    with open('notes.csv', 'r') as file:
        last_line = file.readlines()[-1]
        return int(last_line.split(';')[0])

def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    note = {
        'ID' : last_id,
        'Title' : title,
        'Body' : body,
        'Datetime' : datetime.now().strftime('%Y-%m-%d, %H:%M')
    }
    save_note(note)

def save_note(note: dict):
    with open('notes.csv', 'a') as file:
        writer = csv.DictWriter(file, fields, restval='Empty', delimiter=';')
        writer.writerows([note])

def get_notes() -> list:
    notes = []
    with open('notes.csv', 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            notes.append(row)
    return notes

def show_notes():
    notes = get_notes()
    choice = ''
    cur = 0
    while choice != 'q':
        if cur == len(notes):
            cur = cur-5 if cur-5 > 0 else 0
        next_cur = cur+5 if cur+5 < len(notes) else len(notes) # Правая граница отображения
        for i in range(cur, next_cur):
            cur = next_cur
            note = notes[i]
            print(f"{note['ID']}. {note['Title']} : {note['Datetime']}")
        print('< - обратно; > - далее; {id} - для выбора заметки; q - меню')
        choice = input('Введите операцию или ID: ')
        if choice == '<':
            cur = cur-5 if cur-5 > 0 else 0
        elif choice == '>':
            continue
        elif choice == 'q':
            break
        else:
            if choice.isdigit():
                read_note(choice, notes)

def read_note(note_id: str, notes: list):
    found_line = -1
    for i, note in enumerate(notes):
        if note['ID'] == note_id:
            found_line = i
            break
    if found_line == -1:
        print("Заметка с таким id не найдена!")
        return
    while 1:
        print(f"Заголовок: {note['Title']}")
        print(f"Содержание: {note['Body']}")
        print('e - изменить; d - удалить; q - закрыть')
        choice = input('Введите операцию: ')
        if choice == 'q':
            break
        if choice == 'd':
            delete_note()
            print("Удаляем")
            break
        if choice == 'e':
            edit_note()
            print("Изменяем")

def edit_note():
    pass

def delete_note():
    pass
