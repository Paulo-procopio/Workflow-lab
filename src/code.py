# Funções matemáticas básicas

def somar(a, b):
    """Soma dois números"""
    return a + b

def subtrair(a, b):
    """Subtrai dois números"""
    return a - b

def multiplicar(a, b):
    """Multiplica dois números"""
    return a * b

def dividir(a, b):
    """Divide dois números"""
    if b == 0:
        raise ValueError("Não pode dividir por zero")
    return a / b

# Função principal
if __name__ == "__main__":
    print("Calculadora funcionando!")
    print(f"2 + 3 = {somar(2, 3)}")