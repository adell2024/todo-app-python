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

# ... (garde les imports et fonctions add_task, list_tasks, remove_task, load_tasks, save_tasks)

if __name__ == "__main__":
    load_tasks()  # Charge les tâches existantes
    print("Bienvenue dans le gestionnaire de tâches interactif !")
    
    while True:
        print("\nMenu:")
        print("1. Ajouter une tâche")
        print("2. Lister les tâches")
        print("3. Supprimer une tâche")
        print("4. Quitter")
        
        choix = input("Entrez votre choix (1-4): ").strip()
        
        if choix == '1':
            task = input("Entrez la tâche: ").strip()
            if task:
                add_task(task)
            else:
                print("Tâche vide, annulé.")
        elif choix == '2':
            list_tasks()
        elif choix == '3':
            list_tasks()  # Affiche d'abord pour choisir
            try:
                index = int(input("Entrez le numéro de la tâche à supprimer: "))
                remove_task(index)
            except ValueError:
                print("Entrée invalide, doit être un numéro.")
        elif choix == '4':
            print("Au revoir !")
            break
        else:
            print("Choix invalide, réessayez.")
