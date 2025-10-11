frutas = ["maça", "banana", "laranja"]
for fruta in frutas:
        print(fruta)
        # Neste exemplo, o loop for itera sobre a lista frutas. Em cada iteração, a variável fruta assume o valor de um elemento da lista, e o bloco de código dentro do loop é executado. Neste caso, cada fruta é impressa em uma linha separada

print("\ncontador com while partido do 0")
contador = 0
while contador <5:
    print(contador)
    contador += 1
    #   Neste exemplo, o loop while é executado enquanto a variável contador for menor que 5. Em cada iteração, o valor de contador é impresso e depois incrementado em 1 pela instrução contador += 1. O loop será interrompido quando contador atingir o valor de 5, É importante ter cuidado ao usar o loop while, pois, se a condição nunca se tornar falsa, o loop será executado indefinidamente, o que é conhecido como um loop infinito

print("\nGames mais jogados por mim recentemente")
lista_de_jogos =["2xKo", "Overwatch", "League of Legends", "Death Stranding", "Deathloop"] 
for indice, jogo in enumerate(lista_de_jogos) :
    print(f"{indice+1} - {jogo}")
    #Quando usamos for e enumerate juntos precisamos que ambos  permaneçam juntos, ou seja, o for percorre a lista e o enumerate cria os índices.





