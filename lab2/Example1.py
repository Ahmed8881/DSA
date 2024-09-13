def factorial(n):
    if(n==0):
        return 1
    else:
        return n* factorial(n-1)

import time
start_time=time.perf_counter()
n=990
ans=factorial(n)
end_time=time.perf_counter()
run_time=end_time-start_time
print("Run time of factorial at", n,"is",run_time,"seconds")
