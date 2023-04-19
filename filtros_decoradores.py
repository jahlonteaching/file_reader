
def mayuscula_a_minuscula(func):
    def wrapper(*args, **kwargs):
        c: str = func(*args, **kwargs)
        if c.isupper():
            c = c.lower()
        return c
    return wrapper


def espacio_a_guion(func):
    def wrapper(*args, **kwargs):
        c: str = func(*args, **kwargs)
        if c == ' ':
            c = "_"
        return c
    return wrapper


def parentesis_a_corchetes(func):
    def wrapper(*args, **kwargs):
        c: str = func(*args, **kwargs)
        if c == '(':
            c = '['
        if c == ')':
            c = ']'
        return c
    return wrapper

