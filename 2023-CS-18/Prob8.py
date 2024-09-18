import time
import funcs
import Insertion as IS
import MergeSort as MS

if __name__=="__main__":
    words = funcs.ReadWords("words.txt")
    Array1=[]
    start_time = time.time()
    IS.InsertionSort(words, 0, len(words))
    end_time = time.time()
    run_time = end_time - start_time
    Array1.append(run_time)
    
    start_time = time.time()
    MS.MergeSort(words, 0, len(words)-1)
    end_time = time.time()
    run_time = end_time - start_time
    Array1.append(run_time)
    
    funcs.ShuffleArray(words,0,len(words))
    
    Array2=[]
    start_time = time.perf_counter()
    IS.InsertionSort(words, 0, len(words))
    end_time = time.perf_counter()
    run_time = end_time - start_time
    Array2.append(run_time)
    
    start_time = time.perf_counter()
    MS.MergeSort(words, 0, len(words)-1)
    end_time = time.perf_counter()
    run_time = end_time - start_time
    Array2.append(run_time)
    print("Before Shuffle [InsertionSort,MergeSort]",Array1)
    print("After Shuffle [InsertionSort,MergeSort]",Array2)