# Tools to be shared across sorting algorithms

# swap that makes new entry to states-list and focus-list
def swap(i1, i2, states, focus):
    new = states[-1].copy()
    temp = new[i1]
    new[i1] = new[i2]
    new[i2] = temp
    states.append(new)
    focus.append([i1, i2])
