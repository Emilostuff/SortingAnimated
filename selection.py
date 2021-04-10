# SelectionSort
import tools


def sort(states, focus):

    for i in range(len(states[0]) - 1):
        min = i
        for j in range(i+1, len(states[0])):
            if states[-1][j] < states[-1][min]:
                min = j
                # perform false swap to indicate the update of minimum value
                tools.swap(j, j, states, focus)

        if min != i:
            tools.swap(i, min, states, focus)
