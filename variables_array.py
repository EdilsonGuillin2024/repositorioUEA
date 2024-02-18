#Desarrollo de  contenido
#Estudiante Edilson Guillin
print("*******************************************INICIO DEL PROGRAMA*********************************************")
#Variables unidimensionales con valores enteros
print("Punto 1: Secuencia de enteros")
secuencia_enteros = [42, 7, 19, 23, 56, 91]
print(secuencia_enteros, "\n")
print("****************************************************************************************************")
#Variables unidimensionales con valores flotantes
print("Punto 2: Secuencia de flotantes")
secuencia_flotantes = [3.14, 1.61, 2.72, 6.28, 9.81, 1.41]
print(secuencia_flotantes, "\n")
print("****************************************************************************************************")
#Variables unidimensionales con valores de texto
print("Punto 3: Secuencia de texto")
secuencia_texto = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta"]
print(secuencia_texto, "\n")
print("****************************************************************************************************")
#Variables unidimensionales mixtas
print("Punto 4: Secuencia combinada")
secuencia_combinada = [42, 3.14, "alpha", 7, 1.61, "beta"]
print(secuencia_combinada, "\n")
print("****************************************************************************************************")
#Variables bidimensionales con valores enteros
print("Punto 5: Matrices  con enteros")
Vetor_A_2x3 = [[42, 7, 19], [23, 56, 91]]
Vector_B_5x5 = [[i+j*5 for i in secuencia_enteros[:5]]
for j in range(5)]
Vector_C_3x6 = [[i+j for i in secuencia_enteros[:6]]
for j in range(3)]
print("Vector A 2x3:", Vetor_A_2x3)
print("Vector B 5x5:", Vector_B_5x5)
print("Vector C 3x6:", Vector_C_3x6, "\n")
print("****************************************************************************************************")
#Variables bidimensionales con valores flotantes
print("Punto 6: Matrices  con flotantes")
Matriz_A_2x3_float = [[3.14, 1.61, 2.72], [6.28, 9.81, 1.41]]
Matriz_B_5x5_float = [[i+j*0.5 
for i in secuencia_flotantes[:5]] 
for j in range(5)]
Matriz_C_3x6_float = [[i+j*0.1 
for i in secuencia_flotantes[:6]] 
for j in range(3)]
print("Matriz A 2x3:", Matriz_A_2x3_float)
print("Matriz B 5x5:", Matriz_B_5x5_float)
print("Matriz C 3x6:", Matriz_C_3x6_float, "\n")
print("****************************************************************************************************")
#Variables bidimensionales con valores de texto
print("Punto 7: Matrices 2D con texto")
Matriz_A_2x3_texto = [["alpha", "beta", "gamma"], ["delta", "epsilon", "zeta"]]
Matriz_B_5x5_texto = [["word"+str(i+j*5)
for i in range(5)] for j in range(5)]
Matriz_C_3x6_texto = [["text"+str(i+j) 
for i in range(6)] for j in range(3)]
print("Matriz A 2x3:", Matriz_A_2x3_texto)
print("Matriz B 5x5:", Matriz_B_5x5_texto)
print("Matriz C 3x6:", Matriz_C_3x6_texto, "\n")
print("****************************************************************************************************")
print("Puntos 9 a 11: Matrices ")

#Variables tridimensionales con valores enteros
matriz_2x3x2 = [[[42, 7], [19, 23], [56, 91]], [[42, 7], [19, 23], [56, 91]]]
matriz_5x5x5 = [[[i+j+k for i in range(5)] 
for j in range(5)] for k in range(5)]
matriz_3x6x2 = [[[i+j for i in range(2)] 
for j in range(6)] for k in range(3)]
print("Matriz 2x3x2 con enteros:", matriz_2x3x2)
print("Matriz 5x5x5 con enteros:", matriz_5x5x5)
print("Matriz 3x6x2 con enteros:", matriz_3x6x2, "\n")
print("****************************************************************************************************")
#Variables tridimensionales con valores flotantes
matriz_2x3x1_float = [[[3.14], [1.61], [2.72]], [[6.28], [9.81], [1.41]]]
matriz_5x5x2_float = [[[i+j*0.1+k*0.01 
for i in range(5)] 
for j in range(5)] for k in range(2)]
matriz_3x6x5_float = [[[i+j*0.01 for i in range(5)] 
for j in range(6)] for k in range(3)]
print("Matriz 2x3x1 con flotantes:", matriz_2x3x1_float)
print("Matriz 5x5x2 con flotantes:", matriz_5x5x2_float)
print("Matriz 3x6x5 con flotantes:", matriz_3x6x5_float, "\n")
print("****************************************************************************************************")
#Variables tridimensionales con valores de texto
matriz_2x3x3_texto = [[["alpha", "beta", "gamma"] 
for _ in range(3)] for _ in range(2)]
matriz_5x5x4_texto = [[["text"+str(i+j+k)
for i in range(4)] for j in range(5)] for k in range(5)]
matriz_3x6x1_texto = [[["word"] for _ in range(6)]
for _ in range(3)]
print("Matriz 2x3x3 con texto:", matriz_2x3x3_texto)
print("****************************************************************************************************")
print("Matriz 5x5x4 con texto:", matriz_5x5x4_texto)
print("****************************************************************************************************")
print("Matriz 3x6x1 con texto:", matriz_3x6x1_texto)
print("********************************************FIN DEL PROGRAMA**********************************************")


