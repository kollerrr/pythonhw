"""
Напишите скрипт который выводит надпись "Hello, world",
 если не было передано никаких аргументов.
Если 1 из аргументов "--name" то следующий аргумент должен быть имя. 
В таком случае выведите надпись "Hello, {Имя}"
Пример ввода: python file.py Argument --name John
Пример вывода: Hello, John
"""
import sys

args = sys.argv[1:]

if not args:
    print('Hello, world')

elif args[0] == '--name':
    name = args[1]
    print(f'Hello, {name}')
    
else:
    print('Unexpected arg')