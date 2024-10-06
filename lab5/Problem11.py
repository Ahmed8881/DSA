# List of employee names
employees = ["John", "Alice", "Bob", "Emily", "Michael"]

# Function to search for an employee's name
def search_employee(name):
    if name in employees:
        index = employees.index(name)
        return f"{name} found at index {index}."
    else:
        return f"{name} is not present in the list."

    # Example usage
    
    
result1 = search_employee("Alice")  # Name exists in the list
result2 = search_employee("David")  # Name does not exist in the list

    # Output the results 
print(result1)
print(result2)