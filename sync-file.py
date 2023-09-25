import os
from dirsync import sync
from pathlib import Path

'''
using dirsync to sync files from one folder to another
'''
# get the base directory
BASE_DIR = Path(__file__).resolve().parent
# print(BASE_DIR)

# define origin and destination directories
orgin_dir = os.path.join(BASE_DIR, 'source')
destination_dir = os.path.join(BASE_DIR, 'destination')

# sync files using sync method
results = sync(orgin_dir, destination_dir, action='sync')
print(results)