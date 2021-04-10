# importing libraries
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import bubble
import quick

# plot setup
fig = plt.figure()


def animate(i, data, highlight):
    index = min(i, len(data)-1)
    size = len(data[0])
    fig.clear()

    # create highlight color array
    colors = []
    for j in range(size):
        colors.append('silver')

    if highlight[index][0] != -1:
        colors[highlight[index][0]] = 'peru'

    if highlight[index][1] != -1:
        colors[highlight[index][1]] = 'firebrick'

    plt.bar(list(range(1, size+1)), data[index], align='edge', color=colors)
    plt.ylim([0, size])
    plt.xlim([1, size+1])
    plt.axis('off')
    plt.tight_layout(pad=3)


# setup
n = 25
states = []
init = list(range(1, n + 1))
random.shuffle(init)
states.append(init)

focus = [[-1, -1]]

# sort
#bubble.sort(states, focus)
quick.sort(states, focus)

# duplicate last frame, but without highlight coloring
states.append(states[len(states)-1].copy())
focus.append([-1, -1])



# plot the result
ani = animation.FuncAnimation(fig, animate, interval=50, fargs=[states, focus], frames=len(states)+30)
# plt.show()
# ani.save('bubbleSort.gif', 'pillow')
