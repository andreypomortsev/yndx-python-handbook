# Yandex Python Handbook Solutions

![Codacy grade (branch)](https://img.shields.io/codacy/grade/63f71a9c86ce4a0492af52c23628b78a/main)
![Build Status](https://github.com/andreypomortsev/yndx-python-handbook/actions/workflows/ci.yml/badge.svg)
[![codecov](https://codecov.io/gh/andreypomortsev/yndx-python-handbook/branch/main/graph/badge.svg?token=WPUYVICKGT)](https://codecov.io/gh/andreypomortsev/yndx-python-handbook)
![Python 3.12](https://img.shields.io/badge/Python-3.12-yellow.svg)
![Python 3.13](https://img.shields.io/badge/Python-3.13-green.svg)
![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)

Solutions for [Yandex Python Fundamentals Handbook](https://education.yandex.ru/handbook/python) problems with comprehensive test coverage.

## 📖 About

This repository contains solutions to problems from Yandex's Python handbook, following a structured learning approach:

- Solutions follow the handbook's progression (e.g., no functions before Module 4, no lists/sets/dictionaries before Module 3)
- Each solution includes comprehensive tests
- Code follows PEP 8 style guidelines
- Full test coverage reporting

## 🚀 Getting Started

### Prerequisites

- Python 3.12+ ([Download Python](https://www.python.org/downloads/))
- Git ([Download Git](https://git-scm.com/downloads))

### Installation Options

<details>
<summary><h3>Standard Installation (without venv)</h3></summary>

#### Clone and setup project

```bash
git clone https://github.com/andreypomortsev/yndx-python-handbook
cd yndx-python-handbook
```

#### Install dependencies

```bash
pip install -r requirements.txt
```

</details>

<details>
<summary><h3>Poetry Installation (recommended)</h3></summary>

#### Clone and setup project

    ```bash
    git clone https://github.com/andreypomortsev/yndx-python-handbook
    cd yndx-python-handbook
    ```

- #### Windows
    
    #### Install Poetry

    ```powershell
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
    ```

    #### Install dependencies

    ```bash
    poetry install
    poetry shell
    ```

- #### Unix/MacOS
    
    #### Install Poetry

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

    #### Install dependencies

    ```bash
    make setup
    poetry shell
    ```

</details>

## 🛠️ Development Commands

### Code Quality

#### Format code

- #### Windows

    ```powershell
    poetry run black . --line-length=79
    poetry run isort .
    ```

- #### Unix/MacOS

    ```bash 
    make format
    ```

#### Lint code

- #### Windows

    ```powershell
    poetry run flake8 .
    ```

- #### Unix/MacOS

    ```bash 
    make lint
    ```

### Testing

- #### Windows

    *Run All Tests*
    
    ```powershell
    poetry run pytest
    ```

    *Run tests with verbose output*

    ```powershell
    poetry run pytest -vv
    ```

    *Test specific section*

    ```powershell
    poetry run pytest tests\2.1
    ```

    *Test specific problem*
    
    ```powershell
    poetry run pytest tests\2.3\test_23_q.py
    ```
    
    *Generate coverage HTML report*

    ```powershell
    poetry run pytest --cov-report=html
    ```

    *Generate coverage XML report*
    
    ```powershell
    poetry run pytest --cov-report=xml
    ```

- #### Unix/MacOS

    *Run All Tests*
    ```bash
    make test
    ```

    *Run tests with verbose output*
    
    ```bash
    make debug
    ```

    *Test specific section*

    ```bash
    make test-dir-2.1
    ```

    *Test specific problem*

    ```bash
    make test-file-2.3-Q
    ```

    *Generate coverage HTML report*

    ```bash
    make test-report-html
    ```

    *Generate coverage XML report*

    ```bash
    make test-report-xml
    ```

## 📚 Solutions Structure

Solutions are organized by handbook sections. Each solution:
- Follows the handbook's progression
- Includes comprehensive tests
- Maintains 100% test coverage
- Adheres to PEP 8 style guidelines

### Available Solutions

<details>
<summary><h3>2.1 Data Input/Output, Number Operations, String Formatting</h3></summary>

[📖 Theory](https://education.yandex.ru/handbook/python/article/vvod-i-vyvod-dannykh-operatsii-s-chislami-strokami-formatirovaniye) | [🧪 Test Data](./tests/data/test_data_21.py)

### [Тестовые данные для задач](./tests/data/test_data_21.py)
  
| Задача               | Решение              | Тесты                |
|----------------------|----------------------|----------------------|
| А. [Hello, Yandex!](./problems/russian/2.1/problem_21_a_ru.md) | [✅](./solutions/2.1/21_a.py) | [✅](./tests/2.1/test_21_a.py) |
| B. [Hello, everyone!](./problems/russian/2.1/problem_21_b_ru.md) | [✅](./solutions/2.1/21_b.py) | [✅](./tests/2.1/test_21_b.py) |
| C. [Excessive Automation](./problems/russian/2.1/problem_21_c_ru.md) | [✅](./solutions/2.1/21_c.py) | [✅](./tests/2.1/test_21_c.py) |
| D. [Change Calculation](./problems/russian/2.1/problem_21_d_ru.md) | [✅](./solutions/2.1/21_d.py) | [✅](./tests/2.1/test_21_d.py) |
| E. [Store](./problems/russian/2.1/problem_21_e_ru.md) | [✅](./solutions/2.1/21_e.py) | [✅](./tests/2.1/test_21_e.py) |
| F. [Receipt](./problems/russian/2.1/problem_21_f_ru.md) | [✅](./solutions/2.1/21_f.py) | [✅](./tests/2.1/test_21_f.py) |
| G. [Work Hard, Play Hard](./problems/russian/2.1/problem_21_g_ru.md) | [✅](./solutions/2.1/21_g.py) | [✅](./tests/2.1/test_21_g.py) |
| H. [Punishment](./problems/russian/2.1/problem_21_h_ru.md) | [✅](./solutions/2.1/21_h.py) | [✅](./tests/2.1/test_21_h.py) |
| I. [Businesslike Sausage](./problems/russian/2.1/problem_21_i_ru.md) | [✅](./solutions/2.1/21_i.py) | [✅](./tests/2.1/test_21_i.py) |
| J. [Kindergarten — Overalls](./problems/russian/2.1/problem_21_j_ru.md) | [✅](./solutions/2.1/21_j.py) | [✅](./tests/2.1/test_21_j.py) |
| K. [Game Automation](./problems/russian/2.1/problem_21_k_ru.md) | [✅](./solutions/2.1/21_k.py) | [✅](./tests/2.1/test_21_k.py) |
| L. [Interesting Addition](./problems/russian/2.1/problem_21_l_ru.md) | [✅](./solutions/2.1/21_l.py) | [✅](./tests/2.1/test_21_l.py) |
| M. [Santa Claus and Candy](./problems/russian/2.1/problem_21_m_ru.md) | [✅](./solutions/2.1/21_m.py) | [✅](./tests/2.1/test_21_m.py) |
| N. [Balls and Pens](./problems/russian/2.1/problem_21_n_ru.md) | [✅](./solutions/2.1/21_n.py) | [✅](./tests/2.1/test_21_n.py) |
| O. [Waiting for Delivery](./problems/russian/2.1/problem_21_o_ru.md) | [✅](./solutions/2.1/21_o.py) | [✅](./tests/2.1/test_21_o.py) |
| P. [Delivery](./problems/russian/2.1/problem_21_p_ru.md) | [✅](./solutions/2.1/21_p.py) | [✅](./tests/2.1/test_21_p.py) |
| Q. [Cash Register Error](./problems/russian/2.1/problem_21_q_ru.md) | [✅](./solutions/2.1/21_q.py) | [✅](./tests/2.1/test_21_q.py) |
| R. [Change 10](./problems/russian/2.1/problem_21_r_ru.md) | [✅](./solutions/2.1/21_r.py) | [✅](./tests/2.1/test_21_r.py) |
| S. [Receipt Decoration](./problems/russian/2.1/problem_21_s_ru.md) | [✅](./solutions/2.1/21_s.py) | [✅](./tests/2.1/test_21_s.py) |
| T. [Flies and Cutlets Separately](./problems/russian/2.1/problem_21_t_ru.md) | [✅](./solutions/2.1/21_t.py) | [✅](./tests/2.1/test_21_t.py) |

</details>

## 🧪 Test Files

During testing, temporary files are created in the `tests` directory. These files:
- Wrap solutions in testable functions, I/O files for test purposes
- Enable coverage tracking
- Implement memory and time limits
- Are automatically cleaned up after testing

## 📝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
