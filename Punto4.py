from TAD_lista_obra_social import*
from TAD_obra_social import*
from TADListaVentas import*
from TADventa import*
#4)Informes y actualizaciones por obra social y plan
#----------------------------------------------------------------------------------------------------------------------------------------------
#inciso b: descuento del 20% para planes específicos
#Se considera el usuario cargará una cantidad LIMITADA de planes: Plan GOLD, plan SILVER, y plan BRONZE
#Al inicio del menú se consulta por pantalla que plan tendrá descuento.
#Luego programa generará los descuentos correspondientes cada vez que se ingrese una nueva venta al sistema:
#se analiza si el plan ingresado = plan con descuento. Si lo es, se genera el descuento y se guarda el resultado en IMPORTE. 
def determinar_plan_descuento(): 
    print("""***SELECCION DE PLAN CON DESCUENTO***
          1 - PLAN GOLD
          2 - PLAN SILVER
          3 - PLAN BRONZE""")
    plan_descuento = int(input("SELECCIONE UNA OPCION: "))
    return plan_descuento

#-----------------------------------------------------------------------------------------------------------------------------------------------
#inciso a: informe del total recaudado por cada obra social
#Se considera que le usuario podrá subir una cantidad ILIMITADA de obras sociales. 

#Este procedimiento obtiene ciertos datos de una venta y los ingresa en un variable de tipo ObraSocial, el cual se cargará en la lista de obra sociales
#Se ingresa como DATOS DE ENTRADA: una venta, y la lista de obra sociales por pasaje de parametro por REFERENCIA. 
def cargar_os_nueva(venta, lista_Recaudado_OS): 
            ObraSocial=verNom(venta)                         #Obtiene el nombre de la obra social
            Monto=verImporte(venta)                         #Obtiene el importe de una venta
                
            o_s=crearObraSocial()                           
            cargarObraSocial(o_s, ObraSocial, Monto)        #Carga los datos obtenidos a la obra social creada
            agregarObraSocial(lista_Recaudado_OS, o_s)      #Agrega la obra social a la lista de obra sociales
    
#Este procedimiento imprime la lista de obras sociales, el cual contiene, los nombre de las O.S junto a sus montos totales recaudados respectivamente.
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


#Este procedimiento genera el calculo del totoal recaudado por cada obra social:
#Lógica: 
#Se crea una lista de obras sociales vacia, y se la carga con el 1er nodo de la lista VENTAS (lista preexistente).
#Luego se recupera el 2do nodo de la lista de ventas, y se genera una comparacion con los nodos de la lista de obras sociales.
#En dicha comparación, se evalua si el nombre de la O.Social del 2do nodo es IGUAL al nombre de la o.social de ALGUN nodo de la lista de obras sociales.
#Si la condición es verdadera, se acumula el importe del 2do nodo en el total recaudado del nodo de la o.social, del cual encontro IGUALDAD. 
#En cambio: si la condición es falsa, es decir si no se encontro ninguna obra social con el MISMO NOMBRE de la o.social del 2do nodo; 
#Se crea una tAD tipo obra social nuevo, y se le carga el nombre de la o.social y el importe del 2do nodo. 
#Posteriormente, se agrega el tad obra social nuevo a la lista de Obra sociales. Y se repite toda la secuencia para el 3nodo de la lista de ventas. 
#Finalmente, una vez se haya recorrido la plenitud de la lista de ventas, se obtiene una lista de obras sociales junto a sus montos totales recaudados respectivamente.

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
            while ( n < tamanio(lista_recaudado_os) and (j != True)):                 #Busca una obra social equivalente
                    
                os_aux=recuperarObraSocial(lista_recaudado_os, n)                      #Recupera una obra social en la posicion n
                 
                if( verNom(venta) = verNombre(os_aux)):                                 #Compara la obra social en la posi n con la venta en la posi i
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
          
            

        



