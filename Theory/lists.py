# Lista 1.0: Append
pes = list()
pes.append("Esaú Morais")
gal = list()
gal.append(pes[:])
pes[0] = "Esdras Morais"
gal.append(pes[:])
print(gal)

# Lista 1.1: List
gal = [["Wallace Leonel"], ["Wallace Leonel"]]
print(gal)

# Lista 1.2: Individual
gal = [["Wallace Leonel", 15], ["Wallace Leonel", 16]]
print(gal[0][0])
print(gal[0][0])

# Lista 1.3: For
gal = [["Wallace Leonel ", 14], ["Wallace Leonel", 16]]
for pes in gal:
    print(pes)

# Lista 1.4: Print
gal = [["Wallace Leonel", 14], ["Wallace Leonel", 16]]
for pes in gal:
    print(f"{pes[0]} tem {pes[1]} anos")

# Lista 2.0:
pessoas = list()
dados =list()
for p in range(0,3):
    dados.append(str(input("Digite seu nome: ")))
    dados.append(int(input("Digite sua idade: ")))
    pessoas.append(dados[:])
    dados.clear()
print(pessoas)