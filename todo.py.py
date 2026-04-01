print('This your to-do list\nEnter "x" when you want to stop')
def todo():
    tasks = []
    while True:
        task = str(input('Enter a task: '))
        if task == 'x':
            break
        tasks.append(task)
    show = str(input('Enter "s" to show the tasks: '))
    if show == 's':
        print(tasks)
todo()