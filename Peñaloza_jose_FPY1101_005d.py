from funciones import *

while True:
    limpiar_pantalla()
    print("EMPRESA")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
    opcion=validar_opcion()
    if opcion==1 :
        funcion1()
    elif opcion==2:
        funcion2()
    elif opcion==3:
        funcion3()
    elif opcion==4:
        funcion4()  
    else:
        final()
        break 