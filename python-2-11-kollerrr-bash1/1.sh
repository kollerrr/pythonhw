!/bin/bash

# табуляция не важна, важны пробелы и разные ' "
# and -a
# or -o

echo 'today is' `date`  # print analog
echo '\n введите путь к директории'
read the_path

echo -e '\n путь содержит следующие файлы и папки:'
ls $the_path

# chmod user u+x 1.sh - это прописать в терминале (даем доступ)

# variables
country=Russia # присвоение
same_country=$country # обращение
echo $country

# input/output
read the_path   #read from terminal

while read line    #read from file
do
    echo $line
done < input.txt

# command line args
# передаются в скрипт под именами $1, $2, $3, ...
echo 'hello, $1!'

# output
echo 'hello'
echo 'text for file' > output.txt # перезапись файла
echo 'other text for file' > output.txt # пишется в конец файла

ls >> output.txt # результат работы ls заипшется в файл

# if else
if [ [ condition ] ];
then
    statement
elif [ [ condition ] ]; then
    statement
else
    default statement # по умолчанию, если условие не выполняется
fi  # завершение всех условий

echo "enter the number: "
read num

if [ $num -gt 0 ]; then # greater than
    echo "$num is positive"
elif  [ $num -lt 0 ]; then
    echo "$num is negative"
else
    echo "$num is zero"
fi

# loops
# while
i=1
while [ $i -le 10 ]; do #less equals
    echo "$i"
    i=$(( $i +1 )) # присваиваем значение выражению, а после - переменной i
done

for i in {1..5} # значение включено в интервал 
# for i in {0..10..2} # все четные, от 0 до 10 включительно (интервал 2)
do
    echo $i
done


for (( i=0; i<=10; i++ )) # синтаксис похож на C, шаг один ++
do 
    echo $i
    if [ $i -eq 5 ]: then
        i = 8
    fi
done
