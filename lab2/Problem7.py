import funcs
import time
import Insertion as IM
import HybridMerge as HM
import MergeSort as MS
import Bubble as BS
import Selection as SS



def Calculate_Run_Time():
    n = funcs.ReadFile("Nvalues.txt")  # 'n' is a list of integers
    Results = []
    
    for i in n:
        line = []
        line.append(i)
        
        # Insertion Sort
        array = funcs.RandomArray(i)  # Pass 'i' (integer) instead of 'n' (list)
        start_time = time.time()
        new = IM.InsertionSort(array, 1, i)
        end_time = time.time()
        run_time = end_time - start_time
        line.append(run_time)
        
        # Merge Sort
        array = funcs.RandomArray(i)  # Pass 'i' (integer) instead of 'n' (list)
        start_time = time.time()
        MS.MergeSort(array, 0, i-1)
        end_time = time.time()
        run_time = end_time - start_time
        line.append(run_time)
        
        # Hybrid Merge Sort
        array = funcs.RandomArray(i)  # Pass 'i' (integer) instead of 'n' (list)
        start_time = time.time()
        HM.HybridMerge(array, 0, i-1)
        end_time = time.time()
        run_time = end_time - start_time
        line.append(run_time)
        
        # Selection Sort
        array = funcs.RandomArray(i)  # Pass 'i' (integer) instead of 'n' (list)
        start_time = time.time()
        SS.SelectionSort(array, 0, i)
        end_time = time.time()
        run_time = end_time - start_time
        line.append(run_time)
        
        # Bubble Sort
        array = funcs.RandomArray(i)  # Pass 'i' (integer) instead of 'n' (list)
        start_time = time.time()
        BS.BubbleSort(array, 0, i)
        end_time = time.time()
        run_time = end_time - start_time
        line.append(run_time)
        
        Results.append(line)
        funcs.WriteFile("Results.txt", Results)

if __name__ == "__main__":
    Calculate_Run_Time()
    print("Results are saved in Results.txt file")
