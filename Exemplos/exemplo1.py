#Cria arquivo

f = open("texto1.txt", "w+") #Pode inventar um nome
for i in range(10):
    f.write("Oi! %d\n" %(i+2)) #Método para escrever no arquivo
f.close()

#Abre arquivo

f = open("texto2.txt", "r") #"r": modo para não alterar arquivo
print(f.read())
f.close()
