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
    print('Maintenance Break')
    print('Tool will come soon')
elif bit == '32bit':
    os.system('clear')
    os.system('git pull')
    print('Sorry But Your Mobile Dosent Support  This Tool')
