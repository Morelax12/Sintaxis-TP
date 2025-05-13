#EJERCICIO 6 FARMACIA

from datetime import datetime
from TADventa import *
from TADlistadoVentas import *
from TADcolaObraSoc import *

# ------ FUNCIONES PARA EL PROGRAMA ------
def MENU ():

    print("*** ADMINISTRAR LAS VENTAS FARMACEUTICAS ***\n\n" \
    "1- Registrar nuevas ventas\n" \
    "2- Modificar venta especifica\n" \
    "3- Eliminar venta especifica\n" \
    "4- Mostrar listado de ventas registradas\n" \
    "5- Mostrar informe de Obras Sociales\n" \
    "6- Eliminar ventas por Droga \n" \
    "7- Mostrar Ventas registradas por Obra Social\n" \
    "8- Mostrar Ventas registradas en el Dia \n"
    "0- Salir del sistema")
    a= int(input(": "))
    print("\n***********\n")
    return a  

def eliminar_Droga_UltimoMes (lista,drogaB,fechaActual):
    i= 1

    while (i <= tamanio(lista)):

        v = recuperarVenta(lista, i) #recupera la venta de la posicion i-esima
        vFecha = verFechaHora(lista)
        auxLista = crearListaVentas()

        if verDroga(v) == drogaB and vFecha.month == fechaActual.month and vFecha.year == fechaActual.year: #evalia si la droga del elem V es = a la ingresada x el usuario, lo mismo para la fecha
            agregarVenta(auxLista,v) #guarda las ventas que van a ser eliminadas
            eliminarVenta(lista, i)
        i+=1

    return auxLista

def imprimirVenta(venta):
    #Imprimir los datos de una venta
    fecha = verFechaHora(venta)
    print(f"""\n-CODIGO DEL MEDICAMENTO: {verCodigo(venta)}
    -NOMBRE DEL MEDICAMENTO: {verNombre(venta)}
    -DROGA: {verDroga(venta)}
    -OBRA SOCIAL DEL CLIENTE: {verObraSocial(venta)}
    -PLAN: {verPlan(venta)}
    -IMPORTE: {verImporte(venta)}
    -FECHA: {fecha.strftime("%d")}/{fecha.strftime("%m")}/{fecha.strftime("%Y")} {fecha.strftime("%X")}
          \n""")

def imprimirListaVentas(lista):
    i=1

    print("\n**LISTADO DE VENTAS**\n\n")
    while(tamanio(lista)>=i):

        ventaRecu=recuperarVenta(lista,i)
        
        print("*** VENTA",i,"*** \n")
        imprimirVenta(ventaRecu)
       
        i += 1

def ingreso_de_FechayHora():

    while True:
        fecha_str = input("Introduce la fecha y hora (formato: DD/MM/AAAA HH:MM): ")
        try:
            # Intentamos convertir la cadena; si falla, lanza ValueError
            fecha_dt = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M")
            # Si llegamos aquí, la fecha es correcta: salimos del bucle
            break
        except ValueError:
            print("Formato incorrecto. Intenta de nuevo con el formato DD/MM/AAAA HH:MM.\n")
    print("Fecha y hora ingresadas:", fecha_dt)

    return fecha_dt

def imprimirCola_de_ObrasSociales(cola):
     
    while (tamanioCola(cola) != 0):                 #Repite condicionalmente mientras 
        venta = desencolar(cola)                #Desencola una venta

        #Impresión de datos de la venta
        
        print(f"""   
            -NOMBRE DEL MEDICAMENTO: {verNombre(venta)}
            -DROGA: {verDroga(venta)}
            -FECHA DE LA VENTA: {verFechaHora(venta)}
        """)
    
#codigo

# -- DECLARACION DE VARIABLES --
colaObrasS = crearColaObraSoc()
lista_ventas = crearListaVentas()

# ----- PROGRAMA PRINCIPAL -----
print("\n\n*** BIENVENIDOS AL PROGRAMA REGISTRAR VENTAS FARMACEUTICAS *** \n\n")

opcion = MENU()

