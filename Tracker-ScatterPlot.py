import matplotlib.pyplot as plt

entrada = open(input(), "r")

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

plt.xlabel("t(s)")
plt.ylabel("y(m)")

plt.savefig("Bola metal, agua.png", dpi=1200)