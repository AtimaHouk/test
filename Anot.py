tasklist = {}
number = 1
lst = []
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
        lst.append(number)
        number += 1
    elif command == "delete task":
        command = int(input("Enter the number of task what you want delete: "))
        del tasklist[f"{command}tname"]
        del tasklist[command]
        del tasklist[f"{command}tdesc"]
        del tasklist[f"{command}tprio"]
        lst.remove(command)
    elif command == "edit task":
        command = int(input("Enter the number of task what you want edit: "))
        print (f"{command}, {tasklist[f'{command}tname']}, {tasklist[f'{command}tprio']}: {tasklist[f'{command}tdesc']}\n")
        command2 = input(f"What point do you want to edit?\n Head: ({tasklist[f'{command}tname']})\n Description: ({tasklist[f'{command}tdesc']})\n Priority: ({tasklist[f'{command}tprio']})")
        command3 = input(f"Write the new: ")
        if command2 == "Head":
            tasklist[f'{command}tname'] = command3
        elif command2 == "Description":
            tasklist[f'{command}tdesc'] = command3
        else:
            tasklist[f'{command}tprio'] = command3
    elif command == "show tasks":
        for i in lst:
            print(f"{i}, {tasklist[f'{i}tname']}, {tasklist[f'{command}tprio']}: {tasklist[f'{command}tdesc']}\n"))