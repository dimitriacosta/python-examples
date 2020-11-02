import os

os.chdir('/Users/dimitri')

for filename in os.listdir():
    if filename.endswith('.txt'):
        #  os.unlink(filename)
        print(filename)
