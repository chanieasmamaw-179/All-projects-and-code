def update_tasks(task_list):
	task_to_update = input("Which task would you like to update? (Provide the task description): ")
	
	if task_to_update in task_list:
		new_task_description = input("What do you want to name it? ")
		
		for i, task in enumerate(task_list):
			if task == task_to_update:
				task_list[i] = new_task_description
				print(f"Task '{task_to_update}' updated to '{new_task_description}'.")
				break
	else:
		print("This task is not in the list")


def update_tasks(task_list):
	task_to_update = input("Which task would you like to update? (Provide the task description): ")
	
	if task_to_update in task_list:
		new_task_description = input("What do you want to name it? ")
		
		for i, task in enumerate(task_l	ist):
			if task == task_to_update:
				task_list[i] = new_task_description
				print(f"Task '{task_to_update}' updated to '{new_task_description}'.")
				break
	else:
		print("This task is not in the list")


# Example usage
task_list = ['painting', 'cleaning', 'Learn to code']
update_tasks(task_list)
print(task_list)

# Example usage
task_list = ['painting', 'cleaning', 'Learn to code']
update_tasks(task_list)
print(task_list)

"""
def delete_task(task_list):
	task_to_delete = input("Which task would you like to delete? (Provide the task description): ")
	if task_to_delete in task_list:
		task_list.remove(task_to_delete)
		print(f"'{task_to_delete}' was removed from the task manager.")
	else:
		print("This task is not in the list")
# Example usage
task_list = ['.....', '.....', '......']
delete_task(task_list)
print(task_list)
"""
