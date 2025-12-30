# todo.py
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Tâche ajoutée : {task}")

def list_tasks():
    if not tasks:
        print("Aucune tâche.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

if __name__ == "__main__":
    print("Bienvenue dans le gestionnaire de tâches !")
    add_task("Apprendre Git")
    list_tasks()
