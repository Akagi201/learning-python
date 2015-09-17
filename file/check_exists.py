
import os

path = '/tmp/akdir'
file = '/tmp/akfile'

e = os.path.exists(path)
print(e)

e = os.path.exists(file)
print(e)