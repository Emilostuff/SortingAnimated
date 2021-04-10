# Insertion Sort
import tools


def sort(states, focus):

    for i in range(len(states[0]) - 1):
        for j in range(i+1):
            if states[-1][i-j] > states[-1][i-j + 1]:
                tools.swap(i-j, i-j + 1, states, focus)
            else:
                break
