# importing libraries
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import bubble
import quick

# PARAMETERS
n = 20  # choose size of list
sort = 'quick'  # Choose sorting method
out = 'show'  # Choose output format [show, gif]


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


# make initial scrambles list
states = []
init = list(range(1, n + 1))
random.shuffle(init)
states.append(init)
focus = [[-1, -1]]


if sort == 'bubble':
    bubble.sort(states, focus)
elif sort == 'quick':
    quick.sort(states, focus)
else:
    sys.exit()

print("Done! " + str(len(states)) + " were performed.")


# duplicate last frame, but without highlight coloring
states.append(states[-1].copy())
focus.append([-1, -1])


# animate
ani = animation.FuncAnimation(fig, animate, interval=50, fargs=[states, focus], frames=len(states)+30)

if out == 'show':
    plt.show()
elif out == 'gif':
    # last frame corrections
    if True:
        states.append(states[0].copy())
        focus.append([-1, -1])

    ani.save('export/' + sort + str(n) + '.gif', 'pillow')
