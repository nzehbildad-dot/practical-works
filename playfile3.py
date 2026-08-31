students = [
	{"id": "1001", "name": "Amelia Johnson", "age": 15, "class": "10A", "sex": "Female"},
	{"id": "1002", "name": "Benjamin Smith", "age": 15, "class": "10B", "sex": "Male"},
	{"id": "1003", "name": "Chloe Williams", "age": 16, "class": "11A", "sex": "Female"},
	{"id": "1004", "name": "Daniel Brown", "age": 16, "class": "11B", "sex": "Male"},
	{"id": "1005", "name": "Ella Jones", "age": 14, "class": "9A", "sex": "Female"},
	{"id": "1006", "name": "Freddie Garcia", "age": 14, "class": "9B", "sex": "Male"},
	{"id": "1007", "name": "Grace Miller", "age": 15, "class": "10A", "sex": "Female"},
	{"id": "1008", "name": "Henry Davis", "age": 15, "class": "10B", "sex": "Male"},
	{"id": "1009", "name": "Isla Rodriguez", "age": 16, "class": "11A", "sex": "Female"},
	{"id": "1010", "name": "Jack Wilson", "age": 16, "class": "11B", "sex": "Male"},
]
print("=========== school database ===========")

while True:
	print("\n1. Search for a student")
	print("2. Add student")
	print("3. Exit")
	choice = input("Choose an option: ").strip()

	if choice == "1":
		search = input("Enter student ID or name: ").strip().lower()
		found = False

		for student in students:
			if search == student["id"].lower() or search in student["name"].lower():
				print("\nStudent found")
				print(f"ID:    {student['id']}")
				print(f"Name:  {student['name']}")
				print(f"Age:   {student['age']}")
				print(f"Class: {student['class']}")
				print(f"Sex:   {student['sex']}")
				found = True

		if not found:
			print("Student not found.")

	elif choice == "2":
		student_id = input("Student ID: ").strip()
		name = input("Student name: ").strip()
		age = input("Age: ").strip()
		class_name = input("Class: ").strip()
		sex = input("Sex: ").strip()

		if not student_id or not name or not age or not class_name or not sex:
			print("All student information is required.")
			continue

		students.append({"id": student_id, "name": name, "age": age, "class": class_name, "sex": sex})
		print(f"Added {name}.")

	elif choice == "3":
		print("Goodbye.")
		break

	else:
		print("Please choose 1, 2, or 3.")

