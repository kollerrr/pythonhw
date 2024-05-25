"""
Напишите скрипт-калькулятор, который принимает 3 аргумента:
1. первый аргумент
2. второй аргумент
3. операцию
и вычисляет результат
"""
import sys

def calc(arg1, arg2, operation):

    if operation == "+":
        return arg1 + arg2

    elif operation == "-":
        return arg1 - arg2

    elif operation == "*":
        return arg1*arg2

    elif operation == "/":
        if arg2 == 0:
            return('Division by zero')
        return arg1/arg2
   
    else:
        return('Operation is not supported')

def main():
   
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    operation = sys.argv[3]

    result = calc(arg1, arg2, operation)
    print(result)

if __name__ == "__main__":
    main()