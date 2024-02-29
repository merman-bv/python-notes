# notes.py
# -*- coding: UTF-8 -*-
from sys import argv
import os
import argparse
import datetime
import json

def detection_acton(args):
    print(len(args))
    print(args)


def detection_command(command):  # Определение действия
    if command == "show":
        print("detection", "show")
    elif command == "add":
        print("detection", "add")


def write_json(filename, data): # Запись файла json
    with open(filename, 'w') as notes_file:
        json.dump(data, notes_file, indent=4)

def add_note(title, msg):
    msg_id = 2
    # now = datetime.datetime.now()
    today = datetime.datetime.today()
    msg_data = today.strftime("%Y-%m-%d %H:%M:%S")
    print(msg_data)
    msg_add = {"id":"2", "data":msg_data, "title":"note2", "msg":"test notes"}
    # notes_data = json.load(open("notes.json"))
    # notes_data.appemd(msg_add)
    if os.path.isfile("notes.json"):
        print("Файл существует")
        write_json("notes.json", msg_add)
    else:
        print("Файл не существует")
        data ={}
        write_json("notes.json", data)


def show_notes():
    with open("notes.json", "r") as notes_file:
        data = json.load(notes_file)
        print("Покажем файл JSON")
        print(data)

#  detection_acton(argv)

parser = argparse.ArgumentParser(description='Parser Arguments')
parser.add_argument('action', type=str, help='Action')
parser.add_argument('-t', '--title', type=str, help='Title note')
parser.add_argument('-m', '--msg', type=str, help='Message')
parser.add_argument('-d', '--date', type=str, help='Data')
parser.add_argument('-r', '--remember', type=str, help='Params of Action')
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
