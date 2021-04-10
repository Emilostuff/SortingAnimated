# importing libraries
import sys
import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import bubble
import quick
import insertion

# PARAMETERS
n = 25  # choose size of list
sort = 'insertion'  # Choose sorting method
out = 'gif'  # Choose output format [show, gif]
interval = 50  # Delay between steps
looping = False  # Animation should loop?


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

    offset = n/8

    plt.bar(list(range(1, size+1)), data[index], align='edge', color=colors)
    plt.ylim([0, size+offset])
    plt.xlim([1, size+1])
    plt.axis('off')
    plt.tight_layout(pad=3)
    plt.text(1, n+2*offset/3, sort.capitalize() + " Sort ", fontsize=20,
             fontweight="bold", horizontalalignment='left', color="#252525")


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
elif sort == 'insertion':
    insertion.sort(states, focus)
else:
    sys.exit()

print("Done! " + str(len(states)) + " swaps were performed.")


# duplicate last frame, but without highlight coloring
states.append(states[-1].copy())
focus.append([-1, -1])


# animate
ani = animation.FuncAnimation(fig, animate, interval=interval, fargs=[states, focus], frames=len(states)+interval*3, repeat=looping)

if out == 'show':
    plt.show()
elif out == 'gif':
    # last frame corrections
    if True:
        states.append(states[0].copy())
        focus.append([-1, -1])

    # create output folder if it doesn't exist
    if not os.path.exists('export'):
        os.makedirs('export')

    ani.save('export/' + sort + str(n) + '.gif', 'pillow')
else:
    sys.exit()
