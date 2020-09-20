import random
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation

# game of life
board_size = 10

# official rules

def create_board():
    # create board of all dead cells
    arr = []
    temp = []
    for i in range(board_size):
        for j in range(board_size):
            #temp.append(random.randint(0, 1))
            temp.append(0)
        arr.append(temp)
        temp = []
    # randomly input a live cell
    rand_x_place = random.randint(0, board_size-1)
    rand_y_place = random.randint(0, board_size-1)
    arr[rand_x_place][rand_y_place] = 1
    print(arr)
    return arr
arr = create_board()

# loop rules
def generate_data(arr):
    # randomly input a live cell
    rand_x_place = random.randint(0, board_size-1)
    rand_y_place = random.randint(0, board_size-1)
    print(rand_x_place, rand_y_place)
    arr[rand_x_place][rand_y_place] = 1
    return arr

# create and display dynamically updating grid
# https://stackoverflow.com/questions/10429556/animate-quadratic-grid-changes-matshow
def update(data):
    mat.set_data(data)
    return mat

def data_gen(arr):
    while True:
        yield generate_data(arr)

fig, ax = plt.subplots()
mat = ax.matshow(generate_data(arr))
plt.colorbar(mat)
ani = animation.FuncAnimation(fig, update, data_gen(arr), interval=500,
                              save_count=50)

plt.show()