#Aritmeticos
a=10 
b=3

soma = a + b # Soma (+): soma dois valores
subtracao = a - b  #Subtração (-): subtrai o segundo valor do primeiro
multiplicacao = a * b # Multiplicação (*): multiplica dois valores
divisao = a / b # Divisão (/): divide o primeiro valor pelo segundo e devolve um resultado de tipo flutuante
divisao_inteira = a // b # Divisão inteira (//): divide o primeiro valor pelo segundo e devolve um resultado de tipo inteiro (a parte decimal é descartada).
modulo = a % b # Módulo (%): devolve o resto da divisão entre o primeiro valor e o segundo
exponeciacao = a ** b # Exponenciação (**): eleva o primeiro valor à potência do segundo

print(f"\nsoma {soma}")
print(f"subtracao{subtracao}")
print(f"multiplicacao{multiplicacao}")
print(f"divisao{divisao}")  
print(f"divisao_inteira{divisao_inteira}")
print(f"modulo{modulo}")
print(f"exponeciacao{exponeciacao}")

# De comparação
a=10
b=3

igual = a == b #Igual a (==): devolve True se ambos os valores são iguais
diferente = a != b # Diferente de (!=): devolve True se os valores são diferentes
maior = a > b #Maior que (>): devolve True se o primeiro valor é maior que o segundo
menor = a < b # Menor que (<): devolve True se o primeiro valor é menor que o segundo
maior_igual = a >= b # Maior ou igual que (>=): devolve True se o primeiro valor é maior ou igual que o segundo
menor_igual = a <= b # Menor ou igual que (<=): devolve True se o primeiro valor é menor ou igual que o segundo

print(f"\nigual{igual}")
print(f"diferente{diferente}")
print(f"maior{maior}")
print(f"menor{menor}")
print(f"maior_igual{maior_igual}")
print(f"menor_igual{menor_igual}")

#Logicos
a=10
b=3

resultado_and = (a > 5) and (b <5) # AND (and): devolve True se ambas as expressões forem verdadeiras
resultado_or = (a >15) or (b < 5) # OR (or): devolve True se pelo menos uma das expressões for verdadeira
resultado_not = not( a > 5) # NOT (not): inverte o valor lógico da expressão (True vira False e vice-versa)

print(f"\nreultado_ando{resultado_and}")
print(f"resultado_or{resultado_or}")
print(f"resultado_not{resultado_not}")