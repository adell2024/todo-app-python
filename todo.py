# todo.py
tasks = []

# Ajoutez cette fonction
def remove_task(index):
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"Tâche supprimée : {removed}")
    else:
        print("Index invalide.")

def add_task(task):
    tasks.append(task)
    print(f"Tâche ajoutée : {task}")

def list_tasks():
    if not tasks:
        print("Aucune tâche.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Mettez à jour le if __name__ == "__main__":
if __name__ == "__main__":
    print("Bienvenue dans le gestionnaire de tâches !")
    add_task("Apprendre Git")
    add_task("Maîtriser GitHub")
    list_tasks()
    remove_task(1)  # Supprime la première tâche
    list_tasks()
