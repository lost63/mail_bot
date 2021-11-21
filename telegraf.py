import subprocess
import path
import time

while True:
    try:
        subprocess.call(['python3.8 '+path.path+'recive_parse_email.py'],shell=True, timeout=14)
        subprocess.call(['python3.8 '+path.path+'send_parse_email.py'],shell=True,timeout=14)
    except subprocess.TimeoutExpired:
        pass
    time.sleep(30)