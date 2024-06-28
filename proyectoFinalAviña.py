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

datos = {'nombres': names,
         'español':esps,
         'matematicas':mates,
         'computacion':comps,
         'ingles':ings,
         'promedio':promedio
        }
datos

df = pd.DataFrame (datos, columns=['nombres','español', 'matematicas', 'computacion', 'ingles'])
df

print("grafica de español")
plt.bar(df['nombres'], df['español'])
plt.rcParams["figure.figsize"] = (10,10)
plt.show()

print("grafica de matematicas")
plt.bar(df['nombres'], df['matematicas'])
plt.rcParams["figure.figsize"] = (10,10)
plt.show()

print("grafica de computacion")
plt.bar(df['nombres'], df['computacion'])
plt.rcParams["figure.figsize"] = (10,10)
plt.show()

print("graficad de ingles")
plt.bar(df['nombres'], df['ingles'])
plt.rcParams["figure.figsize"] = (10,10)
plt.show()

