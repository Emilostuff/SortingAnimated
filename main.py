# importing libraries
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# plot setup
fig = plt.figure()


def animate(i, size, data):
    fig.clear()
    plt.bar(list(range(1, size+1)), data[min(i, len(data)-1)], align='center', color='blue')


# set initial conditions
n = 50
states = []
initState = list(range(1, n+1))
random.shuffle(initState)
states.append(initState)


# generate sorting steps
for j in range(n):
    for k in range(1, n-j):
        current = states[len(states)-1].copy()
        if current[j+k] < current[j]:
            # swap
            temp = current[j+k]
            current[j+k] = current[j]
            current[j] = temp
            states.append(current)

swaps = len(states)-1
print("Number of swaps performed: " + str(swaps))


# plot the result
ani = animation.FuncAnimation(fig, animate,interval=20, fargs=[n, states], frames=swaps+50)
#plt.show()
ani.save('bubbleSort.gif', 'pillow')
