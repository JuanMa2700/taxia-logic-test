import math

# This excercise was made by JuanMa using python3
# To execute it write on terminal "python3 problem-one.py" in the containing folder


def media(arr):
    # if the array is empty we return an error
    if(len(arr) < 1):
        return "Wrong!"
    # Here we sort our array
    arr.sort()
    # return the middle element if the array length is odd, else return the division of the central two elements
    return arr[math.floor(len(arr) / 2)] if(len(arr) % 2) else '%g' % ((arr[int(len(arr) / 2)] + arr[int((len(arr) / 2) - 1)]) / 2)


if __name__ == "__main__":
    # Declare variables and receiving the first input with operations size
    arr, inputs, op_size = [], [], int(input())
    # Receiving the inputs with operations
    for i in range(op_size):
        inputs.append(input())
    # Evaluating each operation
    for i in range(op_size):
        # Taking the operation and the value in every input
        op, x = inputs[i].split()
        # for addition operation
        if(op is "a"):
            # append the new element
            arr.append(int(x))
            # Executing our media function and printing the resoult
            print(media(arr))
            # We don't need to evaluate anymore
            continue
        # for remove operation we validate that the element exist in our array
        elif (op is "r" and int(x) in arr):
            # removing the element
            arr.remove(int(x))
            # Executing our media function without the removed element and printing the resoult
            print(media(arr))
        # if the element doesn't exist we print Wrong!
        elif (op is "r"):
            print("Wrong!")