#CAMBIAR POR CASE
while (opcion != 0):

    if (opcion == 1):
    #Registrar nuevas ventas y cargarlas en la lista de ventas
        print("Ingreso de nuevas ventas de medicamentos. \n")
        s = "si"
        while (s == "si"):
            print("Carga de una venta nueva. \n")
            venta = crearVenta()
            cod = int(input("Ingrese el código del medicamento: "))
            nom = input("Ingrese el nombre del medicamento: ").lower()
            dro = input("Ingrese la droga: ").lower()
            os = input("Ingrese la Obra Social: ").lower()
            plan = input("Ingrese el plan: ").lower()
            imp = float(input("Ingrese el importe: "))
            
            # Pedir al usuario que introduzca la fecha y hora
            fechaD = ingreso_de_FechayHora()

            cargarVenta(venta, cod, nom, dro, os, plan, imp, fechaD)
            agregarVenta(lista_ventas, venta)
            print("Venta cargada con éxito. \n")
            s = input("¿Desea cargar otra venta? si/no: ").lower()
            
        print("\nFinalización de ingreso de nuevas ventas de medicamentos. \n")

    #Modificar una venta especifica de la Lista por Codigo del Medicamento
    elif ( opcion == 2):
        print("...\n")
        
    #Eliminar venta especifica de la Lista por Codigo de medicamento
    elif ( opcion == 3):
        print("...\n")
    
    elif (opcion == 4):
    #Mostrar todas las ventas registradas
        if (tamanio(lista_ventas) > 0):
            print("\n** LISTADO DE VENTAS ** \n\n")
            imprimirListaVentas(lista_ventas)
        else:
            print("No hay ventas registradas. \n")

    #Mostrar informe (total recaudado) de todas las Obras sociales
    elif ( opcion == 5):
        print("...\n")

    #Eliminar venta por droga y las mismas registradas en el ultimo mes
    elif ( opcion == 6):

        drogaD = input("Ingresar el nombre de la Droga que desea eliminar sus ventas: ")
        #pregunto la fecha ya que esto es una simulacion, sino se declararia la funcion para registrar la fecha actual
        while True:
            fecha_str = input("Introduce la fecha y hora (formato: DD/MM/AAAA HH:MM): ")
            try:
                fecha_dt = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M") #convierte la fecha str en un objeto datetime
                break  # Salir del bucle si la conversión fue exitosa
            except ValueError:
                print("Formato incorrecto. Intenta de nuevo con el formato DD/MM/AAAA HH:MM.")

            print("Fecha y hora ingresadas:", fecha_dt)

        ventasEliminadas = eliminar_Droga_UltimoMes (lista_ventas,drogaD,fecha_dt)

        print(" \n\n** LAS VENTAS ELIMINADAS DEL ULTIMO MES DE LA DROGA {drogaD} **\n\n")
        imprimirListaVentas(ventasEliminadas)

    #Mostrar ventas registrada (cola) por una obra social especifica
    elif ( opcion == 7):
        obraSocialD = input("Ingresa la Obra Social de la que desea conocer sus ventas: ")

        i = 1
        while(tamanio(lista_ventas) >= i):

            v = recuperarVenta(lista_ventas,i)

            if( verObraSocial(v) == obraSocialD ):
                encolar(colaObrasS,v)
                
            i += 1
        imprimirCola_de_ObrasSociales(colaObrasS)

    #mostrar las ventas registradas en el dia hasta una hora elegida
    elif ( opcion == 8):

        print("\n ** INFORME DE VENTAS HASTA EL MOMENTO **\n\n" \
        "Ingresar Fecha actual: ")
        
        fechaD = ingreso_de_FechayHora()

        listaVentasInforme = [0,0.0]

        #contadores
        i = 1
        cantM = 0
        montoTotal = 0.0

        while(tamanio(lista_ventas) >= i):

            v = recuperarVenta(lista_ventas,i)
            fechaRecu = verFechaHora(v)

            if( fechaRecu.day == fechaD.day and fechaRecu.month == fechaD.month and fechaRecu.year == fechaD.year and  fechaRecu.hour <= fechaD.hour and fechaRecu.minute <= fechaD.minute):
                cantM  += 1
                montoVenta = verImporte(v)
                montoTotal = montoTotal + montoVenta
          
            i += 1
        
        print("\n\n ** INFORME DE LAS VENTAS ** \n\n" \
        "-CANTIDAD DE MEDICAMENTOS VENDIDOS HASTA LA FECHA: ",cantM,"\n" \
        "-MONTO TOTAL RECAUDADO: ",montoTotal,"\n")

    opcion = MENU()
    
print("El programa finalizó.")   
    

#cuando uso una variable nombreD, la de represeneta DESEADA (ingresada x el usuario)

