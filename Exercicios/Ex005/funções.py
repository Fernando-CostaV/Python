def saudcao():
    print("Olá, mundo !")
saudcao()

def saudacao_nome(nome):
    print(f"Olá, {nome} !")
saudacao_nome("João")
saudacao_nome("Maria")

print("\nValores de retorno")
def soma (a,b):
    return a + b

resultado = soma(3,5)
print(resultado)

print("\nFunções anonimas")
quadrado = lambda x: x ** 2
print(quadrado(5))
#Python permite criar funções anônimas ou funções lambda, que são funções sem nome definidas em uma única linha. São comumente usadas para funções pequenas e concisas.

print("\nVariáveis locais e globais")   
def funcao():
    variavel_local = 10
    print("Variável local:")

variavel_global = 20

def funcao2():
    print("Variável global:")

funcao()
funcao2()
print(variavel_global)
print(variavel_local)   # Gera um erro, a variável não está definida neste escopo.

print("\ndocumentação de funções")
def area_retangulo(base, altura):
    """
    Calcula a área de um retângulo.


    Args:
        base (float): A base do retângulo.
        altura (float): A altura do retângulo.


    Returns:
        float: A área do retângulo.
    """
    return base * altura

print("\nFunções com variavel número de argumentos")
def soma_variavel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


print(soma_variavel(1, 2, 3))  # Imprime 6
print(soma_variavel(4, 5, 6, 7))  # Imprime 22