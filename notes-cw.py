# notes.py
# -*- coding: UTF-8 -*-
from sys import argv
import os
import argparse
import datetime
import uuid
import json

def detection_acton(args):
    print(len(args))
    print(args)


def detection_command(command):  # Определение действия
    if command == "show":
        print("detection", "show")
    elif command == "add":
        print("detection", "add")


def write_json(filename, datajson): # Запись файла json
    if os.path.isfile(filename): # Если файл существует воссоздать объект JSON
        print("Файл " + filename + " существует")
        with open(filename, 'r') as notes_file:
            notes_date = json.load(notes_file)
        print(notes_date)
    else: # Иначе преобразуем строку в объект JSON
        print("Файл " + filename + " не существует")
        notes_date = json.loads("[]") # Создаем пустой список (объект list) из строки JSON
    # Добавляем к объекту JSON строку JSON
    notes_date.append(datajson)
    with open(filename, 'w') as notes_file: # Сохраняем объект JSON в файл
        json.dump(notes_date, notes_file, indent=4)


def add_note(title, msg):
    # msg_id = ''.join([hex(ord(c)).replace('0x','') for c in os.urandom(8)])
    msg_id = uuid.uuid1()
    print(msg_id)
    # now = datetime.datetime.now()
    today = datetime.datetime.today()
    msg_data = today.strftime("%Y-%m-%d %H:%M:%S")
    print(msg_data)
    msg_add = {"id":str(msg_id), "data":msg_data, "title":str(title), "msg":str(msg)}
    write_json("notes.json", msg_add)


def show_notes():
    with open("notes.json", "r") as notes_file:
        data = json.load(notes_file)
        print("Покажем файл JSON")
        # print(data)
        # Переберем значения в списке
        for note in data:
            print(note)


#  detection_acton(argv)

parser = argparse.ArgumentParser(description='Parser Arguments')
parser.add_argument('action', type=str, help='Action')
parser.add_argument('-t', '--title', type=str, help='Title note')
parser.add_argument('-m', '--msg', type=str, help='Message')
parser.add_argument('-d', '--date', type=str, help='Data')
parser.add_argument('-r', '--remember', type=str, help='Params of Action')
parser.add_argument('-l', '--list', type=str, help='Show list title notes')
args = parser.parse_args()
print(args.action)
if args.action == "add":
    print(args.title)
    print(args.msg)
    add_note(args.title, args.msg)
else:
    show_notes()

# if len(argv) == 2:
    # script, command = argv
    # print("Этот скрипт называется: ", script)
    # print("Значение первой переменной: ", command)
    # detection_command(command)
# else:
    #script = argv
    # print("Этот скрипт называется: ", script)

# script = argv
# script, first, second, third = argv

# print("Этот скрипт называется: ", script)
# print("Значение первой переменной: ", first)
# print("Значение второй переменной: ", second)
# print("Значение третьей переменной: ", third)
