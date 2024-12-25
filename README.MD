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

  
| Problems             | Solutions            | Tests                |
|----------------------|----------------------|----------------------|
| А. [Hello, Yandex!](./problems/english/2.1/problem_21_a_en.md) | [✅](./solutions/2.1/21_a.py) | [✅](./tests/2.1/test_21_a.py) |
| B. [Hello, everyone!](./problems/english/2.1/problem_21_b_en.md) | [✅](./solutions/2.1/21_b.py) | [✅](./tests/2.1/test_21_b.py) |
| C. [Excessive Automation](./problems/english/2.1/problem_21_c_en.md) | [✅](./solutions/2.1/21_c.py) | [✅](./tests/2.1/test_21_c.py) |
| D. [Change Calculation](./problems/english/2.1/problem_21_d_en.md) | [✅](./solutions/2.1/21_d.py) | [✅](./tests/2.1/test_21_d.py) |
| E. [Store](./problems/english/2.1/problem_21_e_en.md) | [✅](./solutions/2.1/21_e.py) | [✅](./tests/2.1/test_21_e.py) |
| F. [Receipt](./problems/english/2.1/problem_21_f_en.md) | [✅](./solutions/2.1/21_f.py) | [✅](./tests/2.1/test_21_f.py) |
| G. [Work Hard, Play Hard](./problems/english/2.1/problem_21_g_en.md) | [✅](./solutions/2.1/21_g.py) | [✅](./tests/2.1/test_21_g.py) |
| H. [Punishment](./problems/english/2.1/problem_21_h_en.md) | [✅](./solutions/2.1/21_h.py) | [✅](./tests/2.1/test_21_h.py) |
| I. [Businesslike Sausage](./problems/english/2.1/problem_21_i_en.md) | [✅](./solutions/2.1/21_i.py) | [✅](./tests/2.1/test_21_i.py) |
| J. [Kindergarten — Overalls](./problems/english/2.1/problem_21_j_en.md) | [✅](./solutions/2.1/21_j.py) | [✅](./tests/2.1/test_21_j.py) |
| K. [Game Automation](./problems/english/2.1/problem_21_k_en.md) | [✅](./solutions/2.1/21_k.py) | [✅](./tests/2.1/test_21_k.py) |
| L. [Interesting Addition](./problems/english/2.1/problem_21_l_en.md) | [✅](./solutions/2.1/21_l.py) | [✅](./tests/2.1/test_21_l.py) |
| M. [Santa Claus and Candy](./problems/english/2.1/problem_21_m_en.md) | [✅](./solutions/2.1/21_m.py) | [✅](./tests/2.1/test_21_m.py) |
| N. [Balls and Pens](./problems/english/2.1/problem_21_n_en.md) | [✅](./solutions/2.1/21_n.py) | [✅](./tests/2.1/test_21_n.py) |
| O. [Waiting for Delivery](./problems/english/2.1/problem_21_o_en.md) | [✅](./solutions/2.1/21_o.py) | [✅](./tests/2.1/test_21_o.py) |
| P. [Delivery](./problems/english/2.1/problem_21_p_en.md) | [✅](./solutions/2.1/21_p.py) | [✅](./tests/2.1/test_21_p.py) |
| Q. [Cash Register Error](./problems/english/2.1/problem_21_q_en.md) | [✅](./solutions/2.1/21_q.py) | [✅](./tests/2.1/test_21_q.py) |
| R. [Change 10](./problems/english/2.1/problem_21_r_en.md) | [✅](./solutions/2.1/21_r.py) | [✅](./tests/2.1/test_21_r.py) |
| S. [Receipt Decoration](./problems/english/2.1/problem_21_s_en.md) | [✅](./solutions/2.1/21_s.py) | [✅](./tests/2.1/test_21_s.py) |
| T. [Flies and Cutlets Separately](./problems/english/2.1/problem_21_t_en.md) | [✅](./solutions/2.1/21_t.py) | [✅](./tests/2.1/test_21_t.py) |

</details>

<details>
<summary><h3>2.2 The conditional operator</h3></summary>

