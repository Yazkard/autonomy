import os

imdir = 'images'
if not os.path.isdir(imdir):
    os.mkdir(imdir)

ball_folders = [folder for folder in os.listdir('.') if 'tennis_balls' in folder]

n = 0
for folder in ball_folders:
    for imfile in os.scandir(folder):
        os.rename(imfile.path, os.path.join(imdir, '{:06}.png'.format(n)))
n += 1