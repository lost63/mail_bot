import subprocess
import path
import time
import _email2
import sys

count=0
while True:
    try:
        subprocess.check_call(['python3.8 '+path.path+'recive_parse_email.py'],shell=True, timeout=14)
        subprocess.check_call(['python3.8 '+path.path+'send_parse_email.py'],shell=True, timeout=14)
    except subprocess.TimeoutExpired:
        _email2.send_email('Ошибка', 'Exception timeout subprocess, module telegraf, line 11 '+str(count), 'test1@gmail.com')
        count+=1
        if count > 5:
            sys.exit(1)
    except Exception as e:
        _email2.send_email('Ошибка', 'Exception in module telegraf, line 11' + str(e), 'test1@gmail.com')
        sys.exit(1)
    time.sleep(30)

