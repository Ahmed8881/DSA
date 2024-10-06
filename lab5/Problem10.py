import time
integer_list = []
time_list = []

for i in range(1, 101):
    start_time = time.perf_counter()
    integer_list.append(i)
    end_time = time.perf_counter()
    run_time = end_time - start_time
    time_list.append(run_time)

for i in range(100):
    print("Time to append " + str(i+1) + ": " + str(time_list[i]) + " seconds")