# task_logger.py

def add_task(task):
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")

add_task("Complete Django API")
add_task("Push code to GitHub")

print("Tasks saved successfully")
