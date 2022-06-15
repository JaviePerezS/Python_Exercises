import csv

def solucion():

    lista_edad_medida = []
    edades_mujeres = []
    edades_infantes = []

    with open('COVCOLIII.csv', 'r', newline= '') as Archivo:
        archivo_entrada = csv.reader(Archivo, delimiter=',')
        archivo_salida = open('analisis_covcol3.csv', 'w', newline='')
        archivo_salida = csv.writer(archivo_salida, delimiter=';')

        encabezados = ["ID de caso", "Estado", "Concepto"]
        archivo_salida.writerow(encabezados)
        next(archivo_entrada)

        for fila in archivo_entrada:

            id_caso = fila[2]
            edad = int(fila[5])
            unidad_medida = int(fila[6])
            sexo = fila[7]
            estado = fila[8 ]
            estado_upper = estado.upper()

            lista_edad_medida.append(unidad_medida)

            if unidad_medida == 3:
                edad = edad / 365
            elif unidad_medida == 2:
                edad = edad / 12

            if edad < 18 and estado_upper == "FALLECIDO":
                concepto = "Infante fallecido"
            elif edad < 18 and estado_upper != "FALLECIDO":
                concepto = "Infante sobreviviente"
                edades_infantes.append(edad)
            elif edad >= 18 and estado_upper == "FALLECIDO":
                concepto = "Adulto fallecido"
            elif edad >= 18 and estado_upper != "FALLECIDO":
                concepto = "Adulto sobreviviente"
            
            archivo_salida.writerow([id_caso, estado_upper, concepto])

            if sexo == "F" or sexo == "f":
                edades_mujeres.append(edad)
        
        woman_youngest = min(edades_mujeres)
        unit_youngest = min(lista_edad_medida)

        if unit_youngest == 3:
            woman_youngest = woman_youngest * 365
        elif unit_youngest == 2:
            woman_youngest = woman_youngest * 12

        mean_alive_y = sum(edades_infantes) / len(edades_infantes)

        return woman_youngest, unit_youngest, mean_alive_y

print(solucion())

solucion() 