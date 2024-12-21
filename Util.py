def get_bool(value: str) -> bool:
    if value.lower() == "true":
        return True
    else: return False

def is_int(value: str) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False

def is_bool(value: str) -> bool:
    if value.lower() in ['true', 'false']:
        return True
    return False

def get_int(value: str) -> int:
    try:
        int(value)
        return int(value)
    except ValueError:
        pass
    if value.lower() == "true":
        return 1
    else: return 0

def get_data_type(value: str) -> str:
    try:
        int(value)
        return "i32"
    except ValueError:
        pass  # Если ValueError, это не целое число

    if value.lower() in ['true', 'false']:
        return "bool"

    sys.exit("Error: You are using an unsupported data type")

def comp_result(op1: str, op2: str, comp: str) -> bool:
    # Преобразуем входные строки в соответствующие типы данных
    if op1.lower() == "true":
        op1 = True
    elif op1.lower() == "false":
        op1 = False
    else:
        op1 = int(op1)

    if op2.lower() == "true":
        op2 = True
    elif op2.lower() == "false":
        op2 = False
    else:
        op2 = int(op2)

    # Проверка на совпадение типов данных
    if type(op1) != type(op2):
        raise ValueError("Операнды должны быть одного типа (int или bool)")

    # Выполняем операцию сравнения в зависимости от типа comp
    if comp == "==":
        return op1 == op2
    elif comp == "!=":
        return op1 != op2
    elif comp == "<":
        return op1 < op2
    elif comp == "<=":
        return op1 <= op2
    elif comp == ">":
        return op1 > op2
    elif comp == ">=":
        return op1 >= op2
    else:
        raise ValueError("Некорректная операция сравнения")