def get_grade(subject):
	"""
	Collects grades for a given subject from user input, calculates the average grade,
	and returns the average grade and the list of grades.

	Args:
	subject (str): The name of the subject.

	Returns:
	tuple: A tuple containing the average grade (float) and the list of grades (list of floats).
	"""
	try:
		subject_list = []
		while True:
			grade = input(f"Enter the grade for {subject} (press Enter to finish): ")
			if grade.strip() == '':
				break
			try:
				subject_list.append(float(grade))
			except ValueError:
				print("Please enter a valid grade.")
		
		average_grade = sum(subject_list) / len(subject_list) if subject_list else 0.0
		return average_grade, subject_list
	except Exception as e:
		print(f"An error occurred: {e}")
		return 0.0, []


def calculate_average_grades(student_data):
	"""
	Calculates the overall average grade for each student across all subjects.

	Args:
	student_data (dict): A dictionary where keys are student names and values are dictionaries of subjects with their average grades.

	Returns:
	dict: A dictionary containing student names as keys and their overall average grade as values.
	"""
	average_grades = {}
	for student_name, grades in student_data.items():
		total_sum = sum(grades.values())
		count = len(grades)
		average_grades[student_name] = total_sum / count if count != 0 else 0.0
	return average_grades


def get_number_of_students():
	"""
	Prompts the user to enter the number of students.

	Returns:
	int: The number of students.
	"""
	while True:
		try:
			num_students = int(input("Enter the number of students: "))
			return num_students
		except ValueError:
			print("Please enter a valid number.")


def get_student_name():
	"""
	Prompts the user to enter the student's name.

	Returns:
	str: The name of the student.
	"""
	return input("Enter the student's name: ")


def get_student_grades():
	"""
	Collects grades for a student for various subjects from user input.

	Returns:
	dict: A dictionary of subjects and their average grades.
	"""
	all_grades = {}
	empty_input_count = 0
	
	while True:
		if empty_input_count == 1:
			print("Moving to the next student.")
			break
		
		subject = input("Enter the subject (or press Enter again to finish): ")
		if subject.strip() == '':
			empty_input_count += 1
			continue
		else:
			empty_input_count = 0
		
		average_grade, grades = get_grade(subject)
		if grades:
			all_grades[subject] = average_grade
		print(f"\nAverage grade for {subject}: {average_grade:.1f}")
	
	return all_grades


def process_student_data(num_students):
	"""
	Collects and processes data for all students.

	Args:
	num_students (int): The number of students.

	Returns:
	dict: A dictionary containing student names as keys and their grades as values.
	"""
	student_data = {}
	
	for _ in range(num_students):
		student_name = get_student_name()
		student_grades = get_student_grades()
		student_data[student_name] = student_grades
	
	return student_data


def print_student_information(student_data):
	"""
	Prints all student information including their grades for each subject.

	Args:
	student_data (dict): A dictionary containing student names as keys and their grades as values.
	"""
	print("\nAll Student Information:")
	for student_name, grades in student_data.items():
		print(f"\nName: {student_name}")
		for subject, average_grade in grades.items():
			print(f"{subject}: {average_grade:.1f}")


def print_final_student_data(student_data):
	"""
	Prints the final student data in the specified format.

	Args:
	student_data (dict): A dictionary containing student names as keys and their grades as values.
	"""
	print("\nFinal student data:")
	for student_name, grades in student_data.items():
		student_info = {"Name": student_name}
		student_info.update(grades)
		print(student_info)


def print_overall_average_grades(student_data):
	"""
	Calculates and prints overall average grades across all subjects.

	Args:
	student_data (dict): A dictionary containing student names as keys and their grades as values.
	"""
	average_grades = calculate_average_grades(student_data)
	print("\nOverall average grade across all subjects:")
	for student_name, average_grade in average_grades.items():
		print(f"{student_name}: {average_grade:.1f}")


def main():
	"""
	Main function to orchestrate the collection and processing of student data.

	Returns:
	dict: A dictionary containing student names as keys and their grades as values.
	"""
	num_students = get_number_of_students()
	return process_student_data(num_students)


if __name__ == '__main__':
	student_data = main()
	
	print_student_information(student_data)
	print_final_student_data(student_data)
	print_overall_average_grades(student_data)
