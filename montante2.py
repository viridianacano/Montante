from tkinter import N


print("Eliga la cantidad n en la matriz")
#se lee la dimension de la matriz
filas=int(input("Introduce numero de filas: "))
columnas=int(input("Introduce numero de columnas: "))

matriz= []
matriz_identidad=[]
matriz_adjunta=[]

#se leen los datos de la matriz
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        valor= float(input("Fila {}, Columna {} : ".format(i+1, j+1)))
        matriz[i].append(valor)

#se imprimen los elementos de la matriz
print()
for fila in matriz:
    print("[", end=" ")
    for elemento in fila:
        print("{:8.2f}".format(elemento),end="")
        print("]")
print()

#se define la matriz identidad 
matriz_identidad=[[1, 0, 0],
           [0,1,0], 
           [0,0,1]]

print()

print("Vamos a extender la matriz con la matriz identidad")
for fila in matriz_identidad:
    print("[", end=" ")
    for elemento in fila:
        print("{:8.2f}".format(elemento),end="")
        print("]")
print()

#pivote para la primera iteracion
pivote_ant=1
pivote_actual=matriz[0][0]

print("El pivote anterior es, ",pivote_ant, "pivote_actual", pivote_actual)

print ("El pivote actual es igual a: ", pivote_actual)

#se vuelven ceros los numeros debajo del pivote
matriz[0][1]=0
matriz[0][2]=0

print("nueva matriz")

#imprimiendo la nueva matriz con ceros
for fila in matriz:
    print("[", end=" ")
    for elemento in fila:
        print("{:8.2f}".format(elemento),end="")
        print("]")
print()

#primera iteracion
#matriz original

matriz [1][1]=(pivote_actual*matriz[1][1])-(matriz[1][0]*matriz[0][1])
matriz [1][2]=(pivote_actual*matriz[1][2])-(matriz[1][0]*matriz[0][2])
matriz [2][1]=(pivote_actual*matriz[2][1])-(matriz[2][0]*matriz[0][1])
matriz [2][2]=(pivote_actual*matriz[2][2])-(matriz[2][0]*matriz[0][2])

#matriz aumentada

matriz_adjunta[1][0]=pivote_actual*matriz_identidad[1][0]-matriz[1][0]*matriz_adjunta[0][0]
matriz_adjunta[1][1]=pivote_actual*matriz_identidad[1][1]-matriz[1][0]*matriz_adjunta[0][1]
matriz_adjunta[1][2]=pivote_actual*matriz_identidad[1][2]-matriz[1][0]*matriz_adjunta[0][2]

matriz_adjunta[2][0]=pivote_actual*matriz_identidad[2][0]-matriz[2][0]*matriz_adjunta[0][0]
matriz_adjunta[2][1]=pivote_actual*matriz_identidad[2][1]-matriz[2][0]*matriz_adjunta[0][1]
matriz_adjunta[2][2]=pivote_actual*matriz_identidad[2][2]-matriz[2][0]*matriz_adjunta[0][2]

#segunda iteracion 

#valores del pivote
pivote_ant=pivote_actual
pivote_actual=matriz[1][1]

print("El pivote anterior es, ",pivote_ant, "pivote_actual", pivote_actual)

#volverlos ceros
matriz[0][1]=0
matriz[2][1]=0

#calculos de la primera matriz segunda iteracion

matriz[0][0]=pivote_actual*matriz[0][0]-matriz[1][0]*matriz[0][1]
matriz[0][2]=pivote_actual*matriz[0][2]-matriz[0][1]*matriz[1][2]
matriz[2][0]=pivote_actual*matriz[2][0]-matriz[1][0]*matriz[2][1]
matriz[2][2]=pivote_actual*matriz[2][2]-matriz[2][1]*matriz[1][2]

#calculos de la segunda matriz aumentada
matriz_adjunta[0][0]=pivote_actual*matriz_adjunta[0][0]-matriz[0][1]*matriz_adjunta[1][0]
matriz_adjunta[0][1]=pivote_actual*matriz_adjunta[0][1]-matriz[0][1]*matriz_adjunta[1][1]
matriz_adjunta[0][2]=pivote_actual*matriz_adjunta[0][2]-matriz[0][1]*matriz_adjunta[1][2]

#tercer reglon 
matriz_adjunta[2][0]=pivote_actual*matriz_adjunta[2][0]-matriz[2][1]*matriz_adjunta[1][0]
matriz_adjunta[2][1]=pivote_actual*matriz_adjunta[2][1]-matriz[2][1]*matriz_adjunta[1][1]
matriz_adjunta[2][2]=pivote_actual*matriz_adjunta[2][2]-matriz[2][1]*matriz_adjunta[1][2]

#tercer iteracion
#pivotes
pivote_ant=pivote_actual
pivote_actual=matriz[2][2]

matriz[0][2]=0
matriz[1][2]=0

matriz[0][0]=pivote_actual*matriz[0][0]-matriz[2][0]*matriz[0][2]
matriz[0][1]=pivote_actual*matriz[0][1]-matriz[2][1]*matriz[0][2]
matriz[1][0]=pivote_actual*matriz[1][0]-matriz[2][0]*matriz[1][2]
matriz[1][1]=pivote_actual*matriz[1][1]-matriz[2][1]*matriz[1][2]

#matriz aumentada tecer iteracion

matriz_adjunta[0][0]=pivote_actual*matriz[0][0]-matriz[0][2]*matriz_adjunta[2][0]
matriz_adjunta[0][1]=pivote_actual*matriz[0][1]-matriz[0][2]*matriz_adjunta[2][1]
matriz_adjunta[0][2]=pivote_actual*matriz[0][2]-matriz[0][2]*matriz_adjunta[2][2]

#matriz aumentada segun renglon

matriz_adjunta[1][0]=pivote_actual*matriz_adjunta[1][0]-matriz[1][2]*matriz_adjunta[2][0]
matriz_adjunta[1][1]=pivote_actual*matriz_adjunta[1][1]-matriz[1][2]*matriz_adjunta[2][1]
matriz_adjunta[1][2]=pivote_actual*matriz_adjunta[1][2]-matriz[1][2]*matriz_adjunta[2][2]

#determinante y calculo de la matriz inversa

if(matriz[0][0] &  matriz[1][1] & matriz[2][2]):
    determinante=matriz[1][1]
else:
    print("Hay un error")

#impresion del determinante

print("El determinane es igual a: ", determinante)

#impresion de la matriz adjunta
for fila in matriz_adjunta:
    print("[", end=" ")
    for elemento in fila:
        print("{:8.2f}".format(elemento),end="")
        print("]")
print()
#calculo de la matriz inversa
matriz_inversa=(1/determinante)*(matriz_adjunta)
#impresion matriz inversa
for fila in matriz_inversa:
    print("[", end=" ")
    for elemento in fila:
        print("{:8.2f}".format(elemento),end="")
        print("]")
print()
#soluciones del sistema
vector=[]
for i in range(0,2):
    valor=input("Ingrese los terminos independientes del sistema")
    vector[i]=valor

x1=vector[0]*matriz_inversa[0][0]+vector[1]*matriz_inversa[0][1]+vector[2]*matriz_inversa[0][2]
x2=vector[0]*matriz_inversa[1][0]+vector[1]*matriz_inversa[1][1]+vector[2]*matriz_inversa[1][2]
x3=vector[0]*matriz_inversa[2][0]+vector[1]*matriz_inversa[2][1]+vector[2]*matriz_inversa[2][2]

print("Las soluciones del sistema de ecuacion son",x1," ",x2," ",x3)






