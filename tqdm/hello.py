
import time
from tqdm import *

for i in tqdm(range(100), desc="Akagi201", leave=True):
    time.sleep(0.01)

for i in trange(100):
    time.sleep(0.01)

for i in tqdm(xrange(100)):
    time.sleep(0.01)