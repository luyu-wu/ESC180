def num_tasks(tasks, elf_name):
    count = 0
    for i in tasks:
        if tasks[i] == elf_name:
            count += 1
    return count
def most_tasks(tasks):
    most = 0
    most_name = ""
    for i in tasks:
        if num_tasks(tasks,tasks[i]) > most:
            most = num_tasks(tasks,tasks[i])
            most_name = tasks[i]
    return most_name
    
tasks = {
"dolls": "Dewdrop",
"trains": "Frostleaf",
"robots": "Dewdrop",
"puzzles": "Comet",
"compilers": "Mike",
"bridge kits": "Evan"
}
print(num_tasks(tasks,"Dewdrop"))
print(most_tasks(tasks))

