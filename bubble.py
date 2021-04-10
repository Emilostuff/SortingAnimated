# Bubble Sort
import tools


def sort(states, focus):

    print("Bubble Sort")
    while True:
        success = True

        for i in range(len(states[0])-1):
            if states[-1][i] > states[-1][i+1]:
                tools.swap(i, i+1, states, focus)
                success = False

        if success:
            return
