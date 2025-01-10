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

[📖 Theory 2.1](https://education.yandex.ru/handbook/python/article/vvod-i-vyvod-dannykh-operatsii-s-chislami-strokami-formatirovaniye) | [🧪 Test Data](./tests/data/test_data_21.py)

  
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
| А. [Just hello, just how are you?](./problems/english/2.2/problem_22_a_en.md) | [✅](./solutions/2.2/22_a.py) | [✅](./tests/2.2/test_22_a.py) |
| B. [Who is faster?](./problems/english/2.2/problem_22_b_en.md) | [✅](./solutions/2.2/22_b.py) | [✅](./tests/2.2/test_22_b.py) |
| C. [Who is faster this time?](./problems/english/2.2/problem_22_c_en.md) | [✅](./solutions/2.2/22_c.py) | [✅](./tests/2.2/test_22_c.py) |
| D. [List of Winners](./problems/english/2.2/problem_22_d_en.md) | [✅](./solutions/2.2/22_d.py) | [✅](./tests/2.2/test_22_d.py) |
| E. [Apples](./problems/english/2.2/problem_22_e_en.md) | [✅](./solutions/2.2/22_e.py) | [✅](./tests/2.2/test_22_e.py) |
| F. [Power of procrastination](./problems/english/2.2/problem_22_f_en.md) | [✅](./solutions/2.2/22_f.py) | [✅](./tests/2.2/test_22_f.py) |
| G. [Race car](./problems/english/2.2/problem_22_g_en.md) | [✅](./solutions/2.2/22_g.py) | [✅](./tests/2.2/test_22_g.py) |
| H. [Bunny — 1](./problems/english/2.2/problem_22_h_en.md) | [✅](./solutions/2.2/22_h.py) | [✅](./tests/2.2/test_22_h.py) |
| I. [First player, get ready](./problems/english/2.2/problem_22_i_en.md) | [✅](./solutions/2.2/22_i.py) | [✅](./tests/2.2/test_22_i.py) |
| J. [Best defense is encryption](./problems/english/2.2/problem_22_j_en.md) | [✅](./solutions/2.2/22_j.py) | [✅](./tests/2.2/test_22_j.py) |
| K. [Beauty will save the world](./problems/english/2.2/problem_22_k_en.md) | [✅](./solutions/2.2/22_k.py) | [✅](./tests/2.2/test_22_k.py) |
| L. [Musical Instrument](./problems/english/2.2/problem_22_l_en.md) | [✅](./solutions/2.2/22_l.py) | [✅](./tests/2.2/test_22_l.py) |
| M. [Lord of Numbers: The Fellowship of the Common Digit](./problems/english/2.2/problem_22_m_en.md) | [✅](./solutions/2.2/22_m.py) | [✅](./tests/2.2/test_22_m.py) |
| N. [Lord of Numbers: The Two Towers](./problems/english/2.2/problem_22_n_en.md) | [✅](./solutions/2.2/22_n.py) | [✅](./tests/2.2/test_22_n.py) |
| O. [Lord of Numbers: The Return of Caesar](./problems/english/2.2/problem_22_o_en.md) | [✅](./solutions/2.2/22_o.py) | [✅](./tests/2.2/test_22_o.py) |
| P. [Legends of the Cycling Race Return: Who is Faster?](./problems/english/2.2/problem_22_p_en.md) | [✅](./solutions/2.2/22_p.py) | [✅](./tests/2.2/test_22_p.py) |
| Q. [Root of Evil](./problems/english/2.2/problem_22_q_en.md) | [✅](./solutions/2.2/22_q.py) | [✅](./tests/2.2/test_22_q.py) |
| R. [Territory of Evil](./problems/english/2.2/problem_22_r_en.md) | [✅](./solutions/2.2/22_r.py) | [✅](./tests/2.2/test_22_r.py) |
| S. [Automation of Safety](./problems/english/2.2/problem_22_s_en.md) | [✅](./solutions/2.2/22_s.py) | [✅](./tests/2.2/test_22_s.py) |
| T. [Bunnie — 2](./problems/english/2.2/problem_22_t_en.md) | [✅](./solutions/2.2/22_t.py) | [✅](./tests/2.2/test_22_t.py) |

</details>

<details>
<summary><h3>2.3 Loops</h3></summary>

[📖 Theory 2.3](https://education.yandex.ru/handbook/python/article/cikly) | [🧪 Test Data](./tests/data/test_data_23.py)

| Problems             | Solutions            | Tests                |
|----------------------|----------------------|----------------------|
| А. [One, Two, Three, Tree, Light Up! ](./problems/english/2.3/problem_23_a_en.md) | [✅](./solutions/2.3/23_a.py) | [✅](./tests/2.3/test_23_a.py) |
| B. [Bunny — 3](./problems/english/2.3/problem_23_b_en.md) | [✅](./solutions/2.3/23_b.py) | [✅](./tests/2.3/test_23_b.py) |
| C. [Counting Game](./problems/english/2.3/problem_23_c_en.md) | [✅](./solutions/2.3/23_c.py) | [✅](./tests/2.3/test_23_c.py) |
| D. [Counting Game 2.0](./problems/english/2.3/problem_23_d_en.md) | [✅](./solutions/2.3/23_d.py) | [✅](./tests/2.3/test_23_d.py) |
| E. [Attention! Promotion!](./problems/english/2.3/problem_23_e_en.md) | [✅](./solutions/2.3/23_e.py) | [✅](./tests/2.3/test_23_e.py) |
| F. [GCD](./problems/english/2.3/problem_23_f_en.md) | [✅](./solutions/2.3/23_f.py) | [✅](./tests/2.3/test_23_f.py) |
| G. [LCM](./problems/english/2.3/problem_23_g_en.md) | [✅](./solutions/2.3/23_g.py) | [✅](./tests/2.3/test_23_g.py) |
| H. [Excessive Automation 2.0](./problems/english/2.3/problem_23_h_en.md) | [✅](./solutions/2.3/23_h.py) | [✅](./tests/2.3/test_23_h.py) |
| I. [Factorial](./problems/english/2.3/problem_23_i_en.md) | [✅](./solutions/2.3/23_i.py) | [✅](./tests/2.3/test_23_i.py) |
| J. [Route Built](./problems/english/2.3/problem_23_j_en.md) | [✅](./solutions/2.3/23_j.py) | [✅](./tests/2.3/test_23_j.py) |
| K. [Digital Sum](./problems/english/2.3/problem_23_k_en.md) | [✅](./solutions/2.3/23_k.py) | [✅](./tests/2.3/test_23_k.py) |
| L. [Strong Digit](./problems/english/2.3/problem_23_l_en.md) | [✅](./solutions/2.3/23_l.py) | [✅](./tests/2.3/test_23_l.py) |
| M. [Player One, Prepare 2.0](./problems/english/2.3/problem_23_m_en.md) | [✅](./solutions/2.3/23_m.py) | [✅](./tests/2.3/test_23_m.py) |
| N. [Simple Task](./problems/english/2.3/problem_23_n_en.md) | [✅](./solutions/2.3/23_n.py) | [✅](./tests/2.3/test_23_n.py) |
| O. [Bunny - 4](./problems/english/2.3/problem_23_o_en.md) | [✅](./solutions/2.3/23_o.py) | [✅](./tests/2.3/test_23_o.py) |
| P. [Race car 2.0](./problems/english/2.3/problem_23_p_en.md) | [✅](./solutions/2.3/23_p.py) | [✅](./tests/2.3/test_23_p.py) |
| Q. [Even Cleanliness](./problems/english/2.3/problem_23_q_en.md) | [✅](./solutions/2.3/23_q.py) | [✅](./tests/2.3/test_23_q.py) |
| R. [Simple Task 2.0](./problems/english/2.3/problem_23_r_en.md) | [✅](./solutions/2.3/23_r.py) | [✅](./tests/2.3/test_23_r.py) |
| S. [Guessing Game](./problems/english/2.3/problem_23_s_en.md) | [✅](./solutions/2.3/23_s.py) | [✅](./tests/2.3/test_23_s.py) |
| T. [Let's Hype a Little!](./problems/english/2.3/problem_23_t_en.md) | [✅](./solutions/2.3/23_t.py) | [✅](./tests/2.3/test_23_t.py) |

</details>

<details>
<summary><h3>2.4 Nested loops</h3></summary>

- [📖 Theory 2.4](https://education.yandex.ru/handbook/python/article/vlozhennye-cikly) | [🧪 Test Data](./tests/data/test_data_24.py)

| Problems             | Solutions            | Tests                |
|----------------------|----------------------|----------------------|
| А. [Мultiplication table](./problems/english/2.4/problem_24_a_en.md) | [✅](./solutions/2.4/24_a.py) | [✅](./tests/2.4/test_24_a.py) |
| B. [Not multiplication table](./problems/english/2.4/problem_24_b_en.md) | [✅](./solutions/2.4/24_b.py) | [✅](./tests/2.4/test_24_b.py) |
| C. [New Year mood](./problems/english/2.4/problem_24_c_en.md) | [✅](./solutions/2.4/24_c.py) | [✅](./tests/2.4/test_24_c.py) |
| D. [Total amount](./problems/english/2.4/problem_24_d_en.md) | [✅](./solutions/2.4/24_d.py) | [✅](./tests/2.4/test_24_d.py) |
| E. [Bunny — 5](./problems/english/2.4/problem_24_e_en.md) | [✅](./solutions/2.4/24_e.py) | [✅](./tests/2.4/test_24_e.py) |
| F. [GCD 2.0](./problems/english/2.4/problem_24_f_en.md) | [✅](./solutions/2.4/24_f.py) | [✅](./tests/2.4/test_24_f.py) |
| G. [Ready! Steady! Go!](./problems/english/2.4/problem_24_g_en.md) | [✅](./solutions/2.4/24_g.py) | [✅](./tests/2.4/test_24_g.py) |
| H. [Maximum amount](./problems/english/2.4/problem_24_h_en.md) | [✅](./solutions/2.4/24_h.py) | [✅](./tests/2.4/test_24_h.py) |
| I. [Big number](./problems/english/2.4/problem_24_i_en.md) | [✅](./solutions/2.4/24_i.py) | [✅](./tests/2.4/test_24_i.py) |
| J. [We divided the orange](./problems/english/2.4/problem_24_j_en.md) | [✅](./solutions/2.4/24_j.py) | [✅](./tests/2.4/test_24_j.py) |
| K. [Simple task 3.0](./problems/english/2.4/problem_24_k_en.md) | [✅](./solutions/2.4/24_k.py) | [✅](./tests/2.4/test_24_k.py) |
| L. [Numerical rectangle](./problems/english/2.4/problem_24_l_en.md) | [✅](./solutions/2.4/24_l.py) | [✅](./tests/2.4/test_24_l.py) |
| M. [Numerical rectangle 2.0](./problems/english/2.4/problem_24_m_en.md) | [✅](./solutions/2.4/24_m.py) | [✅](./tests/2.4/test_24_m.py) |
| N. [Numerical snake](./problems/english/2.4/problem_24_n_en.md) | [✅](./solutions/2.4/24_n.py) | [✅](./tests/2.4/test_24_n.py) |
| O. [Numerical snake 2.0](./problems/english/2.4/problem_24_o_en.md) | [✅](./solutions/2.4/24_o.py) | [✅](./tests/2.4/test_24_o.py) |
| P. [Multiplication table redesign](./problems/english/2.4/problem_24_p_en.md) | [✅](./solutions/2.4/24_p.py) | [✅](./tests/2.4/test_24_p.py) |
| Q. [Racecar 3.0](./problems/english/2.4/problem_24_q_en.md) | [✅](./solutions/2.4/24_q.py) | [✅](./tests/2.4/test_24_q.py) |
| R. [New Year mood 2.0](./problems/english/2.4/problem_24_r_en.md) | [✅](./solutions/2.4/24_r.py) | [✅](./tests/2.4/test_24_r.py) |
| S. [Numerical square](./problems/english/2.4/problem_24_s_en.md) | [✅](./solutions/2.4/24_s.py) | [✅](./tests/2.4/test_24_s.py) |
| T. [Mathematical benefit](./problems/english/2.4/problem_24_t_en.md) | [✅](./solutions/2.4/24_t.py) | [✅](./tests/2.4/test_24_t.py) |

</details>

<details>
<summary><h3>3.1 String, tuple, list</h3></summary>

- [📖 Theory 3.1](https://education.yandex.ru/handbook/python/article/stroki-kortezhi-spiski) | [🧪 Test Data](./tests/data/test_data_31.py)

| Problems             | Solutions            | Tests                |
|----------------------|----------------------|----------------------|
| А. [Alphabet](./problems/english/3.1/problem_31_a_en.md) | [✅](./solutions/3.1/31_a.py) | [✅](./tests/3.1/test_31_a.py) |
| B. [I spin and twist](./problems/english/3.1/problem_31_b_en.md) | [✅](./solutions/3.1/31_b.py) | [✅](./tests/3.1/test_31_b.py) |
| C. [News announcement](./problems/english/3.1/problem_31_c_en.md) | [✅](./solutions/3.1/31_c.py) | [✅](./tests/3.1/test_31_c.py) |
| D. [Data cleaning](./problems/english/3.1/problem_31_d_en.md) | [✅](./solutions/3.1/31_d.py) | [✅](./tests/3.1/test_31_d.py) |
| E. [Racecar 4.0](./problems/english/3.1/problem_31_e_en.md) | [✅](./solutions/3.1/31_e.py) | [✅](./tests/3.1/test_31_e.py) |
| F. [Bunny — 6](./problems/english/3.1/problem_31_f_en.md) | [✅](./solutions/3.1/31_f.py) | [✅](./tests/3.1/test_31_f.py) |
| G. [A and B sat on the pipe](./problems/english/3.1/problem_31_g_en.md) | [✅](./solutions/3.1/31_g.py) | [✅](./tests/3.1/test_31_g.py) |
| H. [Bunny — 7](./problems/english/3.1/problem_31_h_en.md) | [✅](./solutions/3.1/31_h.py) | [✅](./tests/3.1/test_31_h.py) |
| I. [No comments](./problems/english/3.1/problem_31_i_en.md) | [✅](./solutions/3.1/31_i.py) | [✅](./tests/3.1/test_31_i.py) |
| J. [Basic frequency analysis](./problems/english/3.1/problem_31_j_en.md) | [✅](./solutions/3.1/31_j.py) | [✅](./tests/3.1/test_31_j.py) |
| K. [Everything will be found](./problems/english/3.1/problem_31_k_en.md) | [✅](./solutions/3.1/31_k.py) | [✅](./tests/3.1/test_31_k.py) |
| L. [Menu](./problems/english/3.1/problem_31_l_en.md) | [✅](./solutions/3.1/31_l.py) | [✅](./tests/3.1/test_31_l.py) |
| M. [Mass exponentiation](./problems/english/3.1/problem_31_m_en.md) | [✅](./solutions/3.1/31_m.py) | [✅](./tests/3.1/test_31_m.py) |
| N. [Mass exponentiation 3.0](./problems/english/3.1/problem_31_n_en.md) | [✅](./solutions/3.1/31_n.py) | [✅](./tests/3.1/test_31_n.py) |
| O. [GCD 3.0](./problems/english/3.1/problem_31_o_en.md) | [✅](./solutions/3.1/31_o.py) | [✅](./tests/3.1/test_31_o.py) |
| P. [News announcement 3.0](./problems/english/3.1/problem_31_p_en.md) | [✅](./solutions/3.1/31_p.py) | [✅](./tests/3.1/test_31_p.py) |
| Q. [Racecar 5.0](./problems/english/3.1/problem_31_q_en.md) | [✅](./solutions/3.1/31_q.py) | [✅](./tests/3.1/test_31_q.py) |
| R. [RLE](./problems/english/3.1/problem_31_r_en.md) | [✅](./solutions/3.1/31_r.py) | [✅](./tests/3.1/test_31_r.py) |
| S. [Polish calculator](./problems/english/3.1/problem_31_s_en.md) | [✅](./solutions/3.1/31_s.py) | [✅](./tests/3.1/test_31_s.py) |
| T. [Polish calculator — 2](./problems/english/3.1/problem_31_t_en.md) | [✅](./solutions/3.1/31_t.py) | [✅](./tests/3.1/test_31_t.py) |

</details>

<details>
<summary><h3>3.2 Set, dictionary</h3></summary>

- [📖 Theory 3.2](https://education.yandex.ru/handbook/python/article/mnozhestva-slovari) | [🧪 Test Data](./tests/data/test_data_32.py)

| Problems             | Solutions            | Tests                |
|----------------------|----------------------|----------------------|
| А. [Symbolic summary](./problems/english/3.2/problem_32_a_en.md) | [✅](./solutions/3.2/32_a.py) | [✅](./tests/3.2/test_32_a.py) |
| B. [Symbolic difference](./problems/english/3.2/problem_32_b_en.md) | [✅](./solutions/3.2/32_b.py) | [✅](./tests/3.2/test_32_b.py) |
| C. [Bunny — 8](./problems/english/3.2/problem_32_c_en.md) | [✅](./solutions/3.2/32_c.py) | [✅](./tests/3.2/test_32_c.py) |
| D. [Porridge eaters](./problems/english/3.2/problem_32_d_en.md) | [✅](./solutions/3.2/32_d.py) | [✅](./tests/3.2/test_32_d.py) |
| E. [Porridge eaters — 2](./problems/english/3.2/problem_32_e_en.md) | [✅](./solutions/3.2/32_e.py) | [✅](./tests/3.2/test_32_e.py) |
| F. [Porridge eaters — 3](./problems/english/3.2/problem_32_f_en.md) | [✅](./solutions/3.2/32_f.py) | [✅](./tests/3.2/test_32_f.py) |
| G. [Morse code](./problems/english/3.2/problem_32_g_en.md) | [✅](./solutions/3.2/32_g.py) | [✅](./tests/3.2/test_32_g.py) |
| H. [Porridge eaters — 4](./problems/english/3.2/problem_32_h_en.md) | [✅](./solutions/3.2/32_h.py) | [✅](./tests/3.2/test_32_h.py) |
| I. [Bunny — 9](./problems/english/3.2/problem_32_i_en.md) | [✅](./solutions/3.2/32_i.py) | [✅](./tests/3.2/test_32_i.py) |
| J. [Transliteration](./problems/english/3.2/problem_32_j_en.md) | [✅](./solutions/3.2/32_j.py) | [✅](./tests/3.2/test_32_j.py) |
| K. [Namesakes](./problems/english/3.2/problem_32_k_en.md) | [✅](./solutions/3.2/32_k.py) | [✅](./tests/3.2/test_32_k.py) |
| L. [Namesakes — 2](./problems/english/3.2/problem_32_l_en.md) | [✅](./solutions/3.2/32_l.py) | [✅](./tests/3.2/test_32_l.py) |
| M. [Give me something new!](./problems/english/3.2/problem_32_m_en.md) | [✅](./solutions/3.2/32_m.py) | [✅](./tests/3.2/test_32_m.py) |
| N. [This will be a masterpiece!](./problems/english/3.2/problem_32_n_en.md) | [✅](./solutions/3.2/32_n.py) | [✅](./tests/3.2/test_32_n.py) |
| O. [Binary statistics!](./problems/english/3.2/problem_32_o_en.md) | [✅](./solutions/3.2/32_o.py) | [✅](./tests/3.2/test_32_o.py) |
| P. [Bunny — 10](./problems/english/3.2/problem_32_p_en.md) | [✅](./solutions/3.2/32_p.py) | [✅](./tests/3.2/test_32_p.py) |
| Q. [Friends of friends](./problems/english/3.2/problem_32_q_en.md) | [✅](./solutions/3.2/32_q.py) | [✅](./tests/3.2/test_32_q.py) |
| R. [Treasure map](./problems/english/3.2/problem_32_r_en.md) | [✅](./solutions/3.2/32_r.py) | [✅](./tests/3.2/test_32_r.py) |
| S. [Private property](./problems/english/3.2/problem_32_s_en.md) | [✅](./solutions/3.2/32_s.py) | [✅](./tests/3.2/test_32_s.py) |
| T. [Simple task 4.0](./problems/english/3.2/problem_32_t_en.md) | [✅](./solutions/3.2/32_t.py) | [✅](./tests/3.2/test_32_t.py) |

</details>

<details>
<summary><h3>3.3 List comprehensions. Memory model for Python data types.</h3></summary>

- [📖 Theory 3.3](https://education.yandex.ru/handbook/python/article/spisochnye-vyrazheniya-model-pamyati-dlya-tipov-yazyka-python) | [🧪 Test Data](./tests/data/test_data_33.py)

| Problems             | Solutions            | Tests                |
|----------------------|----------------------|----------------------|
| А. [List of squares](./problems/english/3.3/problem_33_a_en.md) | [✅](./solutions/3.3/33_a.py) | [✅](./tests/3.3/test_33_a.py) |
| B. [Multiplication table 2.0](./problems/english/3.3/problem_33_b_en.md) | [✅](./solutions/3.3/33_b.py) | [✅](./tests/3.3/test_33_b.py) |
| C. [Lengths of all words](./problems/english/3.3/problem_33_c_en.md) | [✅](./solutions/3.3/33_c.py) | [✅](./tests/3.3/test_33_c.py) |
| D. [Set of odd numbers](./problems/english/3.3/problem_33_d_en.md) | [✅](./solutions/3.3/33_d.py) | [✅](./tests/3.3/test_33_d.py) |
| E. [Set of all perfect squares](./problems/english/3.3/problem_33_e_en.md) | [✅](./solutions/3.3/33_e.py) | [✅](./tests/3.3/test_33_e.py) |
| F. [Letter statistics](./problems/english/3.3/problem_33_f_en.md) | [✅](./solutions/3.3/33_f.py) | [✅](./tests/3.3/test_33_f.py) |
| G. [Divisors](./problems/english/3.3/problem_33_g_en.md) | [✅](./solutions/3.3/33_g.py) | [✅](./tests/3.3/test_33_g.py) |
| H. [Abbreviation](./problems/english/3.3/problem_33_h_en.md) | [✅](./solutions/3.3/33_h.py) | [✅](./tests/3.3/test_33_h.py) |
| I. [Conversion to string](./problems/english/3.3/problem_33_i_en.md) | [✅](./solutions/3.3/33_i.py) | [✅](./tests/3.3/test_33_i.py) |
| J. [RLE reversed](./problems/english/3.3/problem_33_j_en.md) | [✅](./solutions/3.3/33_j.py) | [✅](./tests/3.3/test_33_j.py) |

</details>

<details>
<summary><h3>3.4 Built-in capabilities for working with collections</h3></summary>

- [📖 Theory 3.4](https://education.yandex.ru/handbook/python/article/vstroennye-vozmozhnosti-po-rabote-s-kollekciyami) | [🧪 Test Data](./tests/data/test_data_34.py)

| Problems             | Solutions            | Tests                |
|----------------------|----------------------|----------------------|
| А. [List automation](./problems/english/3.4/problem_34_a_en.md) | [✅](./solutions/3.4/34_a.py) | [✅](./tests/3.4/test_34_a.py) |
| B. [Gathering for a walk](./problems/english/3.4/problem_34_b_en.md) | [✅](./solutions/3.4/34_b.py) | [✅](./tests/3.4/test_34_b.py) |
| C. [Rational counting](./problems/english/3.4/problem_34_c_en.md) | [✅](./solutions/3.4/34_c.py) | [✅](./tests/3.4/test_34_c.py) |
| D. [Dictionary tree](./problems/english/3.4/problem_34_d_en.md) | [✅](./solutions/3.4/34_d.py) | [✅](./tests/3.4/test_34_d.py) |
| E. [Shopping list](./problems/english/3.4/problem_34_e_en.md) | [✅](./solutions/3.4/34_e.py) | [✅](./tests/3.4/test_34_e.py) |
| F. [Deck of cards](./problems/english/3.4/problem_34_f_en.md) | [✅](./solutions/3.4/34_f.py) | [✅](./tests/3.4/test_34_f.py) |
| G. [Game grid](./problems/english/3.4/problem_34_g_en.md) | [✅](./solutions/3.4/34_g.py) | [✅](./tests/3.4/test_34_g.py) |
| H. [Menu 2.0](./problems/english/3.4/problem_34_h_en.md) | [✅](./solutions/3.4/34_h.py) | [✅](./tests/3.4/test_34_h.py) |
| I. [Multiplication table 3.0](./problems/english/3.4/problem_34_i_en.md) | [✅](./solutions/3.4/34_i.py) | [✅](./tests/3.4/test_34_i.py) |
| J. [We divided the orange 2.0](./problems/english/3.4/problem_34_j_en.md) | [✅](./solutions/3.4/34_j.py) | [✅](./tests/3.4/test_34_j.py) |
| K. [Numerical rectangle 3.0](./problems/english/3.4/problem_34_k_en.md) | [✅](./solutions/3.4/34_k.py) | [✅](./tests/3.4/test_34_k.py) |
| L. [Shopping list 2.0](./problems/english/3.4/problem_34_l_en.md) | [✅](./solutions/3.4/34_l.py) | [✅](./tests/3.4/test_34_l.py) |
| M. [Athletes arrangement](./problems/english/3.4/problem_34_m_en.md) | [✅](./solutions/3.4/34_m.py) | [✅](./tests/3.4/test_34_m.py) |
| N. [Sports divination](./problems/english/3.4/problem_34_n_en.md) | [✅](./solutions/3.4/34_n.py) | [✅](./tests/3.4/test_34_n.py) |
| O. [Shopping list 3.0](./problems/english/3.4/problem_34_o_en.md) | [✅](./solutions/3.4/34_o.py) | [✅](./tests/3.4/test_34_o.py) |
| P. [The layout is as follows...](./problems/english/3.4/problem_34_p_en.md) | [✅](./solutions/3.4/34_p.py) | [✅](./tests/3.4/test_34_p.py) |
| Q. [Are there any other options?](./problems/english/3.4/problem_34_q_en.md) | [✅](./solutions/3.4/34_q.py) | [✅](./tests/3.4/test_34_q.py) |
| R. [Truth table](./problems/english/3.4/problem_34_r_en.md) | [✅](./solutions/3.4/34_r.py) | [✅](./tests/3.4/test_34_r.py) |
| S. [Truth table 2](./problems/english/3.4/problem_34_s_en.md) | [✅](./solutions/3.4/34_s.py) | [✅](./tests/3.4/test_34_s.py) |
| T. [Truth table 3](./problems/english/3.4/problem_34_t_en.md) | [✅](./solutions/3.4/34_t.py) | [✅](./tests/3.4/test_34_t.py) |

</details>

<details>
<summary><h3>3.5 Stream input/output. Working with text files. JSON</h3></summary>

- [📖 Theory 3.5](https://education.yandex.ru/handbook/python/article/potokovyj-vvodvyvod-rabota-s-tekstovymi-fajlami-json) | [🧪 Test Data](./tests/data/test_data_35.py)

| Problems             | Solutions            | Tests                |
|----------------------|----------------------|----------------------|
| А. [A+B+...](./problems/english/3.5/problem_35_a_en.md) | [✅](./solutions/3.5/35_a.py) | [✅](./tests/3.5/test_35_a.py) |
| B. [Average height](./problems/english/3.5/problem_35_b_en.md) | [✅](./solutions/3.5/35_b.py) | [✅](./tests/3.5/test_35_b.py) |
| C. [No comments 2.0](./problems/english/3.5/problem_35_c_en.md) | [✅](./solutions/3.5/35_c.py) | [✅](./tests/3.5/test_35_c.py) |
| D. [Everything will be found 2.0](./problems/english/3.5/problem_35_d_en.md) | [✅](./solutions/3.5/35_d.py) | [✅](./tests/3.5/test_35_d.py) |
| E. [Racecar 6.0](./problems/english/3.5/problem_35_e_en.md) | [✅](./solutions/3.5/35_e.py) | [✅](./tests/3.5/test_35_e.py) |
| F. [Transliteration 2.0](./problems/english/3.5/problem_35_f_en.md) | [✅](./solutions/3.5/35_f.py) | [✅](./tests/3.5/test_35_f.py) |
| G. [File statistics](./problems/english/3.5/problem_35_g_en.md) | [✅](./solutions/3.5/35_g.py) | [✅](./tests/3.5/test_35_g.py) |
| H. [File difference](./problems/english/3.5/problem_35_h_en.md) | [✅](./solutions/3.5/35_h.py) | [✅](./tests/3.5/test_35_h.py) |
| I. [File cleaning](./problems/english/3.5/problem_35_i_en.md) | [✅](./solutions/3.5/35_i.py) | [✅](./tests/3.5/test_35_i.py) |
| J. [Tail](./problems/english/3.5/problem_35_j_en.md) | [✅](./solutions/3.5/35_j.py) | [✅](./tests/3.5/test_35_j.py) |
| K. [File statistics 2.0](./problems/english/3.5/problem_35_k_en.md) | [✅](./solutions/3.5/35_k.py) | [✅](./tests/3.5/test_35_k.py) |
| L. [Divide and conquer](./problems/english/3.5/problem_35_l_en.md) | [✅](./solutions/3.5/35_l.py) | [✅](./tests/3.5/test_35_l.py) |
| M. [Data update](./problems/english/3.5/problem_35_m_en.md) | [✅](./solutions/3.5/35_m.py) | [✅](./tests/3.5/test_35_m.py) |
| N. [Data merging](./problems/english/3.5/problem_35_n_en.md) | [✅](./solutions/3.5/35_n.py) | [✅](./tests/3.5/test_35_n.py) |
| O. [Put yourself in my shoes](./problems/english/3.5/problem_35_o_en.md) | [✅](./solutions/3.5/35_o.py) | [✅](./tests/3.5/test_35_o.py) |
| P. [Everything will be found 3.0](./problems/english/3.5/problem_35_p_en.md) | [✅](./solutions/3.5/35_p.py) | [✅](./tests/3.5/test_35_p.py) |
| Q. [Hide and seek](./problems/english/3.5/problem_35_q_en.md) | [✅](./solutions/3.5/35_q.py) | [✅](./tests/3.5/test_35_q.py) |
| R. [How much does it weigh in bytes?](./problems/english/3.5/problem_35_r_en.md) | [✅](./solutions/3.5/35_r.py) | [✅](./tests/3.5/test_35_r.py) |
| S. [This will be our secret](./problems/english/3.5/problem_35_s_en.md) | [✅](./solutions/3.5/35_s.py) | [✅](./tests/3.5/test_35_s.py) |
| T. [File sum](./problems/english/3.5/problem_35_t_en.md) | [✅](./solutions/3.5/35_t.py) | [✅](./tests/3.5/test_35_t.py) |

</details>

<details>
<summary><h3>4.1 Functions. Scopes. Passing parameters to functions.</h3></summary>

- [📖 Theory 4.1](https://education.yandex.ru/handbook/python/article/funkcii-oblasti-vidimosti-peredacha-parametrov-v-funkcii) | [🧪 Test Data](./tests/data/test_data_41.py)

| Problems             | Solutions            | Tests                |
|----------------------|----------------------|----------------------|
| А. [Functional greeting](./problems/english/4.1/problem_41_a_en.md) | [✅](./solutions/4.1/41_a.py) | [✅](./tests/4.1/test_41_a.py) |
| B. [Functional GCD](./problems/english/4.1/problem_41_b_en.md) | [✅](./solutions/4.1/41_b.py) | [✅](./tests/4.1/test_41_b.py) |
| C. [Length of number](./problems/english/4.1/problem_41_c_en.md) | [✅](./solutions/4.1/41_c.py) | [✅](./tests/4.1/test_41_c.py) |
| D. [Name of the month](./problems/english/4.1/problem_41_d_en.md) | [✅](./solutions/4.1/41_d.py) | [✅](./tests/4.1/test_41_d.py) |
| E. [Numerical string](./problems/english/4.1/problem_41_e_en.md) | [✅](./solutions/4.1/41_e.py) | [✅](./tests/4.1/test_41_e.py) |
| F. [Output system modernization](./problems/english/4.1/problem_41_f_en.md) | [✅](./solutions/4.1/41_f.py) | [✅](./tests/4.1/test_41_f.py) |
| G. [Chess 'lunch'](./problems/english/4.1/problem_41_g_en.md) | [✅](./solutions/4.1/41_g.py) | [✅](./tests/4.1/test_41_g.py) |
| H. [Racecar 7.0](./problems/english/4.1/problem_41_h_en.md) | [✅](./solutions/4.1/41_h.py) | [✅](./tests/4.1/test_41_h.py) |
| I. [Simple task 5.0](./problems/english/4.1/problem_41_i_en.md) | [✅](./solutions/4.1/41_i.py) | [✅](./tests/4.1/test_41_i.py) |
| J. [Merge](./problems/english/4.1/problem_41_j_en.md) | [✅](./solutions/4.1/41_j.py) | [✅](./tests/4.1/test_41_j.py) |

</details>

<details>
<summary><h3>4.2 Positional and keyword arguments. Higher-order functions...</h3></summary>

- [📖 Theory 4.2](https://education.yandex.ru/handbook/python/article/pozicionnye-i-imenovannye-argumenty-funkcii-vysshih-poryadkov-lyambda-funkcii) | [🧪 Test Data](./tests/data/test_data_42.py)

| Problems             | Solutions            | Tests                |
|----------------------|----------------------|----------------------|
| А. [List generator](./problems/english/4.2/problem_42_a_en.md) | [✅](./solutions/4.2/42_a.py) | [✅](./tests/4.2/test_42_a.py) |
| B. [Matrix generator](./problems/english/4.2/problem_42_b_en.md) | [✅](./solutions/4.2/42_b.py) | [✅](./tests/4.2/test_42_b.py) |
| C. [Functional GCD 2.0](./problems/english/4.2/problem_42_c_en.md) | [✅](./solutions/4.2/42_c.py) | [✅](./tests/4.2/test_42_c.py) |
| D. [Name of the month 2.0](./problems/english/4.2/problem_42_d_en.md) | [✅](./solutions/4.2/42_d.py) | [✅](./tests/4.2/test_42_d.py) |
| E. [Data preparation](./problems/english/4.2/problem_42_e_en.md) | [✅](./solutions/4.2/42_e.py) | [✅](./tests/4.2/test_42_e.py) |
| F. [Coffee shop](./problems/english/4.2/problem_42_f_en.md) | [✅](./solutions/4.2/42_f.py) | [✅](./tests/4.2/test_42_f.py) |
| G. [On air — 'Experiments' section](./problems/english/4.2/problem_42_g_en.md) | [✅](./solutions/4.2/42_g.py) | [✅](./tests/4.2/test_42_g.py) |
| H. [Long sorting](./problems/english/4.2/problem_42_h_en.md) | [✅](./solutions/4.2/42_h.py) | [✅](./tests/4.2/test_42_h.py) |
| I. [Even filtering](./problems/english/4.2/problem_42_i_en.md) | [✅](./solutions/4.2/42_i.py) | [✅](./tests/4.2/test_42_i.py) |
| J. [Key secret](./problems/english/4.2/problem_42_j_en.md) | [✅](./solutions/4.2/42_j.py) | [✅](./tests/4.2/test_42_j.py) |

</details>

<details>
<summary><h3>4.3. Recursion. Decorators. Generators.</h3></summary>

- [📖 Theory 4.3](https://education.yandex.ru/handbook/python/article/rekursiya-dekoratory-generatory) | [🧪 Test Data](./tests/data/test_data_43.py)

| Problems             | Solutions            | Tests                |
|----------------------|----------------------|----------------------|
| А. [Recursive summator](./problems/english/4.3/problem_43_a_en.md) | [✅](./solutions/4.3/43_a.py) | [✅](./tests/4.3/test_43_a.py) |
| B. [Recursive digit adder](./problems/english/4.3/problem_43_b_en.md) | [✅](./solutions/4.3/43_b.py) | [✅](./tests/4.3/test_43_b.py) |
| C. [Polynomial of N degree](./problems/english/4.3/problem_43_c_en.md) | [✅](./solutions/4.3/43_c.py) | [✅](./tests/4.3/test_43_c.py) |
| D. [Result decoration](./problems/english/4.3/problem_43_d_en.md) | [✅](./solutions/4.3/43_d.py) | [✅](./tests/4.3/test_43_d.py) |
| E. [Result accumulation](./problems/english/4.3/problem_43_e_en.md) | [✅](./solutions/4.3/43_e.py) | [✅](./tests/4.3/test_43_e.py) |
| F. [Merge sort](./problems/english/4.3/problem_43_f_en.md) | [✅](./solutions/4.3/43_f.py) | [✅](./tests/4.3/test_43_f.py) |
| G. [Uniformity is not a flaw](./problems/english/4.3/problem_43_g_en.md) | [✅](./solutions/4.3/43_g.py) | [✅](./tests/4.3/test_43_g.py) |
| H. [Fibonacci generator](./problems/english/4.3/problem_43_h_en.md) | [✅](./solutions/4.3/43_h.py) | [✅](./tests/4.3/test_43_h.py) |
| I. [Cyclic generator](./problems/english/4.3/problem_43_i_en.md) | [✅](./solutions/4.3/43_i.py) | [✅](./tests/4.3/test_43_i.py) |
| J. ["Straightening" the list](./problems/english/4.3/problem_43_j_en.md) | [✅](./solutions/4.3/43_j.py) | [✅](./tests/4.3/test_43_j.py) |

</details>

<details>
<summary><h3>5.1 Python object model. Classes, fields, and methods.</h3></summary>

- [📖 Theory 5.1](https://education.yandex.ru/handbook/python/article/obuektnaya-model-python-klassy-polya-i-metody) | [🧪 Test Data](./tests/data/test_data_51.py)

| Problems             | Solutions            | Tests                |
|----------------------|----------------------|----------------------|
| А. [Cool point](./problems/english/5.1/problem_51_a_en.md) | [✅](./solutions/5.1/51_a.py) | [✅](./tests/5.1/test_51_a.py) |
| B. [Cool point 2.0](./problems/english/5.1/problem_51_b_en.md) | [✅](./solutions/5.1/51_b.py) | [✅](./tests/5.1/test_51_b.py) |
| C. [Don't press the red button!](./problems/english/5.1/problem_51_c_en.md) | [✅](./solutions/5.1/51_c.py) | [✅](./tests/5.1/test_51_c.py) |
| D. [Work is not a wolf](./problems/english/5.1/problem_51_d_en.md) | [✅](./solutions/5.1/51_d.py) | [✅](./tests/5.1/test_51_d.py) |
| E. [Cool rectangle](./problems/english/5.1/problem_51_e_en.md) | [✅](./solutions/5.1/51_e.py) | [✅](./tests/5.1/test_51_e.py) |
| F. [Cool rectangle 2.0](./problems/english/5.1/problem_51_f_en.md) | [✅](./solutions/5.1/51_f.py) | [✅](./tests/5.1/test_51_f.py) |
| G. [Cool rectangle 3.0](./problems/english/5.1/problem_51_g_en.md) | [✅](./solutions/5.1/51_g.py) | [✅](./tests/5.1/test_51_g.py) |
| H. [Checkers](./problems/english/5.1/problem_51_h_en.md) | [✅](./solutions/5.1/51_h.py) | [✅](./tests/5.1/test_51_h.py) |
| I. [Queue](./problems/english/5.1/problem_51_i_en.md) | [✅](./solutions/5.1/51_i.py) | [✅](./tests/5.1/test_51_i.py) |
| J. [Stack](./problems/english/5.1/problem_51_j_en.md) | [✅](./solutions/5.1/51_j.py) | [✅](./tests/5.1/test_51_j.py) |

</details>

<details>
<summary><h3>5.2 Magic methods, method overriding. Inheritance.</h3></summary>

- [📖 Theory 5.2](https://education.yandex.ru/handbook/python/article/volshebnye-metody-pereopredelenie-metodov-nasledovanie) | [🧪 Test Data](./tests/data/test_data_52.py)

| Problems             | Solutions            | Tests                |
|----------------------|----------------------|----------------------|
| А. [Cool point 3.0](./problems/english/5.2/problem_52_a_en.md) | [✅](./solutions/5.2/52_a.py) | [✅](./tests/5.2/test_52_a.py) |
| B. [Cool point 4.0](./problems/english/5.2/problem_52_b_en.md) | [✅](./solutions/5.2/52_b.py) | [✅](./tests/5.2/test_52_b.py) |
| C. [Cool point 5.0](./problems/english/5.2/problem_52_c_en.md) | [✅](./solutions/5.2/52_c.py) | [✅](./tests/5.2/test_52_c.py) |
| D. [Fractions v0.1](./problems/english/5.2/problem_52_d_en.md) | [✅](./solutions/5.2/52_d.py) | [✅](./tests/5.2/test_52_d.py) |
| E. [Fractions v0.2](./problems/english/5.2/problem_52_e_en.md) | [✅](./solutions/5.2/52_e.py) | [✅](./tests/5.2/test_52_e.py) |
| F. [Fractions v0.3](./problems/english/5.2/problem_52_f_en.md) | [✅](./solutions/5.2/52_f.py) | [✅](./tests/5.2/test_52_f.py) |
| G. [Fractions v0.4](./problems/english/5.2/problem_52_g_en.md) | [✅](./solutions/5.2/52_g.py) | [✅](./tests/5.2/test_52_g.py) |
| H. [Fractions v0.5](./problems/english/5.2/problem_52_h_en.md) | [✅](./solutions/5.2/52_h.py) | [✅](./tests/5.2/test_52_h.py) |
| I. [Fractions v0.6](./problems/english/5.2/problem_52_i_en.md) | [✅](./solutions/5.2/52_i.py) | [✅](./tests/5.2/test_52_i.py) |
| J. [Fractions v0.7](./problems/english/5.2/problem_52_j_en.md) | [✅](./solutions/5.2/52_j.py) | [✅](./tests/5.2/test_52_j.py) |

</details>

<details>
<summary><h3>5.3 Python exception model. Try, except, else, finally.</h3></summary>

- [📖 Theory 5.3](https://education.yandex.ru/handbook/python/article/model-isklyuchenij-python-try-except-else-finally-moduli) | [🧪 Test Data](./tests/data/test_data_53.py)

| Problems             | Solutions            | Tests                |
|----------------------|----------------------|----------------------|
| А. [Error handling](./problems/english/5.3/problem_53_a_en.md) | [✅](./solutions/5.3/53_a.py) | [✅](./tests/5.3/test_53_a.py) |
| B. [Breaking is not building](./problems/english/5.3/problem_53_b_en.md) | [✅](./solutions/5.3/53_b.py) | [✅](./tests/5.3/test_53_b.py) |
| C. [Breaking is not building 2](./problems/english/5.3/problem_53_c_en.md) | [✅](./solutions/5.3/53_c.py) | [✅](./tests/5.3/test_53_c.py) |
| D. [Parameter control](./problems/english/5.3/problem_53_d_en.md) | [✅](./solutions/5.3/53_d.py) | [✅](./tests/5.3/test_53_d.py) |
| E. [Merge with check](./problems/english/5.3/problem_53_e_en.md) | [✅](./solutions/5.3/53_e.py) | [✅](./tests/5.3/test_53_e.py) |
| F. [Root of evil 2](./problems/english/5.3/problem_53_f_en.md) | [✅](./solutions/5.3/53_f.py) | [✅](./tests/5.3/test_53_f.py) |
| G. [Name validation](./problems/english/5.3/problem_53_g_en.md) | [✅](./solutions/5.3/53_g.py) | [✅](./tests/5.3/test_53_g.py) |
| H. [Username validation](./problems/english/5.3/problem_53_h_en.md) | [✅](./solutions/5.3/53_h.py) | [✅](./tests/5.3/test_53_h.py) |
| I. [User validation](./problems/english/5.3/problem_53_i_en.md) | [✅](./solutions/5.3/53_i.py) | [✅](./tests/5.3/test_53_i.py) |
| J. [Password validation](./problems/english/5.3/problem_53_j_en.md) | [✅](./solutions/5.3/53_j.py) | [✅](./tests/5.3/test_53_j.py) |

</details>

<details>
<summary><h3>6.1 The <b>math</b> and <b>numpy</b> modules.</h3></summary>

- [📖 Theory 6.1](https://education.yandex.ru/handbook/python/article/moduli-math-i-numpy) | [🧪 Test Data](./tests/data/test_data_61.py)

| Problems             | Solutions            | Tests                |
|----------------------|----------------------|----------------------|
| А. [Mathematics is cool, but that's not certain.](./problems/english/6.1/problem_61_a_en.md) | [✅](./solutions/6.1/61_a.py) | [✅](./tests/6.1/test_61_a.py) |
| B. [Stream GCD](./problems/english/6.1/problem_61_b_en.md) | [✅](./solutions/6.1/61_b.py) | [✅](./tests/6.1/test_61_b.py) |
| C. [Any other options?](./problems/english/6.1/problem_61_c_en.md) | [✅](./solutions/6.1/61_c.py) | [✅](./tests/6.1/test_61_c.py) |
| D. [Non-arithmetic mean](./problems/english/6.1/problem_61_d_en.md) | [✅](./solutions/6.1/61_d.py) | [✅](./tests/6.1/test_61_d.py) |
| E. [Step towards](./problems/english/6.1/problem_61_e_en.md) | [✅](./solutions/6.1/61_e.py) | [✅](./tests/6.1/test_61_e.py) |
| F. [Multiplication matrix](./problems/english/6.1/problem_61_f_en.md) | [✅](./solutions/6.1/61_f.py) | [✅](./tests/6.1/test_61_f.py) |
| G. [Chess preparation](./problems/english/6.1/problem_61_g_en.md) | [✅](./solutions/6.1/61_g.py) | [✅](./tests/6.1/test_61_g.py) |
| H. [Numerical snake 3.0](./problems/english/6.1/problem_61_h_en.md) | [✅](./solutions/6.1/61_h.py) | [✅](./tests/6.1/test_61_h.py) |
| I. [Rotation](./problems/english/6.1/problem_61_i_en.md) | [✅](./solutions/6.1/61_i.py) | [✅](./tests/6.1/test_61_i.py) |
| J. [Ladder](./problems/english/6.1/problem_61_j_en.md) | [✅](./solutions/6.1/61_j.py) | [✅](./tests/6.1/test_61_j.py) |

</details>

<details>
<summary><h3>6.2 The <b>pandas</b> module.</h3></summary>

- [📖 Theory 6.2](https://education.yandex.ru/handbook/python/article/modul-pandas) | [🧪 Test Data](./tests/data/test_data_62.py)

| Problems             | Solutions            | Tests                |
|----------------------|----------------------|----------------------|
| А. [Lengths of all words - 2](./problems/english/6.2/problem_62_a_en.md) | [✅](./solutions/6.2/62_a.py) | [✅](./tests/6.2/test_62_a.py) |
| B. [Lengths of all words by parity](./problems/english/6.2/problem_62_b_en.md) | [✅](./solutions/6.2/62_b.py) | [✅](./tests/6.2/test_62_b.py) |
| C. [Check - 2](./problems/english/6.2/problem_62_c_en.md) | [✅](./solutions/6.2/62_c.py) | [✅](./tests/6.2/test_62_c.py) |
| D. [Sale](./problems/english/6.2/problem_62_d_en.md) | [✅](./solutions/6.2/62_d.py) | [✅](./tests/6.2/test_62_d.py) |
| E. [Long words](./problems/english/6.2/problem_62_e_en.md) | [✅](./solutions/6.2/62_e.py) | [✅](./tests/6.2/test_62_e.py) |
| F. [Progress report](./problems/english/6.2/problem_62_f_en.md) | [✅](./solutions/6.2/62_f.py) | [✅](./tests/6.2/test_62_f.py) |
| G. [Failure report](./problems/english/6.2/problem_62_g_en.md) | [✅](./solutions/6.2/62_g.py) | [✅](./tests/6.2/test_62_g.py) |
| H. [Journal update](./problems/english/6.2/problem_62_h_en.md) | [✅](./solutions/6.2/62_h.py) | [✅](./tests/6.2/test_62_h.py) |
| I. [Endless battleship](./problems/english/6.2/problem_62_i_en.md) | [✅](./solutions/6.2/62_i.py) | [✅](./tests/6.2/test_62_i.py) |
| J. [Function extremum](./problems/english/6.2/problem_62_j_en.md) | [✅](./solutions/6.2/62_j.py) | [✅](./tests/6.2/test_62_j.py) |

</details>

<details>
<summary><h3>6.3 The <b>requests</b> module.</h3></summary>

- [📖 Theory 6.3](https://education.yandex.ru/handbook/python/article/modul-requests) | [🧪 Test Data](./tests/data/test_data_63.py)

| Problems             | Solutions            | Tests                |
|----------------------|----------------------|----------------------|
| А. [System check](./problems/english/6.3/problem_63_a_en.md) | [✅](./solutions/6.3/63_a.py) | [✅](./tests/6.3/test_63_a.py) |
| B. [Summing answers](./problems/english/6.3/problem_63_b_en.md) | [✅](./solutions/6.3/63_b.py) | [✅](./tests/6.3/test_63_b.py) |
| C. [Summing answers 2](./problems/english/6.3/problem_63_c_en.md) | [✅](./solutions/6.3/63_c.py) | [✅](./tests/6.3/test_63_c.py) |
| D. [Specific value](./problems/english/6.3/problem_63_d_en.md) | [✅](./solutions/6.3/63_d.py) | [✅](./tests/6.3/test_63_d.py) |
| E. [Summing answers 3](./problems/english/6.3/problem_63_e_en.md) | [✅](./solutions/6.3/63_e.py) | [✅](./tests/6.3/test_63_e.py) |
| F. [User list](./problems/english/6.3/problem_63_f_en.md) | [✅](./solutions/6.3/63_f.py) | [✅](./tests/6.3/test_63_f.py) |
| G. [Message mailing](./problems/english/6.3/problem_63_g_en.md) | [✅](./solutions/6.3/63_g.py) | [✅](./tests/6.3/test_63_g.py) |
| H. [New user registration](./problems/english/6.3/problem_63_h_en.md) | [✅](./solutions/6.3/63_h.py) | [✅](./tests/6.3/test_63_h.py) |
| I. [Data modification](./problems/english/6.3/problem_63_i_en.md) | [✅](./solutions/6.3/63_i.py) | [✅](./tests/6.3/test_63_i.py) |
| J. [Data deletion](./problems/english/6.3/problem_63_j_en.md) | [✅](./solutions/6.3/63_j.py) | [✅](./tests/6.3/test_63_j.py) |

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
