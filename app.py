import os.path

from PIL import Image

import click

@click.command()
@click.option('-t', '--tiles', type=int, default=8, help='Number of tiles to repeat.')
@click.argument('target_image')
def tile_image(tiles, target_image):
    # Opens an image
    bg = Image.open(target_image)

    # The width and height of the background tile
    bg_w, bg_h = bg.size

    # Creates a new empty image, RGB mode, and size 1000 by 1000
    new_im = Image.new('RGB', (bg_w*tiles,bg_h*tiles))

    # The width and height of the new image
    w, h = new_im.size

    # Iterate through a grid, to place the background tile
    for i in range(0, w, bg_w):
        for j in range(0, h, bg_h):
            # Change brightness of the images, just to emphasise they are unique copies
            # bg = Image.eval(bg, lambda x: x+(i+j)/1000)

            #paste the image at location i, j:
            new_im.paste(bg, (i, j))

    filename, file_ext = os.path.splitext(target_image)

    output_image = f'{filename}.{tiles}{file_ext}'

    new_im.show()
    new_im.save(output_image)

if __name__ == '__main__':
    tile_image()