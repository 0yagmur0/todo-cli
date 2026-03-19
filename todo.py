import json
import os

FILENAME = "todos.json"

def load():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return json.load(file)

def save(todos):
    with open(FILENAME, "w") as file:
        json.dump(todos, file)

def add(task):
    todos = load()
    todos.append({"task": task, "done": False})
    save(todos)

def list_todos():
    todos = load()
    if not todos:
        print("No tasks.")
        return
    for index, item in enumerate(todos, 1):
        done = "X" if item["done"] else " "
        print(f"{index}. [{done}] {item['task']}")

def complete(index):
    todos = load()
    todos[index - 1]["done"] = True
    save(todos)

def delete(index):
    todos = load()
    todos.pop(index - 1)
    save(todos)

def menu():
    while True:
        print("\n1. Add\n2. List\n3. Complete\n4. Delete\n5. Quit")
        choice = input("Choice: ")
        if choice == "1":
            add(input("Task: "))
        elif choice == "2":
            list_todos()
        elif choice == "3":
            complete(int(input("Number: ")))
        elif choice == "4":
            delete(int(input("Number: ")))
        elif choice == "5":
            break

menu()

