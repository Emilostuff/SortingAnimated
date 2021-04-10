# Cocktail Sort
import tools


def sort(states, focus):

    print("Cocktail Sort")
    while True:
        success = True

        last = 0
        for i in range(len(states[0])-1):
            if states[-1][i] > states[-1][i+1]:
                tools.swap(i, i+1, states, focus)
                last = i
                success = False

        if success:
            return

        for i in range(last, 0, -1):
            if states[-1][i] > states[-1][i+1]:
                tools.swap(i, i+1, states, focus)

