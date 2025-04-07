import os,sys,platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x sarkar')
    os.system('./sarkar')
elif bit == '32bit':
    os.system('chmod +x sarkar32')
    os.system('./sarkar32')
else:
    print('device not supported')
