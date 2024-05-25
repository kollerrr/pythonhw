"""
Напишите скрипт который принимает 2 аргумента и записывает 
первый аргумент в файл, где имя файла - второй аргумент.
"""

import sys

arg1 = sys.argv[1]
arg2 = sys.argv[2]

with open(arg2, "w") as file:
    file.write(arg1)