[📖 Theory 2.2](https://education.yandex.ru/handbook/python/article/uslovnyy-operator) | [🧪 Test Data](./tests/data/test_data_22.py)

| Problems             | Solutions            | Tests                |
|----------------------|----------------------|----------------------|
| А. [Just hello, just how are you?](./problems/russian/2.2/problem_22_a_en.md) | [✅](./solutions/2.2/22_a.py) | [✅](./tests/2.2/test_22_a.py) |
| B. [Who is faster?](./problems/russian/2.2/problem_22_b_en.md) | [✅](./solutions/2.2/22_b.py) | [✅](./tests/2.2/test_22_b.py) |
| C. [Who is faster this time?](./problems/russian/2.2/problem_22_c_en.md) | [✅](./solutions/2.2/22_c.py) | [✅](./tests/2.2/test_22_c.py) |
| D. [List of Winners](./problems/russian/2.2/problem_22_d_en.md) | [✅](./solutions/2.2/22_d.py) | [✅](./tests/2.2/test_22_d.py) |
| E. [Apples](./problems/russian/2.2/problem_22_e_en.md) | [✅](./solutions/2.2/22_e.py) | [✅](./tests/2.2/test_22_e.py) |
| F. [Power of procrastination](./problems/russian/2.2/problem_22_f_en.md) | [✅](./solutions/2.2/22_f.py) | [✅](./tests/2.2/test_22_f.py) |
| G. [Race car](./problems/russian/2.2/problem_22_g_en.md) | [✅](./solutions/2.2/22_g.py) | [✅](./tests/2.2/test_22_g.py) |
| H. [Bunny — 1](./problems/russian/2.2/problem_22_h_en.md) | [✅](./solutions/2.2/22_h.py) | [✅](./tests/2.2/test_22_h.py) |
| I. [First player, get ready](./problems/russian/2.2/problem_22_i_en.md) | [✅](./solutions/2.2/22_i.py) | [✅](./tests/2.2/test_22_i.py) |
| J. [Best defense is encryption](./problems/russian/2.2/problem_22_j_en.md) | [✅](./solutions/2.2/22_j.py) | [✅](./tests/2.2/test_22_j.py) |
| K. [Beauty will save the world](./problems/russian/2.2/problem_22_k_en.md) | [✅](./solutions/2.2/22_k.py) | [✅](./tests/2.2/test_22_k.py) |
| L. [Musical Instrument](./problems/russian/2.2/problem_22_l_en.md) | [✅](./solutions/2.2/22_l.py) | [✅](./tests/2.2/test_22_l.py) |
| M. [Lord of Numbers: The Fellowship of the Common Digit](./problems/russian/2.2/problem_22_m_en.md) | [✅](./solutions/2.2/22_m.py) | [✅](./tests/2.2/test_22_m.py) |
| N. [Lord of Numbers: The Two Towers](./problems/russian/2.2/problem_22_n_en.md) | [✅](./solutions/2.2/22_n.py) | [✅](./tests/2.2/test_22_n.py) |
| O. [Lord of Numbers: The Return of Caesar](./problems/russian/2.2/problem_22_o_en.md) | [✅](./solutions/2.2/22_o.py) | [✅](./tests/2.2/test_22_o.py) |
| P. [Legends of the Cycling Race Return: Who is Faster?](./problems/russian/2.2/problem_22_p_en.md) | [✅](./solutions/2.2/22_p.py) | [✅](./tests/2.2/test_22_p.py) |
| Q. [Root of Evil](./problems/russian/2.2/problem_22_q_en.md) | [✅](./solutions/2.2/22_q.py) | [✅](./tests/2.2/test_22_q.py) |
| R. [Territory of Evil](./problems/russian/2.2/problem_22_r_en.md) | [✅](./solutions/2.2/22_r.py) | [✅](./tests/2.2/test_22_r.py) |
| S. [Automation of Safety](./problems/russian/2.2/problem_22_s_en.md) | [✅](./solutions/2.2/22_s.py) | [✅](./tests/2.2/test_22_s.py) |
| T. [Bunnie — 2](./problems/russian/2.2/problem_22_t_en.md) | [✅](./solutions/2.2/22_t.py) | [✅](./tests/2.2/test_22_t.py) |

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
