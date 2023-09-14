import subprocess
import os
import time

while True:
    #output = subprocess.getoutput("nc -w 5 -v -4 172.232.78.147 80")
    output = os.system("nc -w 10 -v -4 10.2.2.4 80")
    #time.sleep(10)
