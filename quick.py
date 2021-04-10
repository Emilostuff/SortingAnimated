# Fun Sort
import random


def sort(states, focus):
    def swap(i1, i2):
        new = states[-1].copy()
        temp = new[i1]
        new[i1] = new[i2]
        new[i2] = temp

        # save the move
        states.append(new)
        focus.append([i1, i2])

    def sort_range(arr, start, end):
        if end-start < 1:
            return

        # find pivot and move to end
        pivot = random.randint(start, end)
        swap(pivot, end)

        while True:
            # find left
            left = end
            for i in range(start, end):
                if states[-1][i] > states[-1][end]:
                    left = i
                    break

            # find right
            right = 0
            for i in range(0, end-start):
                if states[-1][end-i] < states[-1][end]:
                    right = end-i
                    break

            if left < right:
                swap(left, right)
            elif end-start > 0:
                sort_range(arr, start, left-1)
                sort_range(arr, left, end)
                return
            else:
                return

    # sorting
    print("Quick Sort")
    sort_range(states[0], 0, len(states[0]) - 1)