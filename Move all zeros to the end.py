def move_zeros_to_end(arr):
    
    i = 0
    for j in range(len(arr)):
        if arr[j] != 0:
            arr[i],arr[j] = arr[j],arr[i]
            i +=1
          

if __name__ == "__main__":
  arr = [0, 1, 0, 3, 12]
  move_zeros_to_end(arr)
  print(arr)  # Output: [1, 3, 12, 0, 0]
