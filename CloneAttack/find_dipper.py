import glob
import sys

for file_name in glob.glob('*.jpg'):
    with open(file_name, 'rb') as fp:
        img = fp.read()
    try:
        code = int(img[0x68:0x68+3])
    except:
        print('no code:', file_name)
    if img == 0:
        print('number 0', file_name)

