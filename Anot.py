tasklist = {}
number = 1
ammount = 0
inf = 0

while inf == 0:
    command = input("Select your action:\n  create task\n  delete task\n  edit task\n  show tasks\n  edit filters\n")
    if command == "create task":
        tasklist[number] = number
        t = f"{number}tname"
        tasklist[t] = input("Enter your task's name: ")
        t = f"{number}tdesc"
        tasklist[t] = input("Enter your task's description: ")
        t = f"{number}tprio"
        tasklist[t] = int(input("Enter your task's priority: "))
        print(f"Created task number {number}, {tasklist[f'{number}tname']}, {tasklist[f'{number}tprio']}: {tasklist[f'{number}tdesc']}")
        number += 1
        ammount += 1
    elif command == "delete task":
        command = input("Enter the number of task what you want delete: ")
        del tasklist[f"{command}tname"]
        del tasklist[command]
        del tasklist[f"{command}tdesc"]
        del tasklist[f"{command}tprio"]