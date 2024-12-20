import os
import time

print(os.getcwd())
os.chdir(r'C:\Users\Student\Desktop')
print(os.getcwd())
try:
    os.mkdir('new_folder')
except FileExistsError:
    pass

time.sleep(2)
os.rename('new_folder', 'new_folder2')
time.sleep(2)
os.rmdir('new_folder2')

os.system('cmd /c "cd C:\\Users\\Student\\Desktop\\Public && \
          dir >> dane.txt"')