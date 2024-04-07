import click 

@click.group()
def config():
    pass

@click.command()
@click.option("--uname", prompt="Give a username ",help="the username for login")
def init(uname):
    click.echo(f"welcome {uname}")
    
# adding a task 
PRIORITIES = {
    'o':"optional".capitalize(),
    'h':"high".capitalize(),
    'l':"low".capitalize(),
    'n':"normal".capitalize(),
    'c':"critical".capitalize()
}
@click.command()
@click.argument('priority',type=click.Choice(PRIORITIES.keys()),default ='o')
@click.argument('tasksfile',type = click.Path(exists=False),required=0)
@click.option("--task",'--tsk', prompt="task name required ",help="the task to be done")
@click.option("--tag", prompt="tag required ",help="a tag for identifying the task")
@click.option("--desc",'--d', prompt="description required ",help="task content description")
def create_task(task,tag,desc,priority,tasksfile):
    filename = tasksfile if tasksfile is not None else "tasks.txt"
    with open(filename,'a+') as f:
        f.write(f"{task} {tag} {desc} [PRIORITIES: {PRIORITIES[priority]}]\n")

@click.command()
@click.argument('index',type=int,required=1)
def del_task(index):
    with open('tasks.txt', 'r') as f:
        tasks = f.read().splitlines()
        tasks.pop(index)
    with open('tasks.tst','w') as wf:
        wf.write("\n".join(tasks))
        wf.write("\n")
        
@click.command()
def edit_task(index,tag,desc):
    pass

@click.command()
@click.argument('priority',type=click.Choice(PRIORITIES.keys()),default ='o')
@click.argument('tasksfile',type = click.Path(exists=True),required=1)
def list_tasks(priority,tasksfile):
    filename = tasksfile if tasksfile is not None else "tasks.txt"
    with open(filename,'r') as f:
        tasks = f.read().splitlines()
    if priority is None:
        for idx,task in enumerate(tasks):
            print(f"{idx}> {task}")
    else:
        for idx,task in enumerate(tasks):
            if f"[PRIORITIES: {PRIORITIES[priority]}]" in task:
                print(f"{idx}> {task}")
                

config.add_command(init)
config.add_command(create_task)
config.add_command(del_task)
config.add_command(edit_task)
config.add_command(list_tasks)

if __name__ == "__main__":
    config()