# Tools to be shared across sorting algorithms

# swap that makes new entry to states-list and focus-list
def swap(a, b, states, focus):
    new = states[-1].copy()
    temp = new[a]
    new[a] = new[b]
    new[b] = temp
    states.append(new)
    focus.append([a, b])
