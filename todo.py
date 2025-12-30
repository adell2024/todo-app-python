import json
import os

tasks = []

def load_tasks():
    global tasks
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as f:
            tasks = json.load(f)
        print("Tâches chargées depuis tasks.json")

def save_tasks():
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)
    print("Tâches sauvegardées dans tasks.json")

def add_task(task):
    tasks.append(task)
    print(f"Tâche ajoutée : {task}")
    save_tasks()

def list_tasks():
    if not tasks:
        print("Aucune tâche.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task(index):
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"Tâche supprimée : {removed}")
        save_tasks()
    else:
        print("Index invalide.")

if __name__ == "__main__":
    load_tasks()  # Charge au démarrage
    print("Bienvenue dans le gestionnaire de tâches !")
    add_task("Apprendre Git")
    add_task("Maîtriser GitHub")
    list_tasks()
    remove_task(1)  # Supprime la première
    list_tasks()
