from setuptools import setup
from Cython.Build import cythonize
from os import walk
from shutil import copyfile
import os

path = "EngineSource"
distPath = "Engine"

for (dirpath, dirnames, filenames) in walk(path):
    try:
        os.mkdir(dirpath.replace(path, distPath))
    except:
        print(dirpath)

    for f in filenames:
        copyfile(dirpath + "\\" + f, dirpath.replace(path, distPath) + "\\" + f + "x")


for (dirpath, dirnames, filenames) in walk(distPath):
    for f in filenames:
        setup(ext_modules = cythonize(dirpath + "\\" + f))