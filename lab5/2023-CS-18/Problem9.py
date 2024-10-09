students = []

def add_student(name):
    message = name + " is enrolled."
    students.append(name)
    print(message)

def remove_student(name):
    if name in students:
        students.remove(name)
        message = name + " has been removed ."
        print(message)
    else:
        message = name + " is not found."
        print(message)

def display_students():
    if students:
        print("The students in class are:")
        for student in students:
            print(student)
    else:
        print("No students found.")

def print_options():
    print("1 - Add Student")
    print("2 - Remove Student")
    print("3 - Display All Students")
    print("4 - Exit")

def main():
    while True:
        print_options()
        choice = input("Enter your choice : ")

        if choice == '1':
            name = input("Enter the name of the student to add: ")
            add_student(name)
        elif choice == '2':
            name = input("Enter the name of the student to remove: ")
            remove_student(name)
        elif choice == '3':
            display_students()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please enter a valid option.")



main()
