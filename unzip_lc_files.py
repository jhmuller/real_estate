import os
import zipfile
from zipfile import ZipFile

mod_path = __file__
mod_dir = os.path.split(mod_path)[0]

zdir = os.path.join(".", "zip")
os.listdir()
zfiles = os.listdir(zdir)
for fname in zfiles:
    fpath = os.path(zdir, fname)
    print (fpath)

if __name__ == '__main__':
    pass