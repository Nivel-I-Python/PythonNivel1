# Definimos tres números decimales
numero1 = 3.5
numero2 = 2.1
numero3 = 4.8

# Calculamos el promedio
promedio = (numero1 + numero2 + numero3) / 3

# Mostramos el resultado utilizando f-strings
print(f"El promedio de {numero1}, {numero2} y {numero3} es igual a {promedio:.2f}")

'''
{promedio:.2f} es una parte de la f-string que se utiliza para formatear la salida del número promedio con dos decimales (f lo indica como número de punto flotante)
 en el resultado impreso. Aquí está el significado de cada parte:

{promedio}: Esto es una expresión dentro de la f-string que se evalúa como el valor de la variable promedio que calculamos anteriormente.

:.2f: Esto es una especificación de formato que le dice a Python cómo debe formatear el valor de promedio. En este caso, :.2f significa:

:: Indica que a continuación seguirá un especificador de formato.
.2: Indica que se mostrarán dos lugares decimales después del punto decimal.
f: Indica que el número debe ser formateado como un número de punto flotante.
Por lo tanto, {promedio:.2f} toma el valor de promedio, lo formatea como un número de punto flotante con dos decimales y luego lo incorpora en la cadena de texto.
 Esto asegura que el resultado del promedio se muestre con precisión de dos decimales en la salida.
'''