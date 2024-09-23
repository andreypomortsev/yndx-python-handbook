def same_type(func):
    def wrapper(*args, **kwargs):
        data_type = type(args[0])
        for data in args[1:]:
            if not isinstance(data, data_type):
                print("Обнаружены различные типы данных")
                return "Fail"
        else:
            return func(*args, **kwargs)

    return wrapper
