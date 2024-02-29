#-*- coding: UTF-8 -*-
from sys import argv
import json

if len(argv)==2:
    script, command = argv
    print("Этот скрипт называется: ", script)
    print("Значение первой переменной: ", command)
    detectionCommand(command)
else:
    script = argv
    print("Этот скрипт называется: ", script)

with open('notes.json', 'r') as notes_file:
    notes_data = json.load(notes_file)
    print(notes_data)

def detectionCommand(command): # Определение действия
    if command=="show":
        print("detection", "show")
    elif command=="add":
        print("detection", "add")



# script = argv
# script, first, second, third = argv

# print("Этот скрипт называется: ", script)
# print("Значение первой переменной: ", first)
# print("Значение второй переменной: ", second)
# print("Значение третьей переменной: ", third)
