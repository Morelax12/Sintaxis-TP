#EJERCICIO 6 FARMACIA

from datetime import datetime
from TADventa import *
from TADListaVentas import *
from TADcolaObraSoc import *
from TAD_lista_obra_social import *
from TAD_obra_social import *
from terminaltexteffects.effects.effect_matrix import Matrix
from terminaltexteffects.effects.effect_slide import Slide
from terminaltexteffects.utils.graphics import Color

#------------------------------------------------ FUNCIONES PARA EL PROGRAMA ------------------------------------------------
def MENU ():

    effect = Matrix("*** ADMINISTRAR LAS VENTAS FARMACEUTICAS ***\n\n" \
    "1- Registrar nuevas ventas\n" \
    "2- Modificar venta especifica\n" \
    "3- Eliminar venta especifica\n" \
    "4- Mostrar listado de ventas registradas\n" \
    "5- Mostrar informe de Obras Sociales\n" \
    "6- Eliminar ventas por Droga del ultimo mes\n" \
    "7- Mostrar Ventas registradas por Obra Social\n" \
    "8- Mostrar Ventas registradas en el Dia \n"
    "9- Mostrar informe de planes con descuento\n"
    "0- Salir del sistema")

    effect.effect_config.merge = True
    effect.effect_config.rain_time = .5
    effect.effect_config.rain_fall_delay_range = [0, 1]
    #Dejar simbolos por defecto o cambiar a 0 y 1
    effect.effect_config.rain_symbols = ["0", "1"]
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

    a= int(input(": "))
    print("\n*\n")

    return a

#--------------------------------- FUNCION DE DESCUENTO PARA PLAN ESPECIFICO ---------------------------------

#Se considera el usuario cargará una cantidad LIMITADA de planes: Plan GOLD, plan SILVER, y plan BRONZE
#Al inicio del menú se consulta por pantalla que plan tendrá descuento.
#Luego programa generará los descuentos correspondientes cada vez que se ingrese una nueva venta al sistema:
#se analiza si el plan ingresado = plan con descuento. Si lo es, se genera el descuento y se guarda el resultado en IMPORTE. 
def determinar_plan_descuento():

    effect = Slide("""***SELECCION DE PLAN CON 20% DESCUENTO***
          1 - PLAN GOLD
          2 - PLAN SILVER
          3 - PLAN BRONZE\n
SELECCIONE UNA OPCION""")
    effect.effect_config.merge = True
    effect.effect_config.final_gradient_stops = (Color("008F11"), Color("008F11"))
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

    plan_descuento = int(input(": "))
    return plan_descuento
#--------------------------------- FUNCIONES Y PROCEDIMIENTOS DE OPCION 5 ---------------------------------
#cargar_os_nueva: obtiene ciertos datos de una venta y los ingresa en un variable de tipo ObraSocial, el cual se cargará en la lista de obra sociales
#Se ingresa como DATOS DE ENTRADA: una venta, y la lista de obra sociales por pasaje de parametro por REFERENCIA. 
def cargar_os_nueva(venta, lista_Recaudado_OS): 
            ObraSocial=verObraSocial(venta)                         #Obtiene el nombre de la obra social
            Monto=verImporte(venta)                         #Obtiene el importe de una venta
                
            o_s=crearObraSocial()                           
            cargarObraSocial(o_s, ObraSocial, Monto)        #Carga los datos obtenidos a la obra social creada
            agregarObraSocial(lista_Recaudado_OS, o_s)      #Agrega la obra social a la lista de obra sociales

#Imprimir_informe_Tot_Recaudado_OS: imprime la lista de obras sociales, el cual contiene, los nombre de las O.S junto a sus montos totales recaudados respectivamente.
#Se ingresa como DATOS DE ENTRADA: la lista de obra sociales por parametro por COPIA
def Imprimir_informe_Tot_Recaudado_OS(lista_Recaudado_OS):
    print("***INFORME DE TOTAL RECAUDADO POR OBRA SOCIAL***")
    
    i = 1                                                   #Inicializa la variable de control
    while (i<=tamanio(lista_Recaudado_OS)):                 #Repite condicionalmente mientras haya ventas por recorrer en la lista
        o_s = recuperarObraSocial(lista_Recaudado_OS,i)     #Recupera una venta de la lista en la posicion i

        #Impresión de datos de la venta i     
        print(f"""
            Nombre de obra social: {verNom(o_s)}
            Total recaudado: {verTot(o_s)}
        """)

        i=i+1

