# import time
from time import sleep, time_ns

print('Siema')
# time.sleep(3)

sleep(3)
print('papa')

try:
    age = int(input('Ile masz lat? '))
except ValueError:
    pass
