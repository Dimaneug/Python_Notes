import csv

fields = ['ID', 'Title', 'Body', 'Date']

def add_note():
    pass

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

