import csv
from datetime import datetime

fields = ['ID', 'Title', 'Body', 'Date']
last_id = 1

def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    note = {
        'ID' : last_id,
        'Title' : title,
        'Body' : body,
        'Datetime' : datetime.now()
    }
    save_note(note)


def save_note(note: dict):
    with open('notes.csv', 'a') as file:
        writer = csv.DictWriter(file, fields, restval='Empty', delimiter=';')
        writer.writerows(note)

def read_note():
    pass

def edit_note():
    pass

def delete_note():
    pass

