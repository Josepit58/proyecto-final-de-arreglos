import sys
import pandas as pd
import matplotlib.pyplot as plt
import statistics

lista = []
names = []
esps = []
mates = []
comps = []
ings = []
promedio = 0
acumulador = 0

for i in range (2):
    print ("cual es su nombre?")
    name = input()
    names.append(name)

    print ("dame tu calificacion de español")
    esp = float(input())
    esps.append(esp)

    print ("dame tu calificacion de matematicas")
    mate = float(input())
    mates.append(mate)

    print ("dame tu calificacion de computacion")
    comp = float(input())
    comps.append(comp)

    print ("dame tu calificacion de ingles")
    ing = float(input())
    ings.append(ing)

    promedio = (esp + mate + comp + ing) / 4
    lista.append(promedio)

promedioE = statistics.mean(esps)
promedioM = statistics.mean(mates)
promedioC = statistics.mean(comps)
promedioEn = statistics.mean(ings)
promedioG = statistics.mean(lista)

ValorMayor = max(lista)
indice = lista.index(ValorMayor)
MejorAlumno = names[indice]
print("El mejor alumno es", MejorAlumno)

print ("promedio de español es de: ", promedioE)
print ("promedio de matematicas es de: ", promedioM)
print ("promedio de computacion es de: ", promedioC)
print ("promedio de ingles es de: ", promedioEn)

print ("el promedio del grupo es de: ",promedioG)

if promedio <= 5:
    acumulador = acumulador + 1

    print ("la cantidad de reprobados es de: ",acumulador)

df = pd.DataFrame({'1stcolumn':[100,200], '2ndcolumn':[10,20]})

graficaE = pd.DataFrame(esps)
graficaM = pd.DataFrame(mates)
graficaC = pd.DataFrame(comps)
graficaI = pd.DataFrame(ings)
graficaP = pd.DataFrame(lista)

print("graficas de español")
plt.bar(df["nombre", df["español"]])
plt.rcParams["figure.figsize"] = (10,10)
plt.show()
print("grafica de matematicas")
print(graficaM)
print("graficas de computacion")
print(graficaC)
print("graficas de ingles")
print(graficaI)

print("grafica de promedio genral de cada alumno")
print(graficaP)

