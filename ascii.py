import os
import time
from PIL import Image
import moviepy.editor as mp


def image_to_ascii(img, cols=80, rows=40):
    width, height = img.size
    new_width = cols
    new_height = int(height * (new_width / width))
    img = img.resize((new_width, new_height), 1)

    ascii_grid = []
    for y in range(new_height):
        ascii_row = ""
        for x in range(new_width):
            grayscale = img.getpixel((x, y))
            chars = "@%#&%*+-.:"
            ascii_char = chars[int(grayscale / 255 * len(chars) - 1)]
            ascii_row += ascii_char
        ascii_grid.append(ascii_row)

    return '\n'.join(ascii_grid)


def gif_to_ascii(gif_path, cols=80, rows=40):
    clip = mp.VideoFileClip(gif_path)
    frames = []
    for frame in clip.iter_frames():
        frame_image = Image.fromarray(frame).convert('L')
        frame_ascii = image_to_ascii(frame_image, cols, rows)
        frames.append(frame_ascii)

    return frames


def animate_ascii(path, cols, rows):
    frames = gif_to_ascii(path, cols, rows)

    while True:
        for frame in frames:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(frame)
            time.sleep(0.1)


def convert_img_to_ascii(pathname, cols, rows):
    img = Image.open(pathname).convert('L')

    ascii_img = image_to_ascii(img, cols, rows)
    print(ascii_img)
