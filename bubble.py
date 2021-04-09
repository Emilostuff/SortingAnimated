
def bubble_sort(states):
    print("Bubble Sort")

    n = len(states[0])

    for j in range(n):
        for k in range(1, n - j):
            current = states[len(states) - 1].copy()
            if current[j + k] < current[j]:
                # swap
                temp = current[j + k]
                current[j + k] = current[j]
                current[j] = temp
                states.append(current)

    swaps = len(states) - 1
    print("Done! Swaps performed: " + str(swaps))

    return swaps


