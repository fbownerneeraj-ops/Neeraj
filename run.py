import os,sys,platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x Neeraj')
    os.system('./Neeraj')
elif bit == '32bit':
    os.system('chmod +x Neeraj32')
    os.system('./khan32')
else:
    print('device not supported')
