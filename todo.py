import json
import os


def load():     # () fonksiyonun dışarıdan veri almasını sağlar. Dışarıdan bir şey almıyor, sadece dosyayı okuyor
    if not os.path.exists("todos.json"):
        return []
    # with: dosyayı aç, işin bitince otomatik kapat.
    with open("todos.json", "r") as file:       # r = read
        return json.load(file)


def save(todos):     # dışarıdan todos listesini alıyor, onu kaydediyor
    with open("todos.json", "w") as file:       # w = write
        # Python listesini JSON formatına çevirip dosyaya yazar.
        json.dump(todos, file)


def add(task):
    todos = load()      # mevcut listeyi dosyadan çek
    # key "task", value dışarıdan gelen parametre (kullanıcının yazdığı görev) | key "done", value False (yeni görev tamamlanmamış)
    todos.append({"task": task, "done": False})
    save(todos)     # güncellenmiş todos listesini dosyaya kaydet


def list_todos():
    todos = load()
    if not todos:
        print("No Tasks.")
        return

 # enumerate - hem index hem eleman var. Normalde 0 dan başlar 1 den başlasın diye (todos) yerine (todos, 1) yazıyoruz.
    for index, item in enumerate(todos, 1):
        done = "X" if item["done"] else " "
        print(f"{index}. [{done}] {item['task']}")


def complete(index):  # görev tamamlandı olarak işaretle.
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
            # kullanıcıdan string aldı, integer e çevirdi, complete fonksiyonuna gönderdi.
            complete(int(input("Number: ")))

        elif choice == "4":
            delete(int(input("Number: ")))

        elif choice == "5":
            break


# Bu olmadan program çalışmaz. Fonksiyonlar tanımlı ama hiçbiri çağrılmamış olur.
menu()
# Başa yazılısa Python menu() görür ama henüz load, save, add tanımlı olmadığı için hata verir. Bu nedenle en sona koyuyoruz.
