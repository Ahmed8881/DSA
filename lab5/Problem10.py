import time

# Initialize an empty list
numbers = []

# Record the time taken for each append operation
times = []

# Append integers from 1 to 100 and track time
for i in range(1, 101):
    start_time = time.perf_counter()
    numbers.append(i)
    end_time = time.perf_counter()
    
    # Calculate the time taken to append
    append_time = end_time - start_time
    times.append(append_time)

# Print results
for i in range(100):
    print(f"Time to append {i+1}: {times[i]} seconds")