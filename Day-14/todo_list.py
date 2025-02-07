# Simple To-Do List Program

tasks = []

while True:
    print("\n📝 To-Do List Options:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print(f"✅ Task '{task}' added.")

    elif choice == '2':
        if not tasks:
            print("📭 Your to-do list is empty.")
        else:
            print("\n📋 Your tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == '3':
        if not tasks:
            print("❌ No tasks to remove.")
        else:
            try:
                task_num = int(input("Enter task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"🗑️ Task '{removed_task}' removed.")
                else:
                    print("⚠️ Invalid task number.")
            except ValueError:
                print("⚠️ Please enter a valid number.")

    elif choice == '4':
        print("👋 Goodbye!")
        break

    else:
        print("⚠️ Invalid choice. Please try again.")
