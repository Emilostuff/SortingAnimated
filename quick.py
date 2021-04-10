# Quick Sort
import random
import tools


def sort(states, focus):
    def sort_range(arr, start, end):
        if end-start < 1:
            return

        # find pivot and move to end
        pivot = random.randint(start, end)
        tools.swap(pivot, end, states, focus)

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
                tools.swap(left, right, states, focus)
            elif end-start > 0:
                sort_range(arr, start, left-1)
                sort_range(arr, left, end)
                return
            else:
                return

    # sorting
    print("Quick Sort")
    sort_range(states[0], 0, len(states[0]) - 1)