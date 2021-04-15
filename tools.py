# Tools to be shared across sorting algorithms

# swap that makes new entry to states-list and focus-list
def swap(a, b, states, focus):
    new = states[-1].copy()
    temp = new[a]
    new[a] = new[b]
    new[b] = temp
    states.append(new)
    focus.append([a, b])


def shift_right(start, end, states, focus):
    new = states[-1].copy()
    new[start: end+1] = new[end: end+1] + new[start: end]
    states.append(new)
    focus.append([start, end])

