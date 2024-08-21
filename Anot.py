tasklist = {}
number = 1
ammount = 0
inf = 0
def create():
    t = f"{number}tnumb"
    tasklist[t] = number
    t = f"{number}tname"
    tasklist[t] = input("Enter your tasks name: ")
    t = f"{number}tdesc"
    tasklist[t] = input("Enter your tasks description: ")
    t = f"{number}tprio"
    tasklist[t] = float(input("Enter your tasks priority: "))
    number += 1
    ammount += 1


while inf == 0:
    command = input("Select your action:\ncreate task\ndelete task\nedit task\nshow tasks\nedit filters")
    