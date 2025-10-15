print("\nDicionarios")
pessoa = {"nome": "João", "idade":25, "cidade":"Madri"}
print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["cidade"])


print("\n/Metodos de dicionarios/")
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

pessoa.update({"profissão": "Engenheiro"})
print(pessoa)
#Outros metodos
#keys(): retorna uma visualização de todas as chaves do dicionário.
#values(): retorna uma visualização de todos os valores do dicionário.
#items(): retorna uma visualização de todos os pares chave-valor do dicionário.
#update(outro_dicionario): atualiza o dicionário com os pares chave-valor de outro dicionário

#O metodo values O método .values() te dá uma "lista" de todos os valores (o conteúdo) do seu dicionário.-O que você pede	O que o Python te dá -pessoa.values()	-Todos os valores: ["João", 25, "Madri"]-Para que serve	Útil quando você quer apenas processar os dados em si (como somar todos os números, ou imprimir todos os nomes).

#O metodo keys O método .keys() te dá uma "lista" de todas as chaves (os rótulos) do seu dicionário.-O que você pede	O que o Python te dá -pessoa.keys()	Todas as chaves: ["nome", "idade", "cidade"] -Para que serve	Útil quando você quer saber quais informações estão disponíveis no dicionário.