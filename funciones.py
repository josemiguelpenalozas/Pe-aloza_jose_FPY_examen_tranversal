import os,random,csv,msvcrt
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos=[]
empleados=[]


def limpiar_pantalla():
    os.system("cls")

def esperar_tecla():
    print("presione cualquier tecla para continuar")
    msvcrt.getch()

def validar_opcion():
    while True:
        try:
            opcion=int(input("Ingrese opcion que desee: "))
            if opcion>0 and opcion<6:
                return opcion
            else:
                print("ERROR,el numero ingresado no esta dentro de las opciones")
        except:
            print("ERROR, solo se puede ingresar numeros")


def funcion1():
    limpiar_pantalla()
    i=0
    while i<10:
        sueldo=random.randint(300000,2500000)
        sueldos.append(sueldo)
        i=i+1
    print("Sueldos creados con exitó")
    esperar_tecla()

def funcion2():
    i=0
    menores=[]
    menores_sueldo=[]
    cont_men=0

    medio=[]
    medio_sueldo=[]
    cont_med=0

    mayor=[]
    mayor_sueldo=[]
    cont_may=0
    total=0
    while i<10:
        total=total+sueldos[i]
        if sueldos[i]<800000:
            menores.append(trabajadores[i])
            menores_sueldo.append(sueldos[i])
            cont_men=cont_men+1
        elif sueldos[i]>=800000 and sueldos[i]<=2000000:
            medio.append(trabajadores[i])
            medio_sueldo.append(sueldos[i])
            cont_med=cont_med+1
        else:
            mayor.append(trabajadores[i])
            mayor_sueldo.append(sueldos[i])
            cont_may=cont_may+1
        i=i+1

    limpiar_pantalla()
    print("Sueldos menores a $800.000 TOTAL:",cont_men)
    print("Nombre empleado    Sueldo")
    i=0
    while i<len(menores):
        print(menores[i],"  $",menores_sueldo[i])
        i=i+1
    print("")

    print("Sueldos entre $800.000 y $2.000.000 TOTAL:",cont_med)
    print("Nombre empleado    Sueldo")
    i=0
    while i<len(medio):
        print(medio[i],"  $",medio_sueldo[i])
        i=i+1
    print("")

    print("Sueldos superiores a $2.000.000 TOTAL:",cont_may)
    print("Nombre empleado    Sueldo")
    i=0
    while i<len(mayor):
        print(mayor[i],"  $",mayor_sueldo[i])
        i=i+1
    print("")

    print( "TOTAL SUELDOS: $",total)
    esperar_tecla()

def funcion3():
    limpiar_pantalla()
    sueldo_mayor()
    sueldo_menor()
    promedio()
    media_geometrica()
    esperar_tecla()

def funcion4():
    limpiar_pantalla()
    i=0
    while i<len(trabajadores):
        empleado={"nombre empleado":trabajadores[i],
                    "sueldo base":sueldos[i],
                    "desc. salud":sueldos[i]*0.07,
                    "desc.AFP":sueldos[i]*0.12,
                    "sueldo liquido":sueldos[i]-(sueldos[i]*0.12+sueldos[i]*0.07)}

        empleados.append(empleado)
        i=i+1
    print("Nombre empleado Sueldo Base Descuento Salud Descuento AFP Sueldo Líquido")
    i=0
    while i<len(empleados):
        print(empleados[i]["nombre empleado"],end="   ")
        print(empleados[i]["sueldo base"],end="   ")
        print(empleados[i]["desc. salud"],end="   ")
        print(empleados[i]["desc.AFP"],end="   ")
        print(empleados[i]["sueldo liquido"])
        i=i+1

    with open("trabajadores_de_empresa.csv","w",newline="") as archivo:
        escritor=csv.DictWriter(archivo,["nombre empleado","sueldo base","desc. salud","desc.AFP","sueldo liquido"])
        escritor.writeheader()
        escritor.writerows(empleados)
    print("Archivo creado")
    esperar_tecla()

def final():
    limpiar_pantalla()
    print ("Finalizando programa…")
    print("Desarrollado por Jose Miguel Peñaloza Seguel")
    print("20.885.208-6")





def sueldo_mayor():
    consentido=sueldos[0]
    consentido_nombre=trabajadores[0]
    i=1
    while i<len(sueldos):
        if sueldos[i]>consentido:
            consentido=sueldos[i]
            consentido_nombre=trabajadores[i]
        i=i+1
    print("El trabajador ",consentido_nombre," con un sueldo de $",consentido,"es el que tiene el sueldo mayor de la empresa")

def sueldo_menor():
    alejado=sueldos[0]
    alejado_nombre=trabajadores[0]
    i=1
    while i<len(sueldos):
        if sueldos[i]<alejado:
            alejado=sueldos[i]
            alejado_nombre=trabajadores[i]
        i=i+1
    print("El trabajador ",alejado_nombre," con un sueldo de $",alejado,"es el que tiene el sueldo menor de la empresa" )

def promedio():
    i=0
    acum=0
    while i<len(sueldos):
        acum=sueldos[i]+acum
        i=i+1
    print("El promedio de lo sueldos de la empresa es $",acum/10)

def media_geometrica():
    i=0
    acum=1
    while i<len(sueldos):
        acum=sueldos[i]*acum
        i=i+1
    acum=acum**(1/10)
    print("La media geometrica de los sueldos es $",acum)