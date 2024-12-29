# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:14:33 2024

@author: Mahfuzur Rahman
"""

# todo_list.py
def todo_list():
    tasks = []
    while True:
        print("\nTo-Do List App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter a new task: ")
            tasks.append(task)
            print(f"Task '{task}' added.")
        elif choice == '2':
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif choice == '3':
            task_no = int(input("Enter task number to remove: "))
            if 0 < task_no <= len(tasks):
                removed = tasks.pop(task_no - 1)
                print(f"Task '{removed}' removed.")
            else:
                print("Invalid task number.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

todo_list()
