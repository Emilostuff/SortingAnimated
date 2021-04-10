# Comb Sort
import tools


def next_gap(gap):
    # Shrink gap by Shrink factor
    gap = (gap * 10) / 13
    if gap < 1:
        return 1
    return gap


def sort(states, focus):

    gap = len(states[0])-2
    success = True

    while success or gap != 1:
        success = False
        gap = next_gap(gap)

        for i in range(len(states[0])-int(gap)):
            if states[-1][i] > states[-1][i+int(gap)]:
                tools.swap(i, i+int(gap), states, focus)
                success = False

