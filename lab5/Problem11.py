student_list = ["Ahmed", "Ali", "Aslam", "Akmal", "Anas"]

def search_employee(name):
    if name in student_list:
        index = student_list.index(name)
        return name + " found at index " + str(index) + "."
    else:
        return name + " is not present in the list."

    
    
result1 = search_employee("Akmal")  
result2 = search_employee("Zaeem")  
print(result1)
print(result2)