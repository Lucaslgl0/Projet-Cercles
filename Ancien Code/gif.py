import os
import imageio


with imageio.get_writer("gif_basique.gif", mode="I") as writer:
    for filename in [
        "fractale n=1.png",
        "fractale n=2.png",
        "fractale n=3.png",
        "fractale n=4.png",
        "fractale n=5.png",
        "fractale n=6.png",
        "fractale n=7.png",
        "fractale n=8.png",
    ]:
        image = imageio.imread(filename)
        writer.append_data(image)
