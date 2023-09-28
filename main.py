# Pido la cantidad de alumnos
cantidad_alumno = int( input( "Ingrese La cantidad de alumnos: " ) )
promedio_general_suma = 0
nota_mayor = 0
nota_menor = 10
arr_promedios = []

def calcular_promedio(nota1, nota2, nota3):
    return sum( [nota1, nota2, nota3] ) / 3

def calcula_mayor_menor(nota):
    global nota_mayor , nota_menor

    if nota > nota_mayor:
        nota_mayor = nota
    elif nota < nota_menor:
        nota_menor = nota

def calcular_promedio_clase( un_promedio , nombre = "" ):
    global promedio_general_suma
    promedio_general_suma += un_promedio 
    
    arr_promedios.append( [un_promedio , nombre] )
    return promedio_general_suma / cantidad_alumno

def promedio_nombre(nombre , promedio):
    """ Devuelve el resumen de los datos """
    calcular_promedio_clase( promedio , nombre )
    print( nombre ," tiene el promedio de: ", promedio )

def promedios_altos():
    promedio_general = calcular_promedio_clase(0)
    for alumno in arr_promedios:
        if alumno[0] >= promedio_general:
            print(alumno[1], "tiene un promedio sobresaliente con ", alumno[0])

for _ in range( cantidad_alumno ):
    
    nombre_completo =  input( "Ingrese Nombre y apellido :" )

    nota1 = int( input( "Ingrese Nota 1: " ) )
    calcula_mayor_menor( nota1 )
    nota2 = int( input( "Ingrese Nota 2: " ) )
    calcula_mayor_menor( nota2 )
    nota3 = int( input( "Ingrese Nota 3: " ) )
    calcula_mayor_menor( nota3 )

    promedio_nombre(nombre_completo, calcular_promedio (nota1, nota2, nota3) )
    print()
    

print("********** Estadisticas Globales **************")
promedios_altos()
print("la nota mas alta es de :" , nota_mayor)
print("la nota mas baja es de :" , nota_menor)
print( "Promedio General es de: ", calcular_promedio_clase( 0 ) )


  



