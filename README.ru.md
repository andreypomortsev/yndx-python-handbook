![Codacy grade (branch)](https://img.shields.io/codacy/grade/63f71a9c86ce4a0492af52c23628b78a/main)
![Build Status](https://github.com/andreypomortsev/yndx-python-handbook/actions/workflows/ci.yml/badge.svg)
[![codecov](https://codecov.io/gh/andreypomortsev/yndx-python-handbook/branch/main/graph/badge.svg?token=WPUYVICKGT)](https://codecov.io/gh/andreypomortsev/yndx-python-handbook)
![Python 3.12](https://img.shields.io/badge/Python-3.12-yellow.svg)
![Python 3.13](https://img.shields.io/badge/Python-3.13-green.svg)
![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)

## Решения задач из учебника [Основы Python](https://education.yandex.ru/handbook/python) от Яндекс

_"Хендбук по Python поможет овладеть основным синтаксисом и принципами языка. Для этого не потребуется специальной подготовки — достаточно знаний по информатике, логике и математике на уровне школьной программы. Кроме основных конструкций в учебнике рассмотрены разные подходы к программированию, реализованные на Python."_ **Яндекс**

### Предварительные требования

- **Python**: Убедитесь, что у вас установлена версия Python 3.12 или выше. Скачать можно по ссылкам:
  - [**Python 3.12**](https://www.python.org/downloads/release/python-3127/)
  - [**Python 3.13**](https://www.python.org/downloads/release/python-3130/)

- **Git**: Потребуется для клонирования репозитория. [Скачать Git](https://git-scm.com/downloads).

## Установка

<details>
<summary><h3>Инструкция по установке и запуску команд для начинающих</h3></summary>

### Шаги установки (без использования venv)

1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/andreypomortsev/yndx-python-handbook
   cd yndx-python-handbook
   ```

2. **Установите зависимости**:
   Установите все необходимые пакеты из файла `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

#### Форматирование кода по PEP8

Для форматирования кода с использованием `black` и сортировка импортов `isort`:
```bash
black . --line-length=79
isort .
```

#### Запуск всех тестов

Запустите все тесты из директории `tests`:
```bash
pytest
```

#### Запуск всех тестов в режиме отладки

Чтобы увидеть расширенные логи во время тестов:
```bash
pytest -vv
```

#### Запуск тестов для конкретного параграфа

Чтобы запустить тесты только для задач в определенной папке (например, `2.1`), используйте:
```bash
pytest tests/2.1
```

#### Запуск тестов для конкретной задачи

Для тестирования отдельной задачи (например, задачи `Q` из папки `2.3`):
```bash
pytest tests/2.3/test_23_q.py
```

#### Создание отчета о покрытии тестами в формате HTML

Чтобы сгенерировать HTML-отчет по покрытию:
```bash
pytest --cov-report html
```

После выполнения этой команды отчет будет доступен в `htmlcov/index.html`.

#### Создание отчета о покрытии тестами в формате XML

Для генерации отчета в формате XML:
```bash
pytest --cov-report xml
```

#### Запуск линтера flake8

Чтобы проверить код на ошибки стиля и потенциальные проблемы:
```bash
flake8 .
```

---

##### Примечание
Эти команды позволяют вручную выполнять все основные задачи по тестированию и форматированию кода в проекте.

</details>

<details>
<summary><h3>Инструкция по установке и запуску команд с Poetry</h3></summary>

### Установка Poetry

- **Windows**:

  ```powershell
  (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
  ```

- **Unix-like OS (Linux/macOS)**:

  ```sh
  curl -sSL https://install.python-poetry.org | python3 -
  ```

#### Проверка успешной установки Poetry

```sh
poetry --version
```

### Шаги установки c poetry

1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/andreypomortsev/yndx-python-handbook
   cd yndx-python-handbook
   ```

2. **Установите зависимости и создайтк виртуальное окружение**:
   - **Windows**:

  ```powershell
  pip install poetry -q
  poetry install
  poetry shell
  ```

  - **Unix-like OS (Linux/macOS)**:

    ```sh
    make setup
    ```

#### Форматирование кода (PEP8)

- **Windows**:

  ```powershell
  poetry run black . --line-length=79
  poetry run isort .
  ```

- **Unix-like OS (Linux/macOS)**:

  ```sh
  make format
  ```

#### Запуск тестов

- **Все тесты в репозитории**:

  - **Windows**:

    ```powershell
    poetry run pytest
    ```

  - **Unix-like OS (Linux/macOS)**:

    ```sh
    make test
    ```

- **Тесты в дебаг-режиме**:

  - **Windows**:

    ```powershell
    poetry run pytest -vv
    ```

  - **Unix-like OS (Linux/macOS)**:

    ```sh
    make debug
    ```

- **Запуск тестов для отдельного параграфа (например, 2.1)**:

  - **Windows**:

    ```powershell
    poetry run pytest tests\2.1
    ```

  - **Unix-like OS (Linux/macOS)**:

    ```sh
    make test-dir-2.1
    ```

- **Запуск теста для одной задачи (например, тест задачи Q в параграфе 2.3)**:

  - **Windows**:

    ```powershell
    poetry run pytest tests\2.3\test_23_q.py
    ```

  - **Unix-like OS (Linux/macOS)**:

    ```sh
    make test-file-2.3-Q
    ```

#### Генерация отчётов покрытия тестами

- **HTML Отчёт**:

  - **Windows**:

    ```powershell
    poetry run pytest --cov-report=html
    ```

  - **Unix-like OS (Linux/macOS)**:

    ```sh
    make test-report-html
    ```

  После выполнения откройте файл `htmlcov/index.html` для просмотра отчёта.

- **XML Отчёт**:

  - **Windows**:

    ```powershell
    poetry run pytest --cov-report=xml
    ```

  - **Unix-like OS (Linux/macOS)**:

    ```sh
    make test-report-xml
    ```

#### Линтинг с flake8

- **Windows**:

  ```powershell
  poetry run flake8 .
  ```

- **Unix-like OS (Linux/macOS)**:

  ```sh
  make lint
  ```

#### Форматирование кода с black и isort

- **Windows**:

  ```powershell
  poetry run black . --line-length=79
  poetry run isort .
  ```

- **Unix-like OS (Linux/macOS)**:

  ```sh
  make format
  ```

#### Удаление лишних файлов

- **Windows**:

  ```powershell
  find . -name '*.pyc' -delete
  find . -name '__pycache__' -delete
  find ../. -name '.coverage' -delete
  ```

- **Unix-like OS (Linux/macOS)**:

  ```sh
  make clean
  ```

---

##### Примечания

- Для пользователей **Windows**: все команды выполняются через `poetry run`, чтобы обеспечить совместимость с системой.
- Для пользователей **Unix-like OS**: можно использовать как `make` для упрощения команд, так и команды для **Windows**.

</details>

</details>

### Проверка Вашего кода

После клонирования репозитория выполните следующие шаги:

- Найдите код, который вам нужно проверить, и замените его на ваше решение.
  - Например у вас проблема с задачей [2.1 C](./solutions/2.1/c.py) заходите в файл вставляете свое решение, сохраняете.
- Запустите тесты.
- Проверьте покрытие кода тестами. Это покажет, сколько строк вашего кода было выполнено во время тестов. Если покрытие меньше 100%, это может указывать на то, что некоторые строки кода не нужны или не были протестированы.
- Если тесты не прошли, названия неудачных тестов будут выделены красным цветом.
- Исправьте код в соответствии с выявленными проблемами, снова запустите тесты и повторяйте процесс до тех пор, пока все тесты не пройдут успешно.

Кроме правильного ответа Яндекс проверяет еще и на соответствие кода [PEP8](https://github.com/Searge/mipt_oop/blob/master/week_1/readme.md), поэтому научитесь пользоваться линтерами: [flake8](https://flake8.pycqa.org/en/latest/) или [pylint](https://pypi.org/project/pylint/) и форматером кода, я использую [black](https://black.readthedocs.io/en/stable/index.html).

## Решения | Тесты

<details>

<summary><h3>2.1 Ввод и вывод данных. Операции с числами, строками. Форматирование</h3></summary>

- [Теория Ввод и вывод данных. Операции с числами, строками. Форматирование](https://education.yandex.ru/handbook/python/article/vvod-i-vyvod-dannykh-operatsii-s-chislami-strokami-formatirovaniye)
  
### [Тестовые данные для задач](./tests/data/test_data_21.py)
  
| Задача               | Решение              | Тесты                |
|----------------------|----------------------|----------------------|
| А. [Привет, Яндекс!](./problems/russian/2.1/problem_21_a_ru.md) | [✅](./solutions/2.1/21_a.py) | [✅](./tests/2.1/test_21_a.py) |
| B. [Привет, всем!](./problems/russian/2.1/problem_21_b_ru.md) | [✅](./solutions/2.1/21_b.py) | [✅](./tests/2.1/test_21_b.py) |
| C. [Излишняя автоматизация](./problems/russian/2.1/problem_21_c_ru.md) | [✅](./solutions/2.1/21_c.py) | [✅](./tests/2.1/test_21_c.py) |
| D. [Сдача](./problems/russian/2.1/problem_21_d_ru.md) | [✅](./solutions/2.1/21_d.py) | [✅](./tests/2.1/test_21_d.py) |
| E. [Магазин](./problems/russian/2.1/problem_21_e_ru.md) | [✅](./solutions/2.1/21_e.py) | [✅](./tests/2.1/test_21_e.py) |
| F. [Чек](./problems/russian/2.1/problem_21_f_ru.md) | [✅](./solutions/2.1/21_f.py) | [✅](./tests/2.1/test_21_f.py) |
| G. [Делу — время, потехе — час](./problems/russian/2.1/problem_21_g_ru.md) | [✅](./solutions/2.1/21_g.py) | [✅](./tests/2.1/test_21_g.py) |
| H. [Наказание](./problems/russian/2.1/problem_21_h_ru.md) | [✅](./solutions/2.1/21_h.py) | [✅](./tests/2.1/test_21_h.py) |
| I. [Деловая колбаса](./problems/russian/2.1/problem_21_i_ru.md) | [✅](./solutions/2.1/21_i.py) | [✅](./tests/2.1/test_21_i.py) |
| J. [Детский сад — штаны на лямках](./problems/russian/2.1/problem_21_j_ru.md) | [✅](./solutions/2.1/21_j.py) | [✅](./tests/2.1/test_21_j.py) |
| K. [Автоматизация игры](./problems/russian/2.1/problem_21_k_ru.md) | [✅](./solutions/2.1/21_k.py) | [✅](./tests/2.1/test_21_k.py) |
| L. [Интересное сложение](./problems/russian/2.1/problem_21_l_ru.md) | [✅](./solutions/2.1/21_l.py) | [✅](./tests/2.1/test_21_l.py) |
| M. [Дед Мороз и конфеты](./problems/russian/2.1/problem_21_m_ru.md) | [✅](./solutions/2.1/21_m.py) | [✅](./tests/2.1/test_21_m.py) |
| N. [Шарики и ручки](./problems/russian/2.1/problem_21_n_ru.md) | [✅](./solutions/2.1/21_n.py) | [✅](./tests/2.1/test_21_n.py) |
| O. [В ожидании доставки](./problems/russian/2.1/problem_21_o_ru.md) | [✅](./solutions/2.1/21_o.py) | [✅](./tests/2.1/test_21_o.py) |
| P. [Доставка](./problems/russian/2.1/problem_21_p_ru.md) | [✅](./solutions/2.1/21_p.py) | [✅](./tests/2.1/test_21_p.py) |
| Q. [Ошибка кассового аппарата](./problems/russian/2.1/problem_21_q_ru.md) | [✅](./solutions/2.1/21_q.py) | [✅](./tests/2.1/test_21_q.py) |
| R. [Сдача 10](./problems/russian/2.1/problem_21_r_ru.md) | [✅](./solutions/2.1/21_r.py) | [✅](./tests/2.1/test_21_r.py) |
| S. [Украшение чека](./problems/russian/2.1/problem_21_s_ru.md) | [✅](./solutions/2.1/21_s.py) | [✅](./tests/2.1/test_21_s.py) |
| T. [Мухи отдельно, котлеты отдельно](./problems/russian/2.1/problem_21_t_ru.md) | [✅](./solutions/2.1/21_t.py) | [✅](./tests/2.1/test_21_t.py) |

</details>

<details>
<summary><h3>2.2 Условный оператор</h3></summary>

- [Теория Условный оператор](https://education.yandex.ru/handbook/python/article/uslovnyy-operator)

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

- [Теория Циклы](https://education.yandex.ru/handbook/python/article/cikly)

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

- [Теория Вложенные циклы](https://education.yandex.ru/handbook/python/article/vlozhennye-cikly)

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

- [Теория Строки, кортежи, списки](https://education.yandex.ru/handbook/python/article/stroki-kortezhi-spiski)

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

- [Теория Множества, словари](https://education.yandex.ru/handbook/python/article/mnozhestva-slovari)

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

- [Теория Списочные выражения. Модель памяти для типов языка Python](https://education.yandex.ru/handbook/python/article/spisochnye-vyrazheniya-model-pamyati-dlya-tipov-yazyka-python)

### [Тестовые данные для задач](./tests/data/test_data_33.py)

| Решение              | Тесты                |
|----------------------|----------------------|
| А. [Список квадратов](./solutions/3.3/33_a.py) | [✅](./tests/3.3/test_33_a.py) |
| B. [Таблица умножения 2.0](./solutions/3.3/33_b.py) | [✅](./tests/3.3/test_33_b.py) |
| C. [Длины всех слов](./solutions/3.3/33_c.py) | [✅](./tests/3.3/test_33_c.py) |
| D. [Множество нечетных чисел](./solutions/3.3/33_d.py) | [✅](./tests/3.3/test_33_d.py) |
| E. [Множество всех полных квадратов](./solutions/3.3/33_e.py) | [✅](./tests/3.3/test_33_e.py) |
| F. [Буквенная статистика](./solutions/3.3/33_f.py) | [✅](./tests/3.3/test_33_f.py) |
| G. [Делители](./solutions/3.3/33_g.py) | [✅](./tests/3.3/test_33_g.py) |
| H. [Аббревиатура](./solutions/3.3/33_h.py) | [✅](./tests/3.3/test_33_h.py) |
| I. [Преобразование в строку](./solutions/3.3/33_i.py) | [✅](./tests/3.3/test_33_i.py) |
| J. [RLE наоборот](./solutions/3.3/33_j.py) | [✅](./tests/3.3/test_33_j.py) |

</details>

<details>
<summary><h3>3.4 Встроенные возможности по работе с коллекциями</h3></summary>

- [Теория Встроенные возможности по работе с коллекциями](https://education.yandex.ru/handbook/python/article/vstroennye-vozmozhnosti-po-rabote-s-kollekciyami)

### [Тестовые данные для задач](./tests/data/test_data_34.py)

| Решение              | Тесты                |
|----------------------|----------------------|
| А. [Автоматизация списка](./solutions/3.4/34_a.py) | [✅](./tests/3.4/test_34_a.py) |
| B. [Сборы на прогулку](./solutions/3.4/34_b.py) | [✅](./tests/3.4/test_34_b.py) |
| C. [Рациональная считалочка](./solutions/3.4/34_c.py) | [✅](./tests/3.4/test_34_c.py) |
| D. [Словарная ёлка](./solutions/3.4/34_d.py) | [✅](./tests/3.4/test_34_d.py) |
| E. [Список покупок](./solutions/3.4/34_e.py) | [✅](./tests/3.4/test_34_e.py) |
| F. [Колода карт](./solutions/3.4/34_f.py) | [✅](./tests/3.4/test_34_f.py) |
| G. [Игровая сетка](./solutions/3.4/34_g.py) | [✅](./tests/3.4/test_34_g.py) |
| H. [Меню питания 2.0](./solutions/3.4/34_h.py) | [✅](./tests/3.4/test_34_h.py) |
| I. [Таблица умножения 3.0](./solutions/3.4/34_i.py) | [✅](./tests/3.4/test_34_i.py) |
| J. [Мы делили апельсин 2.0](./solutions/3.4/34_j.py) | [✅](./tests/3.4/test_34_j.py) |
| K. [Числовой прямоугольник 3.0](./solutions/3.4/34_k.py) | [✅](./tests/3.4/test_34_k.py) |
| L. [Список покупок 2.0](./solutions/3.4/34_l.py) | [✅](./tests/3.4/test_34_l.py) |
| M. [Расстановка спортсменов](./solutions/3.4/34_m.py) | [✅](./tests/3.4/test_34_m.py) |
| N. [Спортивные гадания](./solutions/3.4/34_n.py) | [✅](./tests/3.4/test_34_n.py) |
| O. [Список покупок 3.0](./solutions/3.4/34_o.py) | [✅](./tests/3.4/test_34_o.py) |
| P. [Расклад таков...](./solutions/3.4/34_p.py) | [✅](./tests/3.4/test_34_p.py) |
| Q. [А есть ещё варианты?](./solutions/3.4/34_q.py) | [✅](./tests/3.4/test_34_q.py) |
| R. [Таблица истинности](./solutions/3.4/34_r.py) | [✅](./tests/3.4/test_34_r.py) |
| S. [Таблица истинности 2](./solutions/3.4/34_s.py) | [✅](./tests/3.4/test_34_s.py) |
| T. [Таблица истинности 3](./solutions/3.4/34_t.py) | [✅](./tests/3.4/test_34_t.py) |

</details>

<details>
<summary><h3>3.5 Потоковый ввод/вывод. Работа с текстовыми файлами. JSON</h3></summary>

- [Теория Потоковый ввод/вывод. Работа с текстовыми файлами. JSON](https://education.yandex.ru/handbook/python/article/potokovyj-vvodvyvod-rabota-s-tekstovymi-fajlami-json)

### [Тестовые данные для задач](./tests/data/test_data_35.py)

| Решение              | Тесты                |
|----------------------|----------------------|
| А. [A+B+...](./solutions/3.5/35_a.py) | [✅](./tests/3.5/test_35_a.py) |
| B. [Средний рост](./solutions/3.5/35_b.py) | [✅](./tests/3.5/test_35_b.py) |
| C. [Без комментариев 2.0](./solutions/3.5/35_c.py) | [✅](./tests/3.5/test_35_c.py) |
| D. [Найдётся всё 2.0](./solutions/3.5/35_d.py) | [✅](./tests/3.5/test_35_d.py) |
| E. [А роза упала на лапу Азора 6.0](./solutions/3.5/35_e.py) | [✅](./tests/3.5/test_35_e.py) |
| F. [Транслитерация 2.0](./solutions/3.5/35_f.py) | [✅](./tests/3.5/test_35_f.py) |
| G. [Файловая статистика](./solutions/3.5/35_g.py) | [✅](./tests/3.5/test_35_g.py) |
| H. [Файловая разница](./solutions/3.5/35_h.py) | [✅](./tests/3.5/test_35_h.py) |
| I. [Файловая чистка](./solutions/3.5/35_i.py) | [✅](./tests/3.5/test_35_i.py) |
| J. [Хвост](./solutions/3.5/35_j.py) | [✅](./tests/3.5/test_35_j.py) |
| K. [Файловая статистика 2.0](./solutions/3.5/35_k.py) | [✅](./tests/3.5/test_35_k.py) |
| L. [Разделяй и властвуй](./solutions/3.5/35_l.py) | [✅](./tests/3.5/test_35_l.py) |
| M. [Обновление данных](./solutions/3.5/35_m.py) | [✅](./tests/3.5/test_35_m.py) |
| N. [Слияние данных](./solutions/3.5/35_n.py) | [✅](./tests/3.5/test_35_n.py) |
| O. [Поставь себя на моё место](./solutions/3.5/35_o.py) | [✅](./tests/3.5/test_35_o.py) |
| P. [Найдётся всё 3.0](./solutions/3.5/35_p.py) | [✅](./tests/3.5/test_35_p.py) |
| Q. [Прятки](./solutions/3.5/35_q.py) | [✅](./tests/3.5/test_35_q.py) |
| R. [Сколько вешать в байтах?](./solutions/3.5/35_r.py) | [✅](./tests/3.5/test_35_r.py) |
| S. [Это будет наш секрет](./solutions/3.5/35_s.py) | [✅](./tests/3.5/test_35_s.py) |
| T. [Файловая сумма](./solutions/3.5/35_t.py) | [✅](./tests/3.5/test_35_t.py) |

</details>

<details>
<summary><h3>4.1 Функции. Области видимости. Передача параметров в функции</h3></summary>

- [Теория Функции. Области видимости. Передача параметров в функции](https://education.yandex.ru/handbook/python/article/funkcii-oblasti-vidimosti-peredacha-parametrov-v-funkcii)

### [Тестовые данные для задач](./tests/data/test_data_41.py)

| Решение              | Тесты                |
|----------------------|----------------------|
| А. [Функциональное приветствие](./solutions/4.1/41_a.py) | [✅](./tests/4.1/test_41_a.py) |
| B. [Функциональный НОД](./solutions/4.1/41_b.py) | [✅](./tests/4.1/test_41_b.py) |
| C. [Длина числа](./solutions/4.1/41_c.py) | [✅](./tests/4.1/test_41_c.py) |
| D. [Имя of the month](./solutions/4.1/41_d.py) | [✅](./tests/4.1/test_41_d.py) |
| E. [Числовая строка](./solutions/4.1/41_e.py) | [✅](./tests/4.1/test_41_e.py) |
| F. [Модернизация системы вывода](./solutions/4.1/41_f.py) | [✅](./tests/4.1/test_41_f.py) |
| G. [Шахматный «обед»](./solutions/4.1/41_g.py) | [✅](./tests/4.1/test_41_g.py) |
| H. [А роза упала на лапу Азора 7.0](./solutions/4.1/41_h.py) | [✅](./tests/4.1/test_41_h.py) |
| I. [Простая задача 5.0](./solutions/4.1/41_i.py) | [✅](./tests/4.1/test_41_i.py) |
| J. [Слияние](./solutions/4.1/41_j.py) | [✅](./tests/4.1/test_41_j.py) |

</details>

<details>
<summary><h3>4.2 Позиционные и именованные аргументы. Функции высших порядков...</h3></summary>

- [Теория Позиционные и именованные аргументы. Функции высших порядков. Лямбда-функции](https://education.yandex.ru/handbook/python/article/pozicionnye-i-imenovannye-argumenty-funkcii-vysshih-poryadkov-lyambda-funkcii)

### [Тестовые данные для задач](./tests/data/test_data_42.py)

| Решение              | Тесты                |
|----------------------|----------------------|
| А. [Генератор списков](./solutions/4.2/42_a.py) | [✅](./tests/4.2/test_42_a.py) |
| B. [Генератор матриц](./solutions/4.2/42_b.py) | [✅](./tests/4.2/test_42_b.py) |
| C. [Функциональный нод 2.0](./solutions/4.2/42_c.py) | [✅](./tests/4.2/test_42_c.py) |
| D. [Имя of the month 2.0](./solutions/4.2/42_d.py) | [✅](./tests/4.2/test_42_d.py) |
| E. [Подготовка данных](./solutions/4.2/42_e.py) | [✅](./tests/4.2/test_42_e.py) |
| F. [Кофейня](./solutions/4.2/42_f.py) | [✅](./tests/4.2/test_42_f.py) |
| G. [В эфире рубрика «Эксперименты»](./solutions/4.2/42_g.py) | [✅](./tests/4.2/test_42_g.py) |
| H. [Длинная сортировка](./solutions/4.2/42_h.py) | [✅](./tests/4.2/test_42_h.py) |
| I. [Чётная фильтрация](./solutions/4.2/42_i.py) | [✅](./tests/4.2/test_42_i.py) |
| J. [Ключевой секрет](./solutions/4.2/42_j.py) | [✅](./tests/4.2/test_42_j.py) |

</details>

<details>
<summary><h3>4.3. Рекурсия. Декораторы. Генераторы</h3></summary>

- [Теория Рекурсия. Декораторы. Генераторы](https://education.yandex.ru/handbook/python/article/rekursiya-dekoratory-generatory)

### [Тестовые данные для задач](./tests/data/test_data_43.py)

| Решение              | Тесты                |
|----------------------|----------------------|
| А. [Рекурсивный сумматор](./solutions/4.3/43_a.py) | [✅](./tests/4.3/test_43_a.py) |
| B. [Рекурсивный сумматор цифр](./solutions/4.3/43_b.py) | [✅](./tests/4.3/test_43_b.py) |
| C. [Многочлен N-ой степени](./solutions/4.3/43_c.py) | [✅](./tests/4.3/test_43_c.py) |
| D. [Декор результата](./solutions/4.3/43_d.py) | [✅](./tests/4.3/test_43_d.py) |
| E. [Накопление результата](./solutions/4.3/43_e.py) | [✅](./tests/4.3/test_43_e.py) |
| F. [Сортировка слиянием](./solutions/4.3/43_f.py) | [✅](./tests/4.3/test_43_f.py) |
| G. [Однотипность не порок](./solutions/4.3/43_g.py) | [✅](./tests/4.3/test_43_g.py) |
| H. [Генератор Фибоначчи](./solutions/4.3/43_h.py) | [✅](./tests/4.3/test_43_h.py) |
| I. [Циклический генератор](./solutions/4.3/43_i.py) | [✅](./tests/4.3/test_43_i.py) |
| J. ["Выпрямление" списка](./solutions/4.3/43_j.py) | [✅](./tests/4.3/test_43_j.py) |

</details>

<details>
<summary><h3>5.1 Объектная модель Python. Классы, поля и методы</h3></summary>

- [Теория Объектная модель Python. Классы, поля и методы](https://education.yandex.ru/handbook/python/article/obuektnaya-model-python-klassy-polya-i-metody)

### [Тестовые данные для задач](./tests/data/test_data_51.py)

| Решение              | Тесты                |
|----------------------|----------------------|
| А. [Классная точка](./solutions/5.1/51_a.py) | [✅](./tests/5.1/test_51_a.py) |
| B. [Классная точка 2.0](./solutions/5.1/51_b.py) | [✅](./tests/5.1/test_51_b.py) |
| C. [Не нажимай красную кнопку!](./solutions/5.1/51_c.py) | [✅](./tests/5.1/test_51_c.py) |
| D. [Работа не волк](./solutions/5.1/51_d.py) | [✅](./tests/5.1/test_51_d.py) |
| E. [Классный прямоугольник](./solutions/5.1/51_e.py) | [✅](./tests/5.1/test_51_e.py) |
| F. [Классный прямоугольник 2.0](./solutions/5.1/51_f.py) | [✅](./tests/5.1/test_51_f.py) |
| G. [Классный прямоугольник 3.0](./solutions/5.1/51_g.py) | [✅](./tests/5.1/test_51_g.py) |
| H. [Шашки](./solutions/5.1/51_h.py) | [✅](./tests/5.1/test_51_h.py) |
| I. [Очередь](./solutions/5.1/51_i.py) | [✅](./tests/5.1/test_51_i.py) |
| J. [Стэк](./solutions/5.1/51_j.py) | [✅](./tests/5.1/test_51_j.py) |

</details>

<details>
<summary><h3>5.2 Волшебные методы, переопределение методов. Наследование</h3></summary>

- [Теория Волшебные методы, переопределение методов. Наследование](https://education.yandex.ru/handbook/python/article/volshebnye-metody-pereopredelenie-metodov-nasledovanie)

### [Тестовые данные для задач](./tests/data/test_data_52.py)

| Решение              | Тесты                |
|----------------------|----------------------|
| А. [Классная точка 3.0](./solutions/5.2/52_a.py) | [✅](./tests/5.2/test_52_a.py) |
| B. [Классная точка 4.0](./solutions/5.2/52_b.py) | [✅](./tests/5.2/test_52_b.py) |
| C. [Классная точка 5.0](./solutions/5.2/52_c.py) | [✅](./tests/5.2/test_52_c.py) |
| D. [Дроби v0.1](./solutions/5.2/52_d.py) | [✅](./tests/5.2/test_52_d.py) |
| E. [Дроби v0.2](./solutions/5.2/52_e.py) | [✅](./tests/5.2/test_52_e.py) |
| F. [Дроби v0.3](./solutions/5.2/52_f.py) | [✅](./tests/5.2/test_52_f.py) |
| G. [Дроби v0.4](./solutions/5.2/52_g.py) | [✅](./tests/5.2/test_52_g.py) |
| H. [Дроби v0.5](./solutions/5.2/52_h.py) | [✅](./tests/5.2/test_52_h.py) |
| I. [Дроби v0.6](./solutions/5.2/52_i.py) | [✅](./tests/5.2/test_52_i.py) |
| J. [Дроби v0.7](./solutions/5.2/52_j.py) | [✅](./tests/5.2/test_52_j.py) |

</details>

<details>
<summary><h3>5.3 Модель исключений Python. Try, except, else, finally.</h3></summary>

- [Теория Модель исключений Python. Try, except, else, finally. Модули](https://education.yandex.ru/handbook/python/article/model-isklyuchenij-python-try-except-else-finally-moduli)

### [Тестовые данные для задач](./tests/data/test_data_53.py)

| Решение              | Тесты                |
|----------------------|----------------------|
| А. [Обработка ошибок](./solutions/5.3/53_a.py) | [✅](./tests/5.3/test_53_a.py) |
| B. [Ломать — не строить](./solutions/5.3/53_b.py) | [✅](./tests/5.3/test_53_b.py) |
| C. [Ломать — не строить 2](./solutions/5.3/53_c.py) | [✅](./tests/5.3/test_53_c.py) |
| D. [Контроль параметров](./solutions/5.3/53_d.py) | [✅](./tests/5.3/test_53_d.py) |
| E. [Слияние с проверкой](./solutions/5.3/53_e.py) | [✅](./tests/5.3/test_53_e.py) |
| F. [Корень зла 2](./solutions/5.3/53_f.py) | [✅](./tests/5.3/test_53_f.py) |
| G. [Валидация имени](./solutions/5.3/53_g.py) | [✅](./tests/5.3/test_53_g.py) |
| H. [Валидация имени пользователя](./solutions/5.3/53_h.py) | [✅](./tests/5.3/test_53_h.py) |
| I. [Валидация пользователя](./solutions/5.3/53_i.py) | [✅](./tests/5.3/test_53_i.py) |
| J. [Валидация пароля](./solutions/5.3/53_j.py) | [✅](./tests/5.3/test_53_j.py) |

</details>

<details>
<summary><h3>6.1 Модули math и numpy</h3></summary>

- [Теория Модули math и numpy](https://education.yandex.ru/handbook/python/article/moduli-math-i-numpy)

### [Тестовые данные для задач](./tests/data/test_data_61.py)

| Решение              | Тесты                |
|----------------------|----------------------|
| А. [Математика — круто, но это не точно](./solutions/6.1/61_a.py) | [✅](./tests/6.1/test_61_a.py) |
| B. [Потоковый НОД](./solutions/6.1/61_b.py) | [✅](./tests/6.1/test_61_b.py) |
| C. [Есть варианты?](./solutions/6.1/61_c.py) | [✅](./tests/6.1/test_61_c.py) |
| D. [Среднее не арифметическое](./solutions/6.1/61_d.py) | [✅](./tests/6.1/test_61_d.py) |
| E. [Шаг навстречу](./solutions/6.1/61_e.py) | [✅](./tests/6.1/test_61_e.py) |
| F. [Матрица умножения](./solutions/6.1/61_f.py) | [✅](./tests/6.1/test_61_f.py) |
| G. [Шахматная подготовка](./solutions/6.1/61_g.py) | [✅](./tests/6.1/test_61_g.py) |
| H. [Числовая змейка 3.0](./solutions/6.1/61_h.py) | [✅](./tests/6.1/test_61_h.py) |
| I. [Вращение](./solutions/6.1/61_i.py) | [✅](./tests/6.1/test_61_i.py) |
| J. [Лесенка](./solutions/6.1/61_j.py) | [✅](./tests/6.1/test_61_j.py) |

</details>

<details>
<summary><h3>6.2 Модуль pandas</h3></summary>

- [Теория Модуль pandas](https://education.yandex.ru/handbook/python/article/modul-pandas)

### [Тестовые данные для задач](./tests/data/test_data_62.py)

| Решение              | Тесты                |
|----------------------|----------------------|
| А. [Длины всех слов - 2](./solutions/6.2/62_a.py) | [✅](./tests/6.2/test_62_a.py) |
| B. [Длины всех слов по чётности](./solutions/6.2/62_b.py) | [✅](./tests/6.2/test_62_b.py) |
| C. [Чек - 2](./solutions/6.2/62_c.py) | [✅](./tests/6.2/test_62_c.py) |
| D. [Акция](./solutions/6.2/62_d.py) | [✅](./tests/6.2/test_62_d.py) |
| E. [Длинные слова](./solutions/6.2/62_e.py) | [✅](./tests/6.2/test_62_e.py) |
| F. [Отчёт успеваемости](./solutions/6.2/62_f.py) | [✅](./tests/6.2/test_62_f.py) |
| G. [Отчёт неуспеваемости](./solutions/6.2/62_g.py) | [✅](./tests/6.2/test_62_g.py) |
| H. [Обновление журнала](./solutions/6.2/62_h.py) | [✅](./tests/6.2/test_62_h.py) |
| I. [Бесконечный морской бой](./solutions/6.2/62_i.py) | [✅](./tests/6.2/test_62_i.py) |
| J. [Экстремум функции](./solutions/6.2/62_j.py) | [✅](./tests/6.2/test_62_j.py) |

</details>

<details>
<summary><h3>6.3 Модуль requests</h3></summary>

- [Теория Модуль requests](https://education.yandex.ru/handbook/python/article/modul-requests)

### [Тестовые данные для задач](./tests/data/test_data_63.py)

| Решение              | Тесты                |
|----------------------|----------------------|
| А. [Проверка системы](./solutions/6.3/63_a.py) | [✅](./tests/6.3/test_63_a.py) |
| B. [Суммирование ответов](./solutions/6.3/63_b.py) | [✅](./tests/6.3/test_63_b.py) |
| C. [Суммирование ответов 2](./solutions/6.3/63_c.py) | [✅](./tests/6.3/test_63_c.py) |
| D. [Конкретное значение](./solutions/6.3/63_d.py) | [✅](./tests/6.3/test_63_d.py) |
| E. [Суммирование ответов 3](./solutions/6.3/63_e.py) | [✅](./tests/6.3/test_63_e.py) |
| F. [Список пользователей](./solutions/6.3/63_f.py) | [✅](./tests/6.3/test_63_f.py) |
| G. [Рассылка сообщений](./solutions/6.3/63_g.py) | [✅](./tests/6.3/test_63_g.py) |
| H. [Регистрация нового пользователя](./solutions/6.3/63_h.py) | [✅](./tests/6.3/test_63_h.py) |
| I. [Изменение данных](./solutions/6.3/63_i.py) | [✅](./tests/6.3/test_63_i.py) |
| J. [Удаление данных](./solutions/6.3/63_j.py) | [✅](./tests/6.3/test_63_j.py) |

</details>

<details>
<summary><h3>Почему создаются временные файлы?</h3></summary>

Чтобы отслеживать, насколько тесты покрывают код, обычно импортируют тестируемую функцию, и инструмент `coverage` показывает, какие строки были выполнены, а какие нет. Однако в первых трех параграфах учебника, где еще не введены функции, решения представлены просто как последовательность команд без определения функции. 

В таких случаях мы можем протестировать код напрямую из файла, но не получим данных о покрытии строк. Чтобы обойти это ограничение, я написал функцию `wrap_answer` ([см. здесь](./tests/conftest.py)). Эта функция запускается при старте тестов и принимает параметры: путь к тестируемому файлу и имя файла. Она читает код задачи из файла, оборачивает его в функцию `main`, и сохраняет результат в файл `wrapped_(адрес папки)_(буква задачи).py`. Затем уже этот новый файл тестируется, и `coverage` фиксирует, какие строки были выполнены. Благодаря этому становится возможным отслеживать покрытие строк даже для кода, написанного без функций.

Кроме того, оборачивание кода в функцию `main` нужно для измерения потребляемой памяти и времени выполнения кода. Функция `wrap_answer` добавляет к обертке декораторы `@time_limit` и `@memory_limit`, которые устанавливают ограничения на время исполнения и объем памяти, выделяемой для задачи. Эти ограничения задаются константами `TIME_LIMIT` и `MEMORY_LIMIT` и контролируются в тестах.

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
        root_one = round((-b + discriminant**0.5) / (2 * a), 2)
        root_two = round((-b - discriminant**0.5) / (2 * a), 2)
        if not discriminant:
            print(root_two)
        elif root_one < root_two:  # Условие выполняется при a < 0
            print(root_one, root_two)
        else:
            print(root_two, root_one)
    else:  # Дискриминант меньше 0
        print("No solution")
```

Файл `wrapped_22_q.py` после применения `wrap_answer` к `22_q.py`:

```python
from tests.utils import time_limit, memory_limit
from tests.constants import TIME_LIMIT, MEMORY_LIMIT


@time_limit(TIME_LIMIT)
@memory_limit(MEMORY_LIMIT)
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
            root_one = round((-b + discriminant**0.5) / (2 * a), 2)
            root_two = round((-b - discriminant**0.5) / (2 * a), 2)
            if not discriminant:
                print(root_two)
            elif root_one < root_two:  # Условие выполняется при a < 0
                print(root_one, root_two)
            else:
                print(root_two, root_one)
        else:  # Дискриминант меньше 0
            print("No solution")
```

После того как отчет по покрытию готов, файлы удаляются.

</details>

<details>
<summary><h2>Создание Issue</h2></summary>

Если вы обнаружили ошибку, очепятку или баг в проекте, пожалуйста, создайте новый issue, следуя этому шаблону:

### Шаблон для Issue

#### Описание ошибки

- Краткое описание проблемы.

#### Шаги для воспроизведения

1. Опишите последовательность шагов, которые привели к появлению ошибки.
2. Укажите точные команды, скрипты или действия, названия файла(ов) если возможно.

#### Ожидаемое поведение

- Опишите, как все должно работать при нормальных условиях.

#### Фактическое поведение

- Опишите, что происходит на самом деле.

#### Контекст и окружение

- Операционная система и версия.
- Версия используемого ПО (Python, VSCode, PyCharm, etc.).
- Укажите любые установленные зависимости (например, версии библиотек).

#### Логи и скриншоты

- Прикрепите любые ошибки из логов или скриншоты, если это применимо.

#### Дополнительная информация

- Любые другие важные детали, которые помогут в исправлении ошибки.

---

Спасибо за ваш вклад! 😊

</details>

## Автор

- [Andrei Pomortsev](https://www.linkedin.com/in/andreypomortsev/)