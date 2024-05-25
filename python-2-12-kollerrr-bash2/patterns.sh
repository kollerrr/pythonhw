## Паттерны (шаблоны), регулярки

#!/bin/bash

# GLOB

# * - any string, including non-filled string
# ? - any single symbol
# [..] - any symbol from brackets

filename="some.jpg" # присвоение, пробелы нужны
if [[ filename = *.jpg || $filename = *.jpeg ]]; then # сравнение, пробелы не нужны
    echo "$filename is a jpeg"
fi

# Extended glob

#shopt -s 

?(list) - 0 или 1 совпадение
*(list) - 0 или больше совпадений
+(list) - 1 или больше
@(list) - один из данных паттернов
!(list) - все, кроме указанных паттернов

# можно разделять список внутри скобок симовлом |

# echo +(*deb | tar.gz)

# Regular expresions (regex)

str="hello, world"
r='*,'
if [[ $str =~ r ]]; then
    echo match
else
    echo not match
fi

# 0 true, 1 false, 2 error in regex

# .*[]^${}\+?|()  метасимволы

# Якорные символы
^ - привязывает шаблон к началу строки

echo "welcome to sirius" | awk '/^sirius/{print $0}'
echo "sirius college" | awk '/^sirius/{print $0}'

$ - привязывает шаблон к концу строки

echo "welcome to sirius" | awk '/^sirius${print $0}'
echo "welcome to sirius" | awk '/^sirius${print $0}'