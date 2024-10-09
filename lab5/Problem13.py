# Initialize the grid (2D list)
grid = []

# Function to display the grid
def display_grid():
    if not grid:
        print("The grid is empty.")
    else:
        print("Current grid:")
        for row in grid:
            print(row)

# Function to add a row to the grid
def add_row(new_row):
    if grid and len(new_row) != len(grid[0]):
        print("Error: The new row must have the same number of columns as the existing grid.")
    else:
        grid.append(new_row)
        print("Row added successfully.")

# Function to add a column to the grid
def add_column(new_column):
    if not grid or len(new_column) != len(grid):
        print("Error: The new column must have the same number of rows as the existing grid.")
    else:
        for i in range(len(grid)):
            grid[i].append(new_column[i])
        print("Column added successfully.")

# Function to find the sum of all elements in the grid
def sum_of_grid():
    total_sum = 0
    for row in grid:
        total_sum += sum(row)
    return total_sum

# Main program for user interaction
def main():
    while True:
        print("1 - Add Row")
        print("2 - Add Column")
        print("3 - Display Grid")
        print("4 - Sum of All Elements")
        print("5 - Exit")
        
        choice = input("Enter your choice : ")

        if choice == '1':
            new_row = list(map(int, input("Enter the new row (space-separated values): ").split()))
            add_row(new_row)
        elif choice == '2':
            new_column = list(map(int, input("Enter the new column (space-separated values): ").split()))
            add_column(new_column)
        elif choice == '3':
            display_grid()
        elif choice == '4':
            total = sum_of_grid()
            print("Sum of all elements in the grid:", total)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please enter a valid option.")

if __name__ == "__main__":
    main()
