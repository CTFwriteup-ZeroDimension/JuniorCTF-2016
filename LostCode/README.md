# LosT Code
Input 32 hex chars and the program returns a 32 0-1 string indicating whether each corresponding character is correct. So just bruteforce and make it return '1'*32. It just need to try 16*32=512 times!
``` python3
from subprocess import Popen, PIPE

flag = ['a'] * 32
for i in range(32):
    for s in '0123456789abcdef':
        flag[i] = s
        with Popen(['LosT.exe', '-b', ''.join(flag)], stdout=PIPE) as proc:
            result = proc.stdout.read().strip()
            if result[i] == 49:
                break
with open('flag.txt', 'w') as fp:
    fp.write(''.join(flag))
```
