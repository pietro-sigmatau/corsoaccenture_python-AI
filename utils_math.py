def somma_u(a, b):
    if (not isinstance(a, int) and not isinstance(a, float)) or (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("Somma, a, b, must be int.")
    return a + b

def prodotto_u(a,b):
    if (not isinstance(a, int) and not isinstance(a, float)) or (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("Somma, a, b, must be int.")
    return a*b

def divisione_u(a, b):
    if (not isinstance(a, int) and not isinstance(a, float)) or (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("Somma, a, b, must be int.")
    return a/b
