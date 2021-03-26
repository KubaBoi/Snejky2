from setuptools import setup
from Cython.Build import cythonize
from os import walk
from shutil import copyfile, move, rmtree
import os
import os.path
import time

path = "EngineSource"
distPath = "EnginePyx"
cPath = "Engine"

if (os.path.exists(cPath) and not os.path.exists(path)):
    os.rename(cPath, path)

#odstrani predchozi build
if (os.path.exists(distPath)):
    print(f"Removing {distPath}")
    rmtree(distPath)

if (os.path.exists(cPath)):
    print(f"Removing {cPath}")
    rmtree(cPath)

#zkopiruje zdrojove kody a zmeni priponu na .pyx
for (dirpath, dirnames, filenames) in walk(path):
    try:
        os.mkdir(dirpath.replace(path, distPath))
        os.mkdir(dirpath.replace(path, cPath))
    except:
        print(dirpath)

    for f in filenames:
        copyfile(dirpath + "\\" + f, dirpath.replace(path, distPath) + "\\" + f + "x")

#vytvori .c soubory
for (dirpath, dirnames, filenames) in walk(distPath):
    for f in filenames:
        setup(ext_modules = cythonize(dirpath + "\\" + f))

        name = f.replace("pyx", "") + "cp39-win_amd64.pyd"
        cName = f.replace("pyx", "c")
        while (not os.path.exists(name)):
            time.sleep(0.1)
        move(name, dirpath.replace(distPath, cPath) + "\\" + name) #move .pyd soubory
        move(dirpath + "\\" + cName, dirpath.replace(distPath, cPath) + "\\" + cName) #move .c soubory