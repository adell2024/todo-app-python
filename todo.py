import json
import os

tasks = []

def load_tasks():
    global tasks
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as f:
            tasks = json.load(f)
        print("Tasks loaded from tasks.json")

def save_tasks():
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)
    print("Tasks saved in tasks.json")

def add_task(title):
    task = {"title": title, "done": False}
    tasks.append(task)
    save_tasks()
    print(f"Task added: {title}")

def list_tasks():
    if not tasks:
        print("No tasks.")
    else:
        for task in tasks:
            status = "✔" if task["done"] else "✗"
            print(f"{status} {task['title']}")

def complete_task(index):
    if 1 <= index <= len(tasks):
        task = tasks[index - 1]
        task["done"] = True
        save_tasks()
        print(f"Task {task['title']} completed.")
    else:
        print("Index invalid.")

def remove_task(index):
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks()
        print(f"Task {removed['title']} removed.")
    else:
        print("Index invalid.")

# ... (garde les imports et fonctions add_task, list_tasks, remove_task, load_tasks, save_tasks)

if __name__ == "__main__":
    load_tasks()  # Charge les tâches existantes
    print("Welcome to the interactive task manager!")
    
    while True:
        print("\nMenu:")
        print("1. Add a task")
        print("2. List tasks")
        print("3. Remove a task")
        print("4. Mark a task as completed")
        print("5. Quit")
        
        choix = input("Enter your choice (1-5): ").strip()
        
        if choix == '1':
            title = input("Enter the task: ").strip()
            add_task(title)
        elif choix == '2':
            list_tasks()
        elif choix == '3':
            list_tasks()  # Affiche d'abord pour choisir
            try:
                index = int(input("Enter the task number to remove: "))
                remove_task(index)
            except ValueError:
                print("Invalid input, must be a number.")
        elif choix == '4':
            list_tasks()  # Affiche d'abord pour choisir
            try:
                index = int(input("Enter the task number to mark as completed: "))
                complete_task(index)
            except ValueError:
                print("Invalid input, must be a number.")
        elif choix == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

