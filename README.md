![Codacy grade (branch)](https://img.shields.io/codacy/grade/63f71a9c86ce4a0492af52c23628b78a/main)
![Python 3.12](https://img.shields.io/badge/Python-3.12-green.svg)
![Build Status](https://github.com/andreypomortsev/yndx-python-handbook/actions/workflows/ci.yml/badge.svg)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/andreypomortsev/yndx-python-handbook)
[![codecov](https://codecov.io/gh/andreypomortsev/yndx-python-handbook/branch/main/graph/badge.svg?token=WPUYVICKGT)](https://codecov.io/gh/andreypomortsev/yndx-python-handbook)
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
```
python3 -m venv .venv
```

#### Активируем виртуальную среду

- На macOS и Linux:

  ```bash
  source .venv/bin/activate
  ```

- На Windows:

  ```bash
  .venv\Scripts\activate
  ```

#### Устанавливаемм все необходимое

```
pip3 install -r requirements
```

#### Запускаем тесты

```
pytest
```
Тесты с отчетом в `html`:
```
pytest --cov-report=html
```
после прохождения тестов открываем файл: `htmlcov/index.html`

Во время теста в папке `tests` будут созданы временные файлы `wrapped_*.py` которые удалятся после прохождения тестов.

### Проверка Вашего кода

После клонирования репозитория выполните следующие шаги:

- Найдите код, который вам нужно проверить, и замените его на ваше решение.
  - Например у вас проблема с задачей [2.1 C](./solutions/2.1/c.py) заходите в файл вставляете свое решение, сохраняете и запускаете тесты.
- Сохраните изменения и запустите тесты.
- Проверьте покрытие кода тестами. Это покажет, сколько строк вашего кода было выполнено во время тестов. Если покрытие меньше 100%, это может указывать на то, что некоторые строки кода не нужны или не были протестированы.
- Если тесты не прошли, названия неудачных тестов будут выделены красным цветом. Перейдите в папку с тестами, откройте соответствующий файл и проверьте входные данные.
- Исправьте код в соответствии с выявленными проблемами, снова запустите тесты и повторяйте процесс до тех пор, пока все тесты не пройдут успешно.

Кроме правильного ответа Яндекс проверяет еще и на соответствие кода [PEP8](https://github.com/Searge/mipt_oop/blob/master/week_1/readme.md), поэтому научитесь пользоваться линтерами: [flake8](https://flake8.pycqa.org/en/latest/), [black](https://black.readthedocs.io/en/stable/index.html), etc...

## Решения | Тесты

<details>
<summary><h3>2.1 Ввод и вывод данных. Операции с числами, строками. Форматирование</h3></summary>
В этом параграфе для решения задач используется только пройденный материал: строки, числа и форматирование.
  
### [Тестовые данные для задач](./tests/data/test_data_21.py)
  
| Решение              | Тесты                |
|----------------------|----------------------|
| А. [Привет, Яндекс!](./solutions/2.1/a.py) | [✅](./tests/2.1/test_a.py) |
| B. [Привет, всем!](./solutions/2.1/b.py) | [✅](./tests/2.1/test_b.py) |
| C. [Излишняя автоматизация](./solutions/2.1/c.py) | [✅](./tests/2.1/test_c.py) |
| D. [Сдача](./solutions/2.1/d.py) | [✅](./tests/2.1/test_d.py) |
| E. [Магазин](./solutions/2.1/e.py) | [✅](./tests/2.1/test_e.py) |
| F. [Чек](./solutions/2.1/f.py) | [✅](./tests/2.1/test_f.py) |
| G. [Делу — время, потехе — час](./solutions/2.1/g.py) | [✅](./tests/2.1/test_g.py) |
| H. [Наказание](./solutions/2.1/h.py) | [✅](./tests/2.1/test_h.py) |
| I. [Деловая колбаса](./solutions/2.1/i.py) | [✅](./tests/2.1/test_i.py) |
| J. [Детский сад — штаны на лямках](./solutions/2.1/j.py) | [✅](./tests/2.1/test_j.py) |
| K. [Автоматизация игры](./solutions/2.1/k.py) | [✅](./tests/2.1/test_k.py) |
| L. [Интересное сложение](./solutions/2.1/l.py) | [✅](./tests/2.1/test_l.py) |
| M. [Дед Мороз и конфеты](./solutions/2.1/m.py) | [✅](./tests/2.1/test_m.py) |
| N. [Шарики и ручки](./solutions/2.1/n.py) | [✅](./tests/2.1/test_n.py) |
| O. [В ожидании доставки](./solutions/2.1/o.py) | [✅](./tests/2.1/test_o.py) |
| P. [Доставка](./solutions/2.1/p.py) | [✅](./tests/2.1/test_p.py) |
| Q. [Ошибка кассового аппарата](./solutions/2.1/q.py) | [✅](./tests/2.1/test_q.py) |
| R. [Сдача 10](./solutions/2.1/r.py) | [✅](./tests/2.1/test_r.py) |
| S. [Украшение чека](./solutions/2.1/s.py) | [✅](./tests/2.1/test_s.py) |
| T. [Мухи отдельно, котлеты отдельно](./solutions/2.1/t.py) | [✅](./tests/2.1/test_t.py) |

</details>
<details>
<summary><h3>2.2 Условный оператор</h3></summary>
В этом параграфе для решения задач используется только пройденный материал из предыдущих параграфоф (2.1, 2.2).

### [Тестовые данные для задач](./tests/data/test_data_22.py)

| Решение              | Тесты                |
|----------------------|----------------------|
| А. [Просто здравствуй, просто как дела](./solutions/2.2/a22.py) | [✅](./tests/2.2/test_a22.py) |
| B. [Кто быстрее?](./solutions/2.2/b22.py) | [✅](./tests/2.2/test_b22.py) |
| C. [Кто быстрее на этот раз?](./solutions/2.2/c22.py) | [✅](./tests/2.2/test_c22.py) |
| D. [Список победителей](./solutions/2.2/d22.py) | [✅](./tests/2.2/test_d22.py) |
| E. [Яблоки](./solutions/2.2/e22.py) | [✅](./tests/2.2/test_e22.py) |
| F. [Сила прокрастинации](./solutions/2.2/f22.py) | [✅](./tests/2.2/test_f22.py) |
| G. [А роза упала на лапу Азора](./solutions/2.2/g22.py) | [✅](./tests/2.2/test_g22.py) |
| H. [Зайка — 1](./solutions/2.2/h22.py) | [✅](./tests/2.2/test_h22.py) |
| I. [Первому игроку приготовиться](./solutions/2.2/i22.py) | [✅](./tests/2.2/test_i22.py) |
| J. [Лучшая защита — шифрование](./solutions/2.2/j22.py) | [✅](./tests/2.2/test_j22.py) |
| K. [Красота спасёт мир](./solutions/2.2/k22.py) | [✅](./tests/2.2/test_k22.py) |
| L. [Музыкальный инструмент](./solutions/2.2/l22.py) | [✅](./tests/2.2/test_l22.py) |
| M. [Властелин Чисел: Братство общей цифры](./solutions/2.2/m22.py) | [✅](./tests/2.2/test_m22.py) |
| N. [Властелин Чисел: Две Башни](./solutions/2.2/n22.py) | [✅](./tests/2.2/test_n22.py) |
| O. [Властелин Чисел: Возвращение Цезаря](./solutions/2.2/o22.py) | [✅](./tests/2.2/test_o22.py) |
| P. [Легенды велогонок возвращаются: кто быстрее?](./solutions/2.2/p22.py) | [✅](./tests/2.2/test_p22.py) |
| Q. [Корень зла](./solutions/2.2/q22.py) | [✅](./tests/2.2/test_q22.py) |
| R. [Территория зла](./solutions/2.2/r22.py) | [✅](./tests/2.2/test_r22.py) |
| S. [Автоматизация безопасности](./solutions/2.2/s22.py) | [✅](./tests/2.2/test_s22.py) |
| T. [Зайка — 2](./solutions/2.2/t22.py) | [✅](./tests/2.2/test_t22.py) |

</details>

<details>
<summary><h3>2.3 Циклы</h3></summary>
В этом параграфе для решения задач используется только пройденный материал из предыдущих параграфоф (2.1 - 2.3).

### [Тестовые данные для задач](./tests/data/test_data_23.py)

| Решение              | Тесты                |
|----------------------|----------------------|
| А. [Раз, два, три! Ёлочка, гори!](./solutions/2.3/a23.py) | [✅](./tests/2.3/test_a23.py) |
| B. [Зайка — 3](./solutions/2.3/b23.py) | [✅](./tests/2.3/test_b23.py) |
| C. [Считалочка](./solutions/2.3/c23.py) | [✅](./tests/2.3/test_c23.py) |
| D. [Считалочка 2.0](./solutions/2.3/d23.py) | [✅](./tests/2.3/test_d23.py) |
| E. [Внимание! Акция!](./solutions/2.3/e23.py) | [✅](./tests/2.3/test_e23.py) |
| F. [НОД](./solutions/2.3/f23.py) | [❌](./tests/2.3/test_f23.py) |
| G. [НОК](./solutions/2.3/g23.py) | [❌](./tests/2.3/test_g23.py) |
| H. [Излишняя автоматизация 2.0](./solutions/2.3/h23.py) | [❌](./tests/2.3/test_h23.py) |
| I. [Факториал](./solutions/2.3/i23.py) | [❌](./tests/2.3/test_i23.py) |
| J. [Маршрут построен](./solutions/2.3/j23.py) | [❌](./tests/2.3/test_j23.py) |
| K. [Цифровая сумма](./solutions/2.3/k23.py) | [❌](./tests/2.3/test_k23.py) |
| L. [Сильная цифра](./solutions/2.3/l23.py) | [❌](./tests/2.3/test_l23.py) |
| M. [Первому игроку приготовиться 2.0](./solutions/2.3/m23.py) | [❌](./tests/2.3/test_m23.py) |
| N. [Простая задача](./solutions/2.3/n23.py) | [❌](./tests/2.3/test_n23.py) |
| O. [Зайка - 4](./solutions/2.3/o23.py) | [❌](./tests/2.3/test_o23.py) |
| P. [А роза упала на лапу Азора 2.0](./solutions/2.3/p23.py) | [❌](./tests/2.3/test_p23.py) |
| Q. [Чётная чистота](./solutions/2.3/q23.py) | [❌](./tests/2.3/test_q23.py) |
| R. [Простая задача 2.0](./solutions/2.3/r23.py) | [❌](./tests/2.3/test_r23.py) |
| S. [Игра в «Угадайку»](./solutions/2.3/s23.py) | [❌](./tests/2.3/test_s23.py) |
| T. [Хайпанём немножечко!](./solutions/2.3/t23.py) | [❌](./tests/2.3/test_t23.py) |

</details>

## Автор

- [Andrei Pomortsev](https://www.linkedin.com/in/andreypomortsev/)

### Зачем мне это?

Для помощи начинающим разработчикам в решении задач учебника и пояснения логики этих решений, для некоторых заданий она не очевидна.
