import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def animate(game, interval=100):
    fig, ax = plt.subplots()
    image = ax.imshow(game.grid, cmap="binary", vmin=0, vmax=1)
    ax.set_axis_off()

    def update(frame):
        game.step()
        image.set_data(game.grid)
        return [image]

    anim = FuncAnimation(fig, update, interval=interval, cache_frame_data=False)
    plt.show()
