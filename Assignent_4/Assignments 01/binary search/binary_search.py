import random
import time

def naive_search(l, target):
    # Example: l = [1,3,10,12]                                 
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1  # This should be outside the loop

# Binary Search using Divide & Conquer
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1    

    # Correcting midpoint calculation
    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif l[midpoint] < target:
        # Search right half
        return binary_search(l, target, midpoint + 1, high)
    else:
        # Search left half
        return binary_search(l, target, low, midpoint - 1)

# Running the functions
if __name__ == "__main__":
    length = 10000  # Corrected spelling from "lenght" to "length"
    sorted_list = set()
    
    # Generate unique random numbers
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3 * length, 3 * length))
    
    sorted_list = sorted(list(sorted_list))  # Convert set to sorted list

    # Measure Naive Search Time
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)  # ✅ Corrected
    end = time.time()
    print("Naive Search Time:", (end - start) / length, "seconds")

    # Measure Binary Search Time
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)  # ✅ Corrected
    end = time.time()
    print("Binary Search Time:", (end - start) / length, "seconds")