#generar_informe_tot_recaudado_os: genera el calculo del totoal recaudado por cada obra social:
#Se ingresa como DATOS DE ENTRADA: la lista de obra sociales por COPIA
def generar_informe_tot_recaudado_os(lista_venta):

    lista_recaudado_os = crearListaObraSocial()

    i = 1
    while (i<=tamanio(lista_venta)):                                #Repite condicionalmente hasta quer la lista haya sido plenamente recorrida
        venta = recuperarVenta(lista_venta,i)                       #Recupera la venta i-esima de la lista y la guarda en la var venta
        
        #Ingresa si la listaRecaudado esta vacia, osea si es la 1er iteración, y carga la 1er obrasocial junto a su monto
        if(tamanio(lista_recaudado_os) == 0):
            
            cargar_os_nueva(venta, lista_recaudado_os)              #invoco procedimiento para cargar la 1ra obra social a la lista
            i=i+1           #incremento variable de control
        else:
            j = False
            n = 1         
            #flag: se activa si se encontro una obra social equivalente a la existente
            #Compara el nombre de la venta en la posicion i-esima con todos los nombre de los nodos obras_Social pertenecientes a la lista_recaudado_os
            #Entonces la flag se activa UNICAMENTE si encuentra la unica coincidencia. Si nunca la encuentra, entonces esa obra social nunca se cargo
            while ( n <= tamanio(lista_recaudado_os) and (j != True)):                 #Busca una obra social equivalente
                    
                os_aux=recuperarObraSocial(lista_recaudado_os, n)                      #Recupera una obra social en la posicion n
                 
                if( verObraSocial(venta).lower() == verNom(os_aux).lower()):                                 #Compara la obra social en la posi n con la venta en la posi i
                    monto_final= verTot(os_aux) + verImporte(venta)                   #Acumula el monto que recaudo esa venta de la = obra social
                    modificarTot(os_aux, monto_final)
                    j= True                                                            #Activa la bandera, y aborta la repitición condicional. 
                                 
                    i=i+1                                                              #Incrementa la var de control i                                                         
                
                else:
                    n=n+1                                                               #Incrementa la var de control n

            #Se verifica si la flag esta activada
            if(j != True):
                cargar_os_nueva(venta, lista_recaudado_os)           #Carga el nom y monto de OS, de la venta q no encontro ninguna equivalencia antes
                i=i+1
    
    
    return lista_recaudado_os


#--------------------------------- FUNCION DE OPCION 6 ---------------------------------

def eliminar_Droga_UltimoMes (lista,drogaB,fechaActual):
    i= 1

    auxLista = crearListaVentas()

    while (i <= tamanio(lista)):

        v = recuperarVenta(lista, i) #recupera la venta de la posicion i-esima
        vFecha = verFechaHora(v)

        if verDroga(v) == drogaB and vFecha.month == fechaActual.month and vFecha.year == fechaActual.year: #evalia si la droga del elem V es = a la ingresada x el usuario, lo mismo para la fecha
            agregarVenta(auxLista,v) #guarda las ventas que van a ser eliminadas
            eliminarVenta(lista, v) #al eliminar una venta el i=1 no representa a la misma venta que antes de eliminar una venta, entonces se vuelve a ejecutar el bucle 


        else: #si la venta no cumple con la condicion(if) debe aumentar el indice, para evaluar la siguiente venta
            i+=1

    return auxLista

#--------------------------------- FUNCION DE INGRESAR FECHA Y HORA ---------------------------------

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

#--------------------------------- FUNCION DE DESCUENTO PARA PLAN ESPECIFICO: OPCION 9 ---------------------------------

#Se considera el usuario cargará una cantidad LIMITADA de planes: Plan GOLD, plan SILVER, y plan BRONZE
#El descuento se generará a partir de una opcion del menú, donde se pregunta por pantalla que plan poseera el descuento.
#Luego programa generará los descuentos correspondientes recorriendo la lista de ventas:
#se analiza si el plan ingresado = plan con descuento. Si lo es, se genera el descuento y se GUARDA el resultado en IMPORTE.
#Asi mismo, se informa por pantalla un listado de las ventas modificadas, desvelando (código, nombre, droga, obra social, 
# importe original e importe final) de cada una.

