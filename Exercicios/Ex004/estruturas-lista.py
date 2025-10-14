#Listas
frutas = ["maçã","banana","laranja"]
print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[-1])
print(frutas[-2])
print(frutas[-3])  


print("\nMetodos de listas")
furtas = ["maçã","banana","laranja"]

frutas.append("pera")
print(frutas)

frutas.insert(1,"uva")
print(frutas)

frutas.remove("banana")
print(frutas)

fruta_removida = frutas.pop(2)
print(frutas)
print("fruta_removida")

frutas.sort()
print(frutas)

frutas.reverse()
print(frutas)

print("\nLista de compreensão")
numero = [1,2,3,4,5]
quadrado = [x**2 for x in numero if x%2 == 0]
print(quadrado)