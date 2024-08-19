![Codacy grade (branch)](https://img.shields.io/codacy/grade/63f71a9c86ce4a0492af52c23628b78a/main)
![Build Status](https://github.com/andreypomortsev/yndx-python-handbook/actions/workflows/ci.yml/badge.svg)
[![codecov](https://codecov.io/gh/andreypomortsev/yndx-python-handbook/branch/main/graph/badge.svg?token=WPUYVICKGT)](https://codecov.io/gh/andreypomortsev/yndx-python-handbook)
![Python 3.12](https://img.shields.io/badge/Python-3.12-green.svg)
![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)

## Решения задач из учебника [Основы Python](https://education.yandex.ru/handbook/python) от Яндекс

_"Хендбук по Python поможет овладеть основным синтаксисом и принципами языка. Для этого не потребуется специальной подготовки — достаточно знаний по информатике, логике и математике на уровне школьной программы. Кроме основных конструкций в учебнике рассмотрены разные подходы к программированию, реализованные на Python."_ **Яндекс**

### Описание Проекта

Решения написаны мной, но некоторые варианты для тестов могут быть позаимствованы из [одноименного](https://t.me/handbook_python) телеграм канала. Решение задач подразумевает использование знаний полученных после изучения соответствующего параграфа.
Так же я решил покрыть тестами все свои решения, они не совпадают на 100% с тестами в учебнике, но при замене моего решения на ваш код, можно будет понять на каких данных не работает код или какие строчки не покрыты тестами (эти строки могут быть лишними). 

## Установка

### Клонируем репозиторий

```sh
git clone https://github.com/andreypomortsev/yndx-python-handbook
cd yndx-python-handbook
```

#### Создаем виртуальную среду

Все точно работает на [**Python 3.12.4**](https://www.python.org/downloads/release/python-3124/)
```sh
python3 -m venv .venv
```

#### Активируем виртуальную среду

- На macOS и Linux:

  ```sh
  source .venv/bin/activate
  ```

- На Windows:

  ```PowerShell
  .venv\Scripts\activate
  ```

#### Устанавливаемм все необходимое

```sh
pip3 install -r requirements
```

#### Запускаем тесты
Все тесты в репозитории:
```sh
pytest
```
Все тесты одного парагарафа (вместо `2.1` укажите нужный параграф) приведенный код запустит тесты для всех задач из параграфа [2.1](./solutions/2.1/):
```sh
pytest tests/2.1
```
Тест одной задачи (вместо `2.3` укажите нужный параграф, вместо `test_23_a.py` укажите тест для нужной задачи) приведенный код запустит тесты для задачи **A. Раз, два, три! Ёлочка, гори!**  из парагарафа [2.3](./solutions/2.3/):
```sh
pytest tests/2.3/test_23_a.py
```
Тесты с отчетом в `html`*:
_*можно использовать как для всех тестов так и для отдельных задач и параграфоф (папок)_
```sh
pytest --cov-report=html
```
после прохождения тестов открываем файл: `htmlcov/index.html`

Во время теста в папке `tests` временно создаются файлы `wrapped_*.py`.

<details>
<summary><h4>Почему создаются временные файлы?</h4></summary>

Для определения покрытия кода тестами обычно импортируется тестируемая функция, и инструмент coverage может наблюдать, какие строки исполнялись, а какие нет. Когда в файле решений нет функций, как в первых трех параграфах учебника, когда ещё не задано определение функции, мы можем протестировать код из файла, но не получить покрытия строк тестами. Поэтому я написал функцию `wrap_answer` [см. здесь](./tests/conftest.py). Эта функция запускается при старте тестов с параметрами: путь к тестируемому файлу и имя этого файла. Она считывает содержимое решения задачи из заданного файла, оборачивает его в функцию main и сохраняет в файл с именем `wrapped_(адрес папки)_(буква задачи).py`. Уже этот файл проверяется тестами, и coverage видит, какие строки выполнялись, а какие нет, что позволяет получить информацию о покрытии тестами решения.

**Пример:**

_Решение задачи Q из параграфа 2.2_
Файл `22_q.py` до:

```python
a = float(input())
b = float(input())
c = float(input())

if not a:
    if not b and not c:  # a == b == c == 0
        print("Infinite solutions")
    elif not b and c:  # a == b == 0 and c != 0
        print("No solution")
    else:  # a == 0 and b != 0 линейное уравнение
        print(round(-c / b, 2))
else:
    discriminant = b**2 - 4 * a * c
    if discriminant >= 0:
        root1 = round((-b + discriminant**0.5) / (2 * a), 2)
        root2 = round((-b - discriminant**0.5) / (2 * a), 2)
        if not discriminant:
            print(root2)
        elif root1 < root2:  # Условие выполняется при a < 0
            print(root1, root2)
        else:
            print(root2, root1)
    else:  # Дискриминант меньше 0
        print("No solution")

```

Файл `wrapped_22_q.py` после применения `wrap_answer` к `22_q.py`:
```python
def main():
    a = float(input())
    b = float(input())
    c = float(input())

    if not a:
      if not b and not c:  # a == b == c == 0
          print("Infinite solutions")
      elif not b and c:  # a == b == 0 and c != 0
          print("No solution")
      else:  # a == 0 and b != 0 линейное уравнение
          print(round(-c / b, 2))
    else:
      discriminant = b**2 - 4 * a * c
      if discriminant >= 0:
          root1 = round((-b + discriminant**0.5) / (2 * a), 2)
          root2 = round((-b - discriminant**0.5) / (2 * a), 2)
          if not discriminant:
              print(root2)
          elif root1 < root2:  # Условие выполняется при a < 0
              print(root1, root2)
          else:
              print(root2, root1)
      else:  # Дискриминант меньше 0
          print("No solution")
```

После того как отчет по покрытию готов, файлы удаляются. 

</details>

### Проверка Вашего кода

После клонирования репозитория выполните следующие шаги:

- Найдите код, который вам нужно проверить, и замените его на ваше решение.
  - Например у вас проблема с задачей [2.1 C](./solutions/2.1/c.py) заходите в файл вставляете свое решение, сохраняете и запускаете тесты.
- Сохраните изменения и запустите тесты.
- Проверьте покрытие кода тестами. Это покажет, сколько строк вашего кода было выполнено во время тестов. Если покрытие меньше 100%, это может указывать на то, что некоторые строки кода не нужны или не были протестированы.
- Если тесты не прошли, названия неудачных тестов будут выделены красным цветом. Перейдите в папку с тестами, откройте соответствующий файл и проверьте входные данные.
- Исправьте код в соответствии с выявленными проблемами, снова запустите тесты и повторяйте процесс до тех пор, пока все тесты не пройдут успешно.

Кроме правильного ответа Яндекс проверяет еще и на соответствие кода [PEP8](https://github.com/Searge/mipt_oop/blob/master/week_1/readme.md), поэтому научитесь пользоваться линтерами: [flake8](https://flake8.pycqa.org/en/latest/) или [pylint](https://pypi.org/project/pylint/) и форматером кода, я использую [black](https://black.readthedocs.io/en/stable/index.html).

## Решения | Тесты

<details>
<summary><h3>2.1 Ввод и вывод данных. Операции с числами, строками. Форматирование</h3></summary>

#### Для решения задач используется только материал из параграфа:
- [2.1 Ввод и вывод данных. Операции с числами, строками. Форматирование](https://education.yandex.ru/handbook/python/article/vvod-i-vyvod-dannykh-operatsii-s-chislami-strokami-formatirovaniye)
  
### [Тестовые данные для задач](./tests/data/test_data_21.py)
  
| Решение              | Тесты                |
|----------------------|----------------------|
| А. [Привет, Яндекс!](./solutions/2.1/21_a.py) | [✅](./tests/2.1/test_21_a.py) |
| B. [Привет, всем!](./solutions/2.1/21_b.py) | [✅](./tests/2.1/test_21_b.py) |
| C. [Излишняя автоматизация](./solutions/2.1/21_c.py) | [✅](./tests/2.1/test_21_c.py) |
| D. [Сдача](./solutions/2.1/21_d.py) | [✅](./tests/2.1/test_21_d.py) |
| E. [Магазин](./solutions/2.1/21_e.py) | [✅](./tests/2.1/test_21_e.py) |
| F. [Чек](./solutions/2.1/21_f.py) | [✅](./tests/2.1/test_21_f.py) |
| G. [Делу — время, потехе — час](./solutions/2.1/21_g.py) | [✅](./tests/2.1/test_21_g.py) |
| H. [Наказание](./solutions/2.1/21_h.py) | [✅](./tests/2.1/test_21_h.py) |
| I. [Деловая колбаса](./solutions/2.1/21_i.py) | [✅](./tests/2.1/test_21_i.py) |
| J. [Детский сад — штаны на лямках](./solutions/2.1/21_j.py) | [✅](./tests/2.1/test_21_j.py) |
| K. [Автоматизация игры](./solutions/2.1/21_k.py) | [✅](./tests/2.1/test_21_k.py) |
| L. [Интересное сложение](./solutions/2.1/21_l.py) | [✅](./tests/2.1/test_21_l.py) |
| M. [Дед Мороз и конфеты](./solutions/2.1/21_m.py) | [✅](./tests/2.1/test_21_m.py) |
| N. [Шарики и ручки](./solutions/2.1/21_n.py) | [✅](./tests/2.1/test_21_n.py) |
| O. [В ожидании доставки](./solutions/2.1/21_o.py) | [✅](./tests/2.1/test_21_o.py) |
| P. [Доставка](./solutions/2.1/21_p.py) | [✅](./tests/2.1/test_21_p.py) |
| Q. [Ошибка кассового аппарата](./solutions/2.1/21_q.py) | [✅](./tests/2.1/test_21_q.py) |
| R. [Сдача 10](./solutions/2.1/21_r.py) | [✅](./tests/2.1/test_21_r.py) |
| S. [Украшение чека](./solutions/2.1/21_s.py) | [✅](./tests/2.1/test_21_s.py) |
| T. [Мухи отдельно, котлеты отдельно](./solutions/2.1/21_t.py) | [✅](./tests/2.1/test_21_t.py) |

</details>
<details>
<summary><h3>2.2 Условный оператор</h3></summary>

#### Для решения задач используется только пройденный материал из параграфоф:
- [2.1 Ввод и вывод данных. Операции с числами, строками. Форматирование](https://education.yandex.ru/handbook/python/article/vvod-i-vyvod-dannykh-operatsii-s-chislami-strokami-formatirovaniye)
- [2.2 Условный оператор](https://education.yandex.ru/handbook/python/article/uslovnyy-operator)

### [Тестовые данные для задач](./tests/data/test_data_22.py)

| Решение              | Тесты                |
|----------------------|----------------------|
| А. [Просто здравствуй, просто как дела](./solutions/2.2/22_a.py) | [✅](./tests/2.2/test_22_a.py) |
| B. [Кто быстрее?](./solutions/2.2/22_b.py) | [✅](./tests/2.2/test_22_b.py) |
| C. [Кто быстрее на этот раз?](./solutions/2.2/22_c.py) | [✅](./tests/2.2/test_22_c.py) |
| D. [Список победителей](./solutions/2.2/22_d.py) | [✅](./tests/2.2/test_22_d.py) |
| E. [Яблоки](./solutions/2.2/22_e.py) | [✅](./tests/2.2/test_22_e.py) |
| F. [Сила прокрастинации](./solutions/2.2/22_f.py) | [✅](./tests/2.2/test_22_f.py) |
| G. [А роза упала на лапу Азора](./solutions/2.2/22_g.py) | [✅](./tests/2.2/test_22_g.py) |
| H. [Зайка — 1](./solutions/2.2/22_h.py) | [✅](./tests/2.2/test_22_h.py) |
| I. [Первому игроку приготовиться](./solutions/2.2/22_i.py) | [✅](./tests/2.2/test_22_i.py) |
| J. [Лучшая защита — шифрование](./solutions/2.2/22_j.py) | [✅](./tests/2.2/test_22_j.py) |
| K. [Красота спасёт мир](./solutions/2.2/22_k.py) | [✅](./tests/2.2/test_22_k.py) |
| L. [Музыкальный инструмент](./solutions/2.2/22_l.py) | [✅](./tests/2.2/test_22_l.py) |
| M. [Властелин Чисел: Братство общей цифры](./solutions/2.2/22_m.py) | [✅](./tests/2.2/test_22_m.py) |
| N. [Властелин Чисел: Две Башни](./solutions/2.2/22_n.py) | [✅](./tests/2.2/test_22_n.py) |
| O. [Властелин Чисел: Возвращение Цезаря](./solutions/2.2/22_o.py) | [✅](./tests/2.2/test_22_o.py) |
| P. [Легенды велогонок возвращаются: кто быстрее?](./solutions/2.2/22_p.py) | [✅](./tests/2.2/test_22_p.py) |
| Q. [Корень зла](./solutions/2.2/22_q.py) | [✅](./tests/2.2/test_22_q.py) |
| R. [Территория зла](./solutions/2.2/22_r.py) | [✅](./tests/2.2/test_22_r.py) |
| S. [Автоматизация безопасности](./solutions/2.2/22_s.py) | [✅](./tests/2.2/test_22_s.py) |
| T. [Зайка — 2](./solutions/2.2/22_t.py) | [✅](./tests/2.2/test_22_t.py) |

</details>

<details>
<summary><h3>2.3 Циклы</h3></summary>

#### Для решения задач используется только пройденный материал из параграфоф:
- [2.1 Ввод и вывод данных. Операции с числами, строками. Форматирование](https://education.yandex.ru/handbook/python/article/vvod-i-vyvod-dannykh-operatsii-s-chislami-strokami-formatirovaniye)
- [2.2 Условный оператор](https://education.yandex.ru/handbook/python/article/uslovnyy-operator)
- [2.3 Циклы](https://education.yandex.ru/handbook/python/article/cikly)

### [Тестовые данные для задач](./tests/data/test_data_23.py)

| Решение              | Тесты                |
|----------------------|----------------------|
| А. [Раз, два, три! Ёлочка, гори!](./solutions/2.3/23_a.py) | [✅](./tests/2.3/test_23_a.py) |
| B. [Зайка — 3](./solutions/2.3/23_b.py) | [✅](./tests/2.3/test_23_b.py) |
| C. [Считалочка](./solutions/2.3/23_c.py) | [✅](./tests/2.3/test_23_c.py) |
| D. [Считалочка 2.0](./solutions/2.3/23_d.py) | [✅](./tests/2.3/test_23_d.py) |
| E. [Внимание! Акция!](./solutions/2.3/23_e.py) | [✅](./tests/2.3/test_23_e.py) |
| F. [НОД](./solutions/2.3/23_f.py) | [✅](./tests/2.3/test_23_f.py) |
| G. [НОК](./solutions/2.3/23_g.py) | [✅](./tests/2.3/test_23_g.py) |
| H. [Излишняя автоматизация 2.0](./solutions/2.3/23_h.py) | [✅](./tests/2.3/test_23_h.py) |
| I. [Факториал](./solutions/2.3/23_i.py) | [✅](./tests/2.3/test_23_i.py) |
| J. [Маршрут построен](./solutions/2.3/23_j.py) | [✅](./tests/2.3/test_23_j.py) |
| K. [Цифровая сумма](./solutions/2.3/23_k.py) | [✅](./tests/2.3/test_23_k.py) |
| L. [Сильная цифра](./solutions/2.3/23_l.py) | [✅](./tests/2.3/test_23_l.py) |
| M. [Первому игроку приготовиться 2.0](./solutions/2.3/23_m.py) | [✅](./tests/2.3/test_23_m.py) |
| N. [Простая задача](./solutions/2.3/23_n.py) | [✅](./tests/2.3/test_23_n.py) |
| O. [Зайка - 4](./solutions/2.3/23_o.py) | [✅](./tests/2.3/test_23_o.py) |
| P. [А роза упала на лапу Азора 2.0](./solutions/2.3/23_p.py) | [✅](./tests/2.3/test_23_p.py) |
| Q. [Чётная чистота](./solutions/2.3/23_q.py) | [✅](./tests/2.3/test_23_q.py) |
| R. [Простая задача 2.0](./solutions/2.3/23_r.py) | [✅](./tests/2.3/test_23_r.py) |
| S. [Игра в «Угадайку»](./solutions/2.3/23_s.py) | [✅](./tests/2.3/test_23_s.py) |
| T. [Хайпанём немножечко!](./solutions/2.3/23_t.py) | [✅](./tests/2.3/test_23_t.py) |

</details>

<details>
<summary><h3>2.4 Вложенные циклы</h3></summary>

#### Для решения задач используется только пройденный материал из параграфоф:
- [2.1 Ввод и вывод данных. Операции с числами, строками. Форматирование](https://education.yandex.ru/handbook/python/article/vvod-i-vyvod-dannykh-operatsii-s-chislami-strokami-formatirovaniye)
- [2.2 Условный оператор](https://education.yandex.ru/handbook/python/article/uslovnyy-operator)
- [2.3 Циклы](https://education.yandex.ru/handbook/python/article/cikly)
- [2.4 Вложенные циклы](https://education.yandex.ru/handbook/python/article/vlozhennye-cikly)

### [Тестовые данные для задач](./tests/data/test_data_24.py)

| Решение              | Тесты                |
|----------------------|----------------------|
| А. [Таблица умножения](./solutions/2.4/24_a.py) | [✅](./tests/2.4/test_24_a.py) |
| B. [Не таблица умножения](./solutions/2.4/24_b.py) | [✅](./tests/2.4/test_24_b.py) |
| C. [Новогоднее настроение](./solutions/2.4/24_c.py) | [✅](./tests/2.4/test_24_c.py) |
| D. [Суммарная сумма](./solutions/2.4/24_d.py) | [✅](./tests/2.4/test_24_d.py) |
| E. [Зайка — 5](./solutions/2.4/24_e.py) | [✅](./tests/2.4/test_24_e.py) |
| F. [НОД 2.0](./solutions/2.4/24_f.py) | [✅](./tests/2.4/test_24_f.py) |
| G. [На старт! Внимание! Марш!](./solutions/2.4/24_g.py) | [✅](./tests/2.4/test_24_g.py) |
| H. [Максимальная сумма](./solutions/2.4/24_h.py) | [✅](./tests/2.4/test_24_h.py) |
| I. [Большое число](./solutions/2.4/24_i.py) | [✅](./tests/2.4/test_24_i.py) |
| J. [Мы делили апельсин](./solutions/2.4/24_j.py) | [✅](./tests/2.4/test_24_j.py) |
| K. [Простая задача 3.0](./solutions/2.4/24_k.py) | [✅](./tests/2.4/test_24_k.py) |
| L. [Числовой прямоугольник](./solutions/2.4/24_l.py) | [✅](./tests/2.4/test_24_l.py) |
| M. [Числовой прямоугольник 2.0](./solutions/2.4/24_m.py) | [✅](./tests/2.4/test_24_m.py) |
| N. [Числовая змейка](./solutions/2.4/24_n.py) | [✅](./tests/2.4/test_24_n.py) |
| O. [Числовая змейка 2.0](./solutions/2.4/24_o.py) | [✅](./tests/2.4/test_24_o.py) |
| P. [Редизайн таблицы умножения](./solutions/2.4/24_p.py) | [✅](./tests/2.4/test_24_p.py) |
| Q. [А роза упала на лапу Азора 3.0](./solutions/2.4/24_q.py) | [✅](./tests/2.4/test_24_q.py) |
| R. [Новогоднее настроение 2.0](./solutions/2.4/24_r.py) | [✅](./tests/2.4/test_24_r.py) |
| S. [Числовой квадрат](./solutions/2.4/24_s.py) | [✅](./tests/2.4/test_24_s.py) |
| T. [Математическая выгода](./solutions/2.4/24_t.py) | [✅](./tests/2.4/test_24_t.py) |

</details>

<details>
<summary><h3>3.1 Строки, кортежи, списки</h3></summary>

#### Для решения задач используется только пройденный материал из параграфоф:
- [3.1 Строки, кортежи, списки](https://education.yandex.ru/handbook/python/article/stroki-kortezhi-spiski)

### [Тестовые данные для задач](./tests/data/test_data_31.py)

| Решение              | Тесты                |
|----------------------|----------------------|
| А. [Азбука](./solutions/3.1/31_a.py) | [✅](./tests/3.1/test_31_a.py) |
| B. [Кручу-верчу](./solutions/3.1/31_b.py) | [✅](./tests/3.1/test_31_b.py) |
| C. [Анонс новости](./solutions/3.1/31_c.py) | [✅](./tests/3.1/test_31_c.py) |
| D. [Очистка данных](./solutions/3.1/31_d.py) | [✅](./tests/3.1/test_31_d.py) |
| E. [А роза упала на лапу Азора 4.0](./solutions/3.1/31_e.py) | [✅](./tests/3.1/test_31_e.py) |
| F. [Зайка — 6](./solutions/3.1/31_f.py) | [✅](./tests/3.1/test_31_f.py) |
| G. [А и Б сидели на трубе](./solutions/3.1/31_g.py) | [✅](./tests/3.1/test_31_g.py) |
| H. [Зайка — 7](./solutions/3.1/31_h.py) | [✅](./tests/3.1/test_31_h.py) |
| I. [Без комментариев](./solutions/3.1/31_i.py) | [✅](./tests/3.1/test_31_i.py) |
| J. [Частотный анализ на минималках](./solutions/3.1/31_j.py) | [✅](./tests/3.1/test_31_j.py) |
| K. [Найдётся всё](./solutions/3.1/31_k.py) | [✅](./tests/3.1/test_31_k.py) |
| L. [Меню питания](./solutions/3.1/31_l.py) | [✅](./tests/3.1/test_31_l.py) |
| M. [Массовое возведение в степень](./solutions/3.1/31_m.py) | [✅](./tests/3.1/test_31_m.py) |
| N. [Массовое возведение в степень 3.0](./solutions/3.1/31_n.py) | [✅](./tests/3.1/test_31_n.py) |
| O. [НОД 3.0](./solutions/3.1/31_o.py) | [✅](./tests/3.1/test_31_o.py) |
| P. [Анонс новости 3.0](./solutions/3.1/31_p.py) | [✅](./tests/3.1/test_31_p.py) |
| Q. [А роза упала на лапу Азора 5.0](./solutions/3.1/31_q.py) | [✅](./tests/3.1/test_31_q.py) |
| R. [RLE](./solutions/3.1/31_r.py) | [✅](./tests/3.1/test_31_r.py) |
| S. [Польский калькулятор](./solutions/3.1/31_s.py) | [✅](./tests/3.1/test_31_s.py) |
| T. [Польский калькулятор — 3](./solutions/3.1/31_t.py) | [✅](./tests/3.1/test_31_t.py) |

</details>

<details>
<summary><h3>3.2 Множества, словари</h3></summary>

#### Для решения задач используется только пройденный материал из параграфоф:
- [3.1 Строки, кортежи, списки](https://education.yandex.ru/handbook/python/article/stroki-kortezhi-spiski)
- [3.2 Множества, словари](https://education.yandex.ru/handbook/python/article/mnozhestva-slovari)

### [Тестовые данные для задач](./tests/data/test_data_32.py)

| Решение              | Тесты                |
|----------------------|----------------------|
| А. [Символическая выжимка](./solutions/3.2/32_a.py) | [✅](./tests/3.2/test_32_a.py) |
| B. [Символическая разница](./solutions/3.2/32_b.py) | [✅](./tests/3.2/test_32_b.py) |
| C. [Зайка — 8](./solutions/3.2/32_c.py) | [✅](./tests/3.2/test_32_c.py) |
| D. [Кашееды](./solutions/3.2/32_d.py) | [✅](./tests/3.2/test_32_d.py) |
| E. [Кашееды — 2](./solutions/3.2/32_e.py) | [✅](./tests/3.2/test_32_e.py) |
| F. [Кашееды — 3](./solutions/3.2/32_f.py) | [✅](./tests/3.2/test_32_f.py) |
| G. [Азбука Морзе](./solutions/3.2/32_g.py) | [✅](./tests/3.2/test_32_g.py) |
| H. [Кашееды — 4](./solutions/3.2/32_h.py) | [✅](./tests/3.2/test_32_h.py) |
| I. [Зайка — 9](./solutions/3.2/32_i.py) | [✅](./tests/3.2/test_32_i.py) |
| J. [Транслитерация](./solutions/3.2/32_j.py) | [✅](./tests/3.2/test_32_j.py) |
| K. [Однофамильцы](./solutions/3.2/32_k.py) | [✅](./tests/3.2/test_32_k.py) |
| L. [Однофамильцы — 2](./solutions/3.2/32_l.py) | [✅](./tests/3.2/test_32_l.py) |
| M. [Дайте чего-нибудь новенького!](./solutions/3.2/32_m.py) | [✅](./tests/3.2/test_32_m.py) |
| N. [Это будет шедевр!](./solutions/3.2/32_n.py) | [✅](./tests/3.2/test_32_n.py) |
| O. [Двоичная статистика!](./solutions/3.2/32_o.py) | [✅](./tests/3.2/test_32_o.py) |
| P. [Зайка — 10](./solutions/3.2/32_p.py) | [✅](./tests/3.2/test_32_p.py) |
| Q. [Друзья друзей](./solutions/3.2/32_q.py) | [✅](./tests/3.2/test_32_q.py) |
| R. [Карта сокровищ](./solutions/3.2/32_r.py) | [✅](./tests/3.2/test_32_r.py) |
| S. [Частная собственность](./solutions/3.2/32_s.py) | [✅](./tests/3.2/test_32_s.py) |
| T. [Простая задача 4.0](./solutions/3.2/32_t.py) | [✅](./tests/3.2/test_32_t.py) |

</details>

<details>
<summary><h3>3.3 Списочные выражения. Модель памяти для типов языка Python</h3></summary>

#### Для решения задач используется только пройденный материал из параграфоф:
- [3.1 Строки, кортежи, списки](https://education.yandex.ru/handbook/python/article/stroki-kortezhi-spiski)
- [3.2 Множества, словари](https://education.yandex.ru/handbook/python/article/mnozhestva-slovari)
- [3.3 Списочные выражения. Модель памяти для типов языка Python](https://education.yandex.ru/handbook/python/article/spisochnye-vyrazheniya-model-pamyati-dlya-tipov-yazyka-python)

### [Тестовые данные для задач](./tests/data/test_data_33.py)

| Решение              | Тесты                |
|----------------------|----------------------|
| А. [Список квадратов](./solutions/3.3/33_a.py) | [❌](./tests/3.3/test_33_a.py) |
| B. [Таблица умножения 2.0](./solutions/3.3/33_b.py) | [❌](./tests/3.3/test_33_b.py) |
| C. [Длины всех слов](./solutions/3.3/33_c.py) | [❌](./tests/3.3/test_33_c.py) |
| D. [Множество нечетных чисел](./solutions/3.3/33_d.py) | [❌](./tests/3.3/test_33_d.py) |
| E. [Множество всех полных квадратов](./solutions/3.3/33_e.py) | [❌](./tests/3.3/test_33_e.py) |
| F. [Буквенная статистика](./solutions/3.3/33_f.py) | [❌](./tests/3.3/test_33_f.py) |
| G. [Делители](./solutions/3.3/33_g.py) | [❌](./tests/3.3/test_33_g.py) |
| H. [Аббревиатура](./solutions/3.3/33_h.py) | [❌](./tests/3.3/test_33_h.py) |
| I. [Преобразование в строку](./solutions/3.3/33_i.py) | [❌](./tests/3.3/test_33_i.py) |
| J. [RLE наоборот](./solutions/3.3/33_j.py) | [❌](./tests/3.3/test_33_j.py) |

</details>

## Автор

- [Andrei Pomortsev](https://www.linkedin.com/in/andreypomortsev/)

### Зачем мне это?

Для помощи начинающим разработчикам в решении задач учебника и пояснения логики этих решений, для некоторых заданий она не очевидна.
