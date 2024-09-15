import time
import funcs
import Insertion as IS
import MergeSort as MS

def Shuffle():
    words = funcs.ReadWords("words.txt")
    Array1=[]
    start_time = time.time()
    IS.InsertionSort(words, 0, len(words)-1)
    end_time = time.time()
    run_time = end_time - start_time
    Array1.append(run_time)
    
    start_time = time.time()
    MS.MergeSort(words, 0, len(words)-1)
    end_time = time.time()
    run_time = end_time - start_time
    Array1.append(run_time)
    
    funcs.ShuffleArray(words,0,len(words)-1)
    
    Array2=[]
    start_time = time.time()
    IS.InsertionSort(words, 0, len(words)-1)
    end_time = time.time()
    run_time = end_time - start_time
    Array2.append(run_time)
    
    start_time = time.time()
    MS.MergeSort(words, 0, len(words)-1)
    end_time = time.time()
    run_time = end_time - start_time
    Array2.append(run_time)
    
    print("Before Shuffle",Array1)
    print("After Shuffle",Array2)
    
if __name__ == "__main__":
    Shuffle()
    
    
    