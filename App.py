#EJERCICIO 6 FARMACIA

from datetime import datetime
from TADventa import *
from TADlistadoVentas import *
from TADcolaObraSoc import *

# ----- FUNCIONES PARA EL PROGRAMA ------
def MENU ():

    print("*** ADMINISTRAR LAS VENTAS FARMACEUTICAS ***\n\n" \
    "1- Registrar Nueva Venta\n" \
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

def imprimirLista_de_Ventas ():
#codigo
def imprimirCola_de_ObrasSociales():
#codigo

# -- DECLARACION DE VARIABLES --

# ----- PROGRAMA PRINCIPAL -----
print("\n\n*** BIENVENIDOS AL PROGRAMA REGISTRAR VENTAS FARMACEUTICAS *** \n\n")

opcion = MENU()

#CAMBIAR POR CASE
while (opcion != 0):

    #Registrar Nueva venta y cargarla en la ListaVentas
    if ( opcion == 1):
        #aplicar descuento del 20% a plan especifico

    #Modificar una venta especifica de la Lista por Codigo del Medicamento
    elif ( opcion == 2):
        print("hola")
        
    #Eliminar venta especifica de la Lista por Codigo de medicamento
    elif ( opcion == 3):

    #Mostrar todas las ventas registradad ( imprimir lista de Ventas)
    elif ( opcion == 4):

    #Mostrar informe (total recaudado) de todas las Obras sociales
    elif ( opcion == 5):

    #Eliminar venta por droga y las mismas registradas en el ultimo mes
    elif ( opcion == 6):

    #Mostrar ventas registrada (cola) por una obra social especifica
    elif ( opcion == 7):

    #mostrar las ventas registradas en el dia hasta una hora elegida
    elif ( opcion == 8):

    opcion = int(input("Ingresar Opcion elegida: "))
    
print("El programa Finalizo")   
    

