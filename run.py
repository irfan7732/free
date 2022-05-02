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
    from irfan32 import ___RecodeSampah__
    ___RecodeSampah__()
elif bit == '32bit':
    os.system('clear')
    os.system('git pull')
    print('Sorry But Your Mobile Dosent Support  This Tool')
