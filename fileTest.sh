#!/bin/sh

# Делим аргумент (e.g., '2.1-a') на номер папки '2.1'
DIR=$(echo $1 | cut -d'-' -f1)
# И номер теста 'a', переводя букву в нижний регистр
FILE=$(echo $1 | cut -d'-' -f2 | tr '[:upper:]' '[:lower:]')

# Убираем точку 'DIR' ('2.1' -> '21')
DIR_NO_DOT=$(echo $DIR | sed 's/\.//g')

# Запускаем pytest на выбранном файле
pytest tests/$DIR/test_${DIR_NO_DOT}_$FILE.py
