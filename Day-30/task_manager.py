import json

# Load tasks from a JSON file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to a JSON file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(task, tasks):
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print(f"✔️ Task '{task}' added successfully!")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("Your task list is empty.")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "✔️" if task["completed"] else "❌"
            print(f"{idx}. {task['task']} [{status}]")

# Mark a task as completed
def complete_task(task_index, tasks):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks(tasks)
        print("✔️ Task marked as completed!")
    else:
        print("❌ Invalid task number.")

# Main program loop
def main():
    tasks = load_tasks()
    while True:
        print("\n📋 Task Manager Menu:")
        print("1. Add Task\n2. View Tasks\n3. Mark Task as Complete\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a new task: ")
            add_task(task, tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            view_tasks(tasks)
            try:
                task_num = int(input("Enter task number to mark as complete: ")) - 1
                complete_task(task_num, tasks)
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
