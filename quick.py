# Fun Sort
import random


def sort(states, focus):
    print("Fun Sort")
    print()
    n = len(states[0])

    # sorting
    sort_range(states[0], 0, n-1)


def sort_range(arr, start, end):
    if end-start < 1:
        return

    pivot = random.randint(start, end)

    print("pivot: " + str(pivot) + ", start: " + str(start) + ", end: " + str(end))

    # move pivot
    swap(arr, pivot, end)

    # sort
    while True:
        # find left
        left = end
        for i in range(start, end):
            if arr[i] > arr[end]:
                left = i
                break

        # find right
        right = 0
        for i in range(0, end-start):
            if arr[end-i] < arr[end]:
                right = end-i
                break
                
        if left < right:
            swap(arr, left, right)
        elif end-start > 0:
            sort_range(arr, left, end)
            sort_range(arr, start, left-1)
            return
        else:
            return


def swap(arr, i1, i2):
    print("swap: " + str(i1) +" and " + str(i2))
    temp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = temp
    print(arr)
    print()


# setup
n = 25
states = []
init = list(range(1, n + 1))
random.shuffle(init)
states.append(init)

focus = [[-1, -1]]

print(states)

# sort
sort(states, focus)