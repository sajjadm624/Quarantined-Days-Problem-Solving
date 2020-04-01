def bubbleSort(arr): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n): 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print()
    
if __name__ == '__main__': 
    s = input()
    arr = list(map(int, s.split()))
    print ("Given array is", end="\n")  
    printList(arr) 
    bubbleSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr)