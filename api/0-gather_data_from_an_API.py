#!/usr/bin/python3
""" Library to gather data from an API """

import requests
import sys

""" Function to gather data from an API """

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)

    todo = "https://jsonplaceholder.typicode.com/todos?userId={}"
    todo = todo.format(employee_id)

    user_info = requests.request("GET", url).json()
    todo_info = requests.request("GET", todo).json()

    employee_name = user_info.get("name")
    total_tasks = list(filter(lambda x: (x["completed"] is True), todo_info))
    task_com = len(total_tasks)
    total_task_done = len(todo_info)

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          task_com, total_task_done))

    """
        return name, total number of tasks & completed tasks
    """
    EMPLOYEE_NAME = employee_name
    TOTAL_NUMBER_OF_TASKS = len(tasks)
    NUMBER_OF_DONE_TASKS = len([k for k, v in tasks.items() if v is True])
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for k, v in tasks.items():
        if v is True:
            print("\t {}".format(k))