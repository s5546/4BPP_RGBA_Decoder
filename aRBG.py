import numpy as np
from PIL import Image

filename = input("Enter a filename (or absolute path)")
pixels = []
with open(filename, "r") as f:
    line = f.readline()
    count = 1
    x = y = 0
    for space in line:
        if space == " ":
            x += 1
    x += 1
    # count occurances of space character and add 1 for x
    while line:
        line = f.readline()
        y += 1
    print(x, y)
    f.seek(0)
    line = f.readline()
    while line:
        colorArray = line.split(" ")
        # convert each hex character into a decimal value
        #    do this by advancing one character, and then converting it
        try:
            r = int(f.read(1), 16) * 16
            g = int(f.read(1), 16) * 16
            b = int(f.read(1), 16) * 16
            a = int(f.read(1), 16) * 16
            f.read(1)
            pixels.append((r, g, b, a))
        except ValueError:
            print("ok i guess its over")
            break
        count += 1
print(len(pixels))
img = Image.new("RGBA", (x, y))
img.putdata(pixels)
img.save(filename + "_output.png")

print("saved?")
