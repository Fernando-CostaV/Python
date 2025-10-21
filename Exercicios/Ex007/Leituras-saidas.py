arquivo = open ("dados.txt", "r")
conteudo = arquivo.read()
print (conteudo)
arquivo.close()


arquivo= open("arquivo.txt","w") 
arquivo.write("Olá, mundo")
arquivo.close()