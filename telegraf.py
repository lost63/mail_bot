import subprocess
import path
import time
import _email2
import sys

while True:
    try:
        subprocess.call(['python3.8 '+path.path+'recive_parse_email.py'],shell=True, timeout=14)
        subprocess.call(['python3.8 '+path.path+'send_parse_email.py'],shell=True,timeout=14)
    except Exception as e:
        _email2.send_email('Ошибка', 'Exception in module telegraf, line 11' + str(e), 'test1@gmail.com')
        sys.exit(1)
    time.sleep(30)
