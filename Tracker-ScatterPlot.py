import matplotlib.pyplot as plt

entrada = open(input("Route of input file: "), "r")
salida = input("Name of output file (without extension): ")

primeraVez = True
t = []
x = []

for linea in entrada:
    
    if not primeraVez:
    
        t.append(float(linea.split()[0]))
        x.append(float(linea.split()[1]))
        
    entrada.readline()
    primeraVez = False
    
plt.figure(figsize=(10,4))

plt.scatter(t[:150], x[:150])

plt.xlabel("t")
plt.ylabel("y")

plt.savefig(salida + ".png", dpi=1200)
