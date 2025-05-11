#EJERCICIO 6 FARMACIA

from datetime import datetime
from TadVenta import *
from TADListaVentas import *
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


def imprimirVenta(venta):
    #Imprimir los datos de una venta
    fecha = verFechaHora(venta)
    print(f"""\nCódigo del medicamento: {verCodigo(venta)}
    Nombre del medicamento: {verNombre(venta)}
    Droga: {verDroga(venta)}
    Obra Social: {verObraSocial(venta)}
    Plan: {verPlan(venta)}
    Importe: {verImporte(venta)}
    Fecha: {fecha.strftime("%d")}/{fecha.strftime("%m")}/{fecha.strftime("%Y")} {fecha.strftime("%X")}
          \n""")

def imprimirCola_de_ObrasSociales():
#codigo

# -- DECLARACION DE VARIABLES --
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
            fyh = datetime.now()
            cargarVenta(venta, cod, nom, dro, os, plan, imp, fyh)
            agregarVenta(lista_ventas, venta)
            print("Venta cargada con éxito. \n")
            s = input("¿Desea cargar otra venta? si/no: ").lower()
        print("\nFinalización de ingreso de nuevas ventas de medicamentos. \n")

    #Modificar una venta especifica de la Lista por Codigo del Medicamento
    elif ( opcion == 2):
        print("hola")
        
    #Eliminar venta especifica de la Lista por Codigo de medicamento
    elif ( opcion == 3):

    
    elif (opcion == 4):
    #Mostrar todas las ventas registradas
        if (tamanio(lista_ventas) > 0):
            print("Listado de todas las ventas registradas. \n")
            for i in range(1, tamanio(lista_ventas)+1):
                print("Datos de la venta n° " + i + "\n")
                imprimirVenta(recuperarVenta(lista_ventas, i))
        else:
            print("No hay ventas registradas. \n")

    #Mostrar informe (total recaudado) de todas las Obras sociales
    elif ( opcion == 5):

    #Eliminar venta por droga y las mismas registradas en el ultimo mes
    elif ( opcion == 6):

    #Mostrar ventas registrada (cola) por una obra social especifica
    elif ( opcion == 7):

    #mostrar las ventas registradas en el dia hasta una hora elegida
    elif ( opcion == 8):

    opcion = MENU()
    
print("El programa finalizó.")   
    

