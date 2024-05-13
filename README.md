# Python-Ejercicios

# Descripcion del ejercicio 
Crear un nuevo archivo llamado analisis_covcol3. csv, cuyo delimitador no
será el que está por defecto (Coma ",") sino un punto y coma ";"; con
este archivo hará lo siguiente:

1.El encabezado debe ser: "ID de caso;Estado;Concepto".
   
2.Lea el archivo COVCOLIII. csv línea por línea, y a medida que vaya
leyendo, escriba en analisis_covcol3. csv lo siguiente:

▪ ID de caso del caso positivo que está leyendo

▪ Un punto y coma (";")

▪ Estado del caso positivo que está leyendo (El estado de la
persona deberá estar completamente en mayúscula, si no lo
está, hacer la conversión)

▪ Un punto y coma (";")

▪ Una cadena de texto que será un concepto respecto a la
edad y estado del caso (Lo resaltado en rojo equivale a UN
espacio en blanco):

• Infante fallecido: Cumple que es menor de edad
(Menor de 18 años) y falleció por covid 19

• Infante sobreviviente: Cumple que es menor de
edad (Menor de 18 años) y no falleció por covid 19

• Adulto fallecido: Cumple que es mayor de edad
(Mayor de 18 años, incluyendo el 18) y falleció por
covid 19

• Adulto sobreviviente: Cumple que es mayor de
edad (Mayor de 18 años, incluyendo el 18) y no falleció
por covid 19

• Retornar los siguientes datos EN ESTE MISMO ORDEN:

1. Edad (En la unidad de medida original) de la persona de sexo
femenino con menor edad contagiada en este conjunto de datos.

3. Unidad de medida de edad de la persona de sexo femenino con
menor edad contagiada en este conjunto de datos.

5. Promedio de edad (En años) de las personas menores de edad
(Menores de 18 años) contagiados en este conjunto de datos QUE
NO FALLECIERON (Para los casos en que la unidad de medida no
sea en años, hacer la conversión, por ejemplo "10" meses de
nacido equivale a "0.8333333333333334" años).

# FORMATO DE SALIDA
La función solucion( ) debe hacer los siguientes retornos en este mismo orden:

• woman_youngest: Número entero (Objeto de la clase int) que
contiene la edad (En la unidad de medida original) de la persona de
sexo femenino más joven contagiada en el conjunto de datos dado.

• unit_youngest: Número entero (Objeto de la clase int) que
contiene la unidad de medida de la edad de la persona de sexo
femenino más joven contagiada en el conjunto de datos dado
(Puede ser 1, 2 o 3 como se especificó anteriormente).

• mean_alive_y: Número flotante (Objeto de la clase float) que
contiene el promedio de edad (En años) de las personas menores
de edad que NO fallecieron por Covid – 19 (No fallecidos).
