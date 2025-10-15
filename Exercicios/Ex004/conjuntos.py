print("conjuntos set()")
conjunto1= {1,2,3}
conjunto2 = {3,4,5}

uniao = conjunto1 | conjunto2 # Elementos que estão em qualquer um dos conjuntos
print(uniao)

intersecao = conjunto1 & conjunto2 # Elementos que estão em ambos os conjuntos
print(intersecao)

diferenca = conjunto1 - conjunto2 # Elementos que estão no conjunto1, mas não no conjunto2
print(diferenca)

defernca_simetrica = conjunto1 ^ conjunto2 # Elementos que estão em um ou outro conjunto, mas não em ambos
print (defernca_simetrica)

print("\nMetodos de conjuntos")

frutas = {"maçã", "banana", "laranja"}

frutas.add("pera") # Adiciona um elemento ao conjunto
print(frutas)

frutas.remove("banana")    # Gera erro se o elemento não existir
print(frutas)

frutas.discard("uva")  # Não gera erro se o elemento não existir
print(frutas)

frutas.clear()  # Remove todos os elementos do conjunto
print(frutas)