#Se ingresa como DATOS DE ENTRADA: lista ventas por pasaje de parametro por REFERENCIA.
def generar_descuento_plan(lista_venta):

    print("Generando descuentos...")
    i=1
    j = False
    while( i <= tamanio(lista_venta)):
        venta = recuperarVenta(lista_venta,i)
                                                                               #flag: demuestra que existe almenos una venta con el plan ingresado
        if (plan_con_descuento == verPlan(venta)):                           #Ingresa si encuentra planes coincidentes al seleccionado por el usuario
            importe_original = verImporte(venta)
            importeNuevo= verImporte(venta) - (verImporte(venta)*20/100)     #Genera y guarda el descuento en la lista de ventas
            cambiarImporte(venta,importeNuevo) 
            j = True

            #Imprime los datos de la venta modificada
            print(f"""Venta {i}:                                                        
                  Codigo: {verCodigo(venta)}
                  Nombre: {verNombre(venta)}
                  Droga: {verDroga(venta)}
                  Obra Social: {verObraSocial(venta)}
                  Importe original: {importe_original}
                  Importe aplicado el descuento: {verImporte(venta)}
                  """)
            
            i=i+1
        else:
            i=i+1                                                                      #incrementa la variable de control
    
    if (j == False):                                                                    #Ingresa si no se encontro ningun plan concordante al ingresado
        print("El plan seleccionado no pertenece a ninguna venta")


#--------------------------------- FUNCIONES DE IMPRESION ---------------------------------

def imprimirVenta(venta):
    #Imprimir los datos de una venta
    fecha = verFechaHora(venta)
    print(f"""\n-CODIGO DEL MEDICAMENTO: {verCodigo(venta)}
-NOMBRE DEL MEDICAMENTO: {verNombre(venta).upper()}
-DROGA: {verDroga(venta).upper()}
-OBRA SOCIAL DEL CLIENTE: {verObraSocial(venta).upper()}
-PLAN: {verPlan(venta)}
-IMPORTE: {verImporte(venta)}
-FECHA: {fecha.strftime("%d")}/{fecha.strftime("%m")}/{fecha.strftime("%Y")} {fecha.strftime("%X")}
            \n""")

def imprimirListaVentas(lista):
    i=1

    print("\n**LISTADO DE VENTAS**\n\n")
    while(tamanio(lista)>=i):

        ventaRecu = recuperarVenta(lista, i)
        
        print("*** DATOS DE LA VENTA", i ,"*** \n")
        imprimirVenta(ventaRecu)
       
        i += 1

def imprimirCola_de_ObrasSociales(cola):
     
    while (tamanioCola(cola) != 0):                 #Repite condicionalmente mientras 
        venta = desencolar(cola)                #Desencola una venta
        fecha = verFechaHora(venta)
        #Impresión de datos de la venta
        
        print(f"""   
            -NOMBRE DEL MEDICAMENTO: {verNombre(venta).upper()}
            -DROGA: {verDroga(venta).upper()}
            -FECHA DE LA VENTA: {fecha.strftime("%d")}/{fecha.strftime("%m")}/{fecha.strftime("%Y")} {fecha.strftime("%X")}
        """)
    


#------------------------------------------------ SIMULACION DEL PROGRAMA ------------------------------------------------

# -- DECLARACION DE VARIABLES --
colaObrasS = crearColaObraSoc()
lista_ventas = crearListaVentas()

#--------------------------------- PROGRAMA ---------------------------------

#print("\n\n*** BIENVENIDOS AL PROGRAMA REGISTRAR VENTAS FARMACEUTICAS *** \n\n")

effect = Slide("\n\n*** BIENVENIDOS AL PROGRAMA REGISTRAR VENTAS FARMACEUTICAS *** \n\n")
effect.effect_config.merge = True
effect.effect_config.final_gradient_stops = (Color("008F11"), Color("008F11"))
with effect.terminal_output() as terminal:
    for frame in effect:
        terminal.print(frame)


