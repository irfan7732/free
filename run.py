import os, platform
try:
    import requests
except:
    os.system('pip2 install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('clear')
    os.system('git pull')
    os.system('clear')
    print(' \033[1;32mFacebook Is On Update All Method Are Going Lol')
    print(' \033[1;32mI will Try to Find New Method Inshaallah')
elif bit == '32bit':
    os.system('clear')
    os.system('git pull')
    print('Sorry But Your Mobile Dosent Support  This Tool')
