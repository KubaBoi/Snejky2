from setuptools import setup
from Cython.Build import cythonize
from os import walk
from shutil import copyfile, move
import os
import os.path
import time

path = "EngineSource"
distPath = "Engine"

#zkopiruje zdrojove kody a zmeni priponu na .pyx
for (dirpath, dirnames, filenames) in walk(path):
    try:
        os.mkdir(dirpath.replace(path, distPath))
    except:
        print(dirpath)

    for f in filenames:
        copyfile(dirpath + "\\" + f, dirpath.replace(path, distPath) + "\\" + f + "x")

#vytvori .c soubory
for (dirpath, dirnames, filenames) in walk(distPath):
    for f in filenames:
        setup(ext_modules = cythonize(dirpath + "\\" + f))
        name = f.replace(".pyx", "") + ".cp39-win_amd64.pyd"
        while (not os.path.exists(name)):
            time.sleep(0.1)
        move(name, dirpath + "\\" + name)