# Merge Sort
import random
import tools


def sort(states, focus):
    def merge(start1, end1, start2, end2):
        # split up further until one element remains
        if end1-start1 > 0:
            print("a")
            divider = max(start1, (start1+end1)//2)
            merge(start1, divider,  divider + 1,  end1)

        if end2-start2 > 0:
            print("b")
            divider = max(start2, (start2 + end2) // 2)
            merge(start2, divider,  divider+1,  end2)

        # At this point the two sub ranges are now sorted –> merge in place
        print(str(start1) + ", " + str(end1) + ", " + str(start2) + ", " + str(end2))
        print(states[-1])
        a = start1
        b = start2
        while a != b and b <= end2 and a <= end2:
            print(str(a) + ", " + str(b))
            if states[-1][b] < states[-1][a]:
                # shift element
                tools.shift_right(a, b, states, focus)
                a += 1
                b += 1
            else:
                a += 1

    # sorting
    merge(0, len(states[-1])//2 - 1, len(states[-1])//2, len(states[-1])-1)
