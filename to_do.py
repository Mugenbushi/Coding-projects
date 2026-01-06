import argparse
import os
import json


# file to sore my list items
Get_done = "tlist.json"


def load_task():
    # laods teh tqaskk file ro creates one if missing
    if not os.path.exists(Get_done):
        return []
    with open(Get_done, "r") as doc:
        return json.load(doc)
    
def save_task(tasks):
    # Saves taskt tot he file
    with open(Get_done, "w") as doc :
        json.dump(tasks, doc, indent=4)



def list_task():
    #this function list all the task
    tasks = load_task()

    if not tasks:
        print(" no task in file")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✔️" if task["done"] else "❌"
        print(f"{i}. {status} {task['title']}") 


def new_task(title):
    # creating a new task
    tasks = load_task()
    tasks.append({"title" : title, "done" : False })
    save_task(tasks)
    print(f"added task {title}")

# new_task(input("Tell me Your task"))

def mark_task(index):
    tasks = load_task()

    try:
        tasks[index - 1]["done"] = True
        save_task(tasks)
        print(f"marked task #{index} as done")
    except IndexError:
        print("Invalid task marked")

def delete_task(index):
    # Delete a task
    tasks = load_task()
    try:
        removed = tasks.pop(index - 1)
        save_task(tasks)
        print(f"Deleted task: {removed['title']}")
    except IndexError:
        print("Invalid task number.")

def main():
    parser = argparse.ArgumentParser(description="Simple command-line to-do list.")
    subparsers = parser.add_subparsers(dest="command")

    # Add command
    add_pars = subparsers.add_parser("add", help="Add a new task")
    add_pars.add_argument("title", type=str, help="The task description")

    # List command
    subparsers.add_parser("list", help="List all tasks")

    # Done command
    done_pars = subparsers.add_parser("done", help="Mark a task as done")
    done_pars.add_argument("index", type=int, help="The task number")

    # Delete command
    delete_pars = subparsers.add_parser("delete", help="Delete a task")
    delete_pars.add_argument("index", type=int, help="The task number")

    args = parser.parse_args()

    if args.command == "add":
        new_task(args.title)
    elif args.command == "list":
        list_task()
    elif args.command == "done":
        mark_task(args.index)
    elif args.command == "delete":
        delete_task(args.index)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
        