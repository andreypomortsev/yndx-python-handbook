## [Изменение данных](../../../solutions/6.3/63_i.py)

Продолжим работу с сервером из прошлых задач. При _PUT_ запросе по пути _/users/\<id\>_ доступна возможность изменение информации о пользователе. Для этого в данные запроса (`data`) требуется передать _JSON_ объект с новой информацией (без указания идентификатора).

Напишите программу, которая изменяет информацию о пользователе.

### Формат ввода

В первой строке вводится адрес сервера.\
Во второй строке записан идентификатор пользователя, информацию о котором требуется изменить. В следующих строках вводятся данные для изменения в формате: <название поля>=<новое значение>.

### Формат вывода

Ничего выводить не требуется.

### Пример

__Ввод__
```plaintext
# Пользовательский ввод:
127.0.0.1:5000
2
username=ivanov_vasily
email=ivanov_vasily@server.none
# Данные сервера:
[
    {
        "id": 1,
        "username": "first",
        "last_name": "Петрова",
        "first_name": "Елизавета",
        "email": "e.petrova@server.none"
    },
    {
        "id": 2,
        "username": "second",
        "last_name": "Иванов",
        "first_name": "Василий",
        "email": "vas.ivanov@server.none"
    },
    {
        "id": 3,
        "username": "third",
        "last_name": "Иванов",
        "first_name": "Виктор",
        "email": "vik.ivanov@server.none"
    }
]
```

__Вывод__
```plaintext
# Данные сервера:
[
    {
        "id": 1,
        "username": "first",
        "last_name": "Петрова",
        "first_name": "Елизавета",
        "email": "e.petrova@server.none"
    },
    {
        "id": 2,
        "username": "ivanov_vasily",
        "last_name": "Иванов",
        "first_name": "Василий",
        "email": "ivanov_vasily@server.none"
    },
    {
        "id": 3,
        "username": "third",
        "last_name": "Иванов",
        "first_name": "Виктор",
        "email": "vik.ivanov@server.none"
    }
]
```