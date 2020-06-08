# This excercise was made by JuanMa using python3
# To execute it write on terminal "python3 problem-one.py" in the containing folder

if __name__ == "__main__":
    # Receiving inputs with size and array
    size, line = int(input()), input()
    # converting the input in the array and declaring the swaps variable
    arr, swaps = [int(i) for i in line.split()], 0
    # Bubble sort
    for i in range(size):
        for j in range(size - 1):
            if(arr[j] > arr[j + 1]):
                # incrementing the swaps counter
                swaps += 1
                aux = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = aux

    print("Array is sorted in ", swaps, " swaps.")
    print("First element: ", arr[0])
    print("Last element: ", arr[len(arr) - 1])
