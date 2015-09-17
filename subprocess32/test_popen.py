
import subprocess
import string
import json

# child = subprocess.Popen(['ping', '-c', '4', 'www.baidu.com'], stdout=subprocess.PIPE)
# child = subprocess.Popen(['python', 'cerepos_umspay_cmd.py', 'func:sign_on'], stdout=subprocess.PIPE)
amount = 1.0
cmd = ["python", "/home/mm/kiosk/ckcerepos/ckcerepos/cerepos_umspay_cmd.py", "func:consume", "amount:"+str(amount)]
print("umspay sale: %s" % cmd)
child = subprocess.Popen(cmd, stdout=subprocess.PIPE)
child.wait()
print("umspay child.returncode: %s" % child.returncode)
if child.returncode == 0:
    res = child.stdout.read()
else:
    res = {"resp_code":"crash"}

child.wait()
print('parent process')
print("child.returncode: %s" % child.returncode)
print("child.stdout: %s" % res)
print("child.stdout type: %s" % type(res))
b = eval(res)
print("type(b): %s" % type(b))
# print("child.stdout json: %s" % json.loads(res))
