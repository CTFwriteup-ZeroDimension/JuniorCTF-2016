# Clone Attack
All the pictures look the same, but if we use diff to compare them, we see that every picture is different. To look at which part of the picture is different, I use xxd to make the binary file store in hex presentation. With diff command, we can find that only three bytes are different and the difference characters are numbers. It comes to my mind that it may be the serial number of the cloned Dipper, so I write a python script to checkout, and BINGO. One picture does not have numbers. Strings the picture and it says the flag is the md5sum of the picture.  
``` python3
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
```