#Se consulta el plan que poseera el 20% de descuento
plan_con_descuento = determinar_plan_descuento()                    #Resolución punto 4)b

opcion = MENU()

#CAMBIAR POR CASE
while (opcion != 0):

    match opcion:

        case 1:
        #Registrar nuevas ventas y cargarlas en la lista de ventas
            print("Ingreso de nuevas ventas de medicamentos. \n")
            s = "si"
            while (s == "si"):
                print("Carga de una venta nueva. \n")
                venta = crearVenta()

                #carga codigo
                while True:
                    try:
                        cod = int(input("Ingrese el código del medicamento: "))
                        break  # Sale del bucle si no hay error

                    except ValueError:
                        print("Error: ingresá un número entero válido.")
                

                nom = input("Ingrese el nombre del medicamento: ").lower()
                dro = input("Ingrese la droga: ").lower()
                os = input("Ingrese la Obra Social: ").lower()
                #ingresar plan
                while True:

                    print("""*** SELECCIONE EL PLAN ***
                        1 - PLAN GOLD
                        2 - PLAN SILVER
                        3 - PLAN BRONZE""")
                    plan = int(input("Opcion: "))

                    if plan <= 3 and plan > 0:
                        break
                    else:
                        print("Plan invalido,vuelva a intentarlo \n")

                #ingresar importe
                while True:
                    
                    imp = float(input("Ingrese el importe: "))
                    try:
                        if imp < 0:
                            raise ValueError("El importe no puede ser negativo\n")
                        break
                    except ValueError:
                        print("El importe es invalido,vuelva a intentarlo\n")

                
                # Pedir al usuario que introduzca la fecha y hora
                fechaD = ingreso_de_FechayHora()

                #Se evalua si corresponde un 20% respecto el plan ingresado
                if plan_con_descuento == plan:
                    imp = imp - (imp*20/100)
                    print(f"Se aplicó el descuento correspondiente al plan",plan)

                cargarVenta(venta, cod, nom, dro, os, plan, imp, fechaD)
                agregarVenta(lista_ventas, venta)
                print("Venta cargada con éxito. \n")
                s = input("¿Desea cargar otra venta? si/no: ").lower()
                
            print("\nFinalización de ingreso de nuevas ventas de medicamentos. \n")

        
        case 2:
            #Modificar una venta especifica de la lista por nombre del medicamento
            nombre=input("Ingrese el nombre del medicamento a modificar: ").lower()
            control=False
            encontrado=False
            for i in range(1, tamanio(lista_ventas)+1):
                vent=recuperarVenta(lista_ventas, i)
                if verNombre(vent)==nombre:
                    encontrado=True
                    control=True

                    
                while control:
                    print(f"Venta {i}:")
                    print("\n¿Qué quiere modificar?\n")
                    print("1 - Código del medicamento")
                    print("2 - Nombre del medicamento")
                    print("3 - Droga del medicamento")
                    print("4 - Obra Social asociada a la venta")
                    print("5 - Importe de la venta")
                    print("6 - Fecha y hora de la venta")
                    print("7 - Salir\n")
                    try:
                        mod=int(input("Seleccionar: "))
                    except ValueError:
                        print("\nEl número ingresado no es válido\n")
                        continue
                    if mod==1:
                        nuevo=int(input("Ingrese nuevo código del medicamento: "))
                        cambiarCodigo(vent, nuevo)
                        print("Código modificado con éxito. \n")
                    elif mod==2:
                        nuevo=input("Ingrese nuevo nombre del medicamento: ").lower()
                        cambiarNombre(vent, nuevo)
                        print("Nombre modificado con éxito. \n")
                    elif mod==3:
                        nuevo=input("Ingrese nueva droga del medicamento: ").lower()
                        cambiarDroga(vent, nuevo)
                        print("Droga modificada con éxito. \n")
                    elif mod==4:
                        nuevo=input("Ingrese nueva obra social asociada a la venta: ").lower()
                        cambiarObraSocial(vent, nuevo)
                        print("Obra Social modificada con éxito. \n")
                    elif mod==5:
                        nuevo=float(input("Ingrese nuevo importe de la venta: "))
                        cambiarImporte(vent, nuevo)
                        print("Importe modificado con éxito. \n")
                    elif mod==6:
                        nuevo=ingreso_de_FechayHora()
                        cambiarFechaHora(vent, nuevo)
                        print("Fecha y hora modificada con éxito. \n")
                    elif mod==7:
                        control=False
                    else:
                        print("\nOpción no válida\n")  
                        continue

            if not encontrado:
                print("No se encontró venta con el nombre ingresado\n")
            
        
        case 3:
            #Eliminar venta especifica de la lista por codigo de medicamento
            if tamanio(lista_ventas)==0:
                print("No hay ventas para eliminar.\n")
            else:
                codigo=int(input("Ingrese el código del medicamento a eliminar: "))
                i=1
                eliminado=False
                while i<=tamanio(lista_ventas):
                    venta=recuperarVenta(lista_ventas, i)
                    if verCodigo(venta)==codigo:
                        eliminarVenta(lista_ventas, venta)
                        print("\nVenta eliminada con éxito.\n")
                        eliminado = True
                    else:    
                        i = i+ 1
                if not eliminado:
                    print("No se encontró venta con el código ingresado.\n")
        
        case 4:
        #Mostrar todas las ventas registradas
            if (tamanio(lista_ventas) > 0):
                print("\n** LISTADO DE VENTAS ** \n\n")
                imprimirListaVentas(lista_ventas)
            else:
                print("No hay ventas registradas. \n")

        #Mostrar informe (total recaudado) de todas las Obras sociales
        case 5:
            print("Generando informe de total recaudado por obra social...")
            lista_tot_obra_social = generar_informe_tot_recaudado_os(lista_ventas)

            if (tamanio(lista_tot_obra_social) == 0):
                print("No se pudo generar el informe ya que no existen ventas")
            else:    
                print("informe generado existosamente")
                Imprimir_informe_Tot_Recaudado_OS(lista_tot_obra_social)

        #Eliminar venta por droga y las mismas registradas en el ultimo mes
        case 6:

            # Bucle para verificar si la droga ingresada está en la lista
            while True:
                drogaD = input("Ingresar el nombre de la Droga que desea eliminar sus ventas: ")

                # Verificar si la droga existe en la lista
                droga_encontrada = False #creamos una bandera (para verificar si algo ocurrio(true) sino (false), la inicalizamos en false)

                for i in range (1 ,tamanio(lista_ventas)+1): #recorre la lista ventas, en ventaRecu se almacena cada venta encontrada

                    ventaRecu= recuperarVenta(lista_ventas,i)

                    if verDroga(venta).lower() == drogaD.lower(): #verifica si la droga se encuentra en la lista de ventas
                        droga_encontrada = True
                        break
                
                #evaluamos la bandera, para saber que ocurrio, si encontro la droga(true) sino (false)

                if not droga_encontrada: #si drogra encontrada es falso, se informa y se muestran opciones
                    print(f"\nLa droga '{drogaD}' no se encuentra registrada en las ventas.")

                    #opciones 
                    eleccion = input("¿Desea intentar con otra droga? (S/N): ").strip().lower() #strip elimina espacios en blanco al inicio y al final
                    if eleccion != 's':
                        print("Volviendo al menú principal...\n")
                        break  # Salimos del while general (opción 6), volvemos al menu principal, ya que si se llega a este break termina la ejecucion de la opcion 6
                
                #si droga encontrada es true, se pide la fecha y se eliminan las ventas del mes
                else: 
                    # Pregunto la fecha (ya que es una simulación)
                    while True:
                        fecha_str = input("Introduce la fecha y hora (formato: DD/MM/AAAA HH:MM): ")
                        try:
                            fecha_dt = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M")
                            break
                        except ValueError:
                            print("Formato incorrecto. Intenta de nuevo con el formato DD/MM/AAAA HH:MM.")

                    print("Fecha y hora ingresadas:", fecha_dt)

                    # Proceder a eliminar ventas
                    ventasEliminadas = eliminar_Droga_UltimoMes(lista_ventas, drogaD, fecha_dt)

                    print(f"\n\n** LAS VENTAS ELIMINADAS DEL ULTIMO MES DE LA DROGA {drogaD} **\n\n")
                    imprimirListaVentas(ventasEliminadas)

                    break  # Salimos del while principal ya que ya se realizó la acción


        #Mostrar ventas registrada (cola) por una obra social especifica
        case 7:
            while True:

                obraSocialD = input("Ingresa la Obra Social de la que desea conocer sus ventas: ").lower()

                #verificamos que la obrasocialD exista en el listado de ventas
                obraS_encontrada=False

                for i in range (1 ,tamanio(lista_ventas)+1):

                    venta = recuperarVenta(lista_ventas,i)

                    if verObraSocial(venta).lower() == obraSocialD.lower():
                        obraS_encontrada = True
                        break

                #si obraS encontrada es falsa(no se encuentra en el listado), mostrar opciones
                if not obraS_encontrada:
                    print(f"\nLa Obra Social '{obraSocialD}' no se encuentra registrada en las ventas.\n")
                    
                    #opciones 
                    eleccion = input("¿Desea intentar con otra Obra social? (S/N): ").strip().lower() #strip elimina espacios en blanco al inicio y al final
                    if eleccion != 's':
                        print("Volviendo al menú principal...\n")
                        break  # Salimos del while general (opción 6)   
                #si se encuentra la obra social(obraS = true)
                else:
                    #recorremos la lista
                    for i in range (1 ,tamanio(lista_ventas)+1):
                        venta= recuperarVenta(lista_ventas,i)
                        
                        #evaluamos si la O.S de la venta recuperada es igual a la desada
                        if verObraSocial(venta).lower() == obraSocialD.lower():
                            encolar(colaObrasS,venta)

                    imprimirCola_de_ObrasSociales(colaObrasS)
                    break #salimos del while principal

        #mostrar las ventas registradas en el dia hasta una hora elegida
        case 8:

            print("\n ** INFORME DE VENTAS HASTA EL MOMENTO **\n\n" \
                    "Ingresar Fecha actual: ")
                    
            fechaD = ingreso_de_FechayHora() #se registra la fecha deseada para analizar las ventas del dia,ingresada por el usuario

            #contadores
            i = 1                       #v.Control
            cantM = 0                   #Contador de cantidad de medicamentos vendidos
            montoTotal = 0.0            #v. almacena el monto total recaudado de todas las ventas

            while(tamanio(lista_ventas) >= i): #recorremos la lista_ventas hasta alcanzar su ultima venta

                v = recuperarVenta(lista_ventas,i) #recuperamos una venta en la posicion i-esinma
                fechaRecu = verFechaHora(v)        #obtenemos la fecha de la venta recuperada, para luego usarla como condicion

                #para tener en cuenta la venta en el informe(fechaRecu), esta debe: ser el mismo dia,mes y año que fechaD, y la hora debe ser menor o igual a la de fechaD
                if( fechaRecu.day == fechaD.day and fechaRecu.month == fechaD.month and fechaRecu.year == fechaD.year and fechaRecu.hour <= fechaD.hour):
                    #luego evaluamos los minutos, xq si lo ponemos en el primer if, podria ser que una venta 11:40 y la hora max es 12:20, 40>20 entonces en el primer if no cumpliria la condicion y dejaria ventas afueras
                    if(fechaRecu.minute <= fechaD.minute):

                        cantM  += 1                             #aumentamos el contador de medicamentos, ya que la venta fue valida(pertenece al mismo dia)
                        montoVenta = verImporte(v)              #obtenemos cuanto valio la venta
                        montoTotal = montoTotal + montoVenta    #sumamos al total el monto de la venta
                    
                i += 1
                    
            print("\n\n ** INFORME DE LAS VENTAS ** \n\n" \
            "-CANTIDAD DE MEDICAMENTOS VENDIDOS HASTA LA FECHA: ",cantM,"\n" \
            "-MONTO TOTAL RECAUDADO: ",montoTotal,"\n")

        #Genera e imprime el informe de ventas con planes con descuento
        case 9:
            generar_descuento_plan(lista_ventas)

    opcion = MENU()
   
effect = Slide("El programa finalizó.")
effect.effect_config.merge = True
effect.effect_config.final_gradient_stops = (Color("008F11"), Color("008F11"))
with effect.terminal_output() as terminal:
    for frame in effect:
        terminal.print(frame)



