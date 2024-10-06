# List to hold the names of students
students = []

# Function to add a student
def add_student(name):
    students.append(name)
    print(f"{name} has been added to the list.")

# Function to remove a student
def remove_student(name):
    if name in students:
        students.remove(name)
        print(f"{name} has been removed from the list.")
    else:
        print(f"{name} is not in the list.")

# Function to display all students
def display_students():
    if students:
        print("The students in the class are:")
        for student in students:
            print(student)
    else:
        print("No students in the list.")

# Example usage
add_student("John")
add_student("Alice")
display_students()
remove_student("John")
display_students()