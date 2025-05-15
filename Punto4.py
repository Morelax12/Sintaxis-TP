#4)Informes y actualizaciones por obra social y plan
#TadListaObraSocial
def crearListaObraSocial():

def agregarObraSocial(lista_obra_social, obra_social):

def eliminarObraSocial(lista_obra_social, i):

def recuperarObraSocial(lista_obra_social, i):

def tamanioListaOS(lista_obra_social):

def CopiarListaRecaudado(lista_obra_social1, lista_obra_social2):

#TadObraSocial
def crearObraSocial():
     obra_social=["",0.0]
     return obra_social

def cargarObraSocial(obra_social, nombre, tot):
    obra_social[0]=nombre
    obra_social[1]=tot

def verNombre(obra_social):
    return obra_social[0]


def verTot(obra_social):
    return obra_social[1]

def modificarNombre(obra_social,nombre):
    

def modificarTot(obra_social, Tot):

def copiarObraSocial(obra_social1, obra_social2):

#----------------------------------------------------------------------------------------------------------------------------------------------
#inciso b
#Descuento del 20% para planes específicos
#Al inicio del menú se consulta por pantalla que plan tendra descuento
def plan_con_descuento(): 
    print("***PLAN CON DESCUENTO***")
    plan=input("Ingrese el nombre del plan con descuento: ")
return plan

#En la carga de una venta, se analiza si el plan ingresado = plan. Si es true, se descuenta, sino no.

#------------------------------------------------------------------------------------------------------------------------------------------
#inciso a
#Informe del total recaudado por cada obra social

def cargar_os_nueva(venta, lista_Recaudado_OS): #obtiene los datos p/ nodo ObraSocial de una venta, y los carga en la lista_Recaudado_OS
            ObraSocial=VerOS(venta)
            Monto=verImporte(venta)
                
            o_s=crearObraSocial()
            cargarObraSocial(o_s, ObraSocial, Monto)
            #agrega una obra social a la lista de recaudado por obra social
            agregarObraSocial(lista_Recaudado_OS, o_s)
    
def Imprimir_informe_Tot_Recaudado_OS(lista_Recaudado_OS):
    print("***INFORME DE TOTAL RECAUDADO POR OBRA SOCIAL***")
    
    i = 0                                           #Inicializa la variable de control
    while (i<=tamanio(lista_Recaudado_OS)):                 #Repite condicionalmente mientras haya ventas por recorrer en la lista
        o_s = recuperarObraSocial(lista_Recaudado_OS,i)        #Recupera una venta de la lista en la posicion i

        #Impresión de datos de la venta i     
        printf(f"""
            Nombre de obra social: {verNombre(o_s)}
            Total recaudado: {verTot(o_s)}
        """)

        i=i+1


def generar_informe_tot_recaudado_os(lista_venta):

    lista_recaudado_os = crearListaObraSocial()


    i == 1
    while (i<=tamanio(lista_venta)):             #Repite condicionalmente hasta quer la lista haya sido plenamente recorrida
        venta = recuperarVenta(lista_venta,i)   #Recupera la venta i-esima de la lista y la guarda en la var venta
        
        #Ingresa si la listaRecaudado esta vacia, osea si es la 1er iteración, y carga la 1er obrasocial junto a su monto
        if(Tamanio(lista_Recaudado_os) == 0):
            
            cargar_os_nueva(venta, lista_recaudado_os)                #invoco procedimiento para cargar la 1ra obra social a la lista
            i=i+1           #incremento variable de control
        else 
            j == False         #flag: se activa si se encontro una obra social equivalente a la existente
            #Compara el nombre de la venta en la posicion i-esima con todos los nombre de los nodos obras_Social pertenecientes a la lista_recaudado_OS
            #Entonces la flag se activa UNICAMENTE si encuentra la unica coincidencia. Si nunca la encuentra, entonces esa obra social no se cargo nunca
            n == 1
            while ( n <= tamanio(lista_recaudado_os) and (j != True)):                 #busca una obra social equivalente
                    
                os_aux=recuperarObraSocial(lista_recaudado_os, n)               #Se recupera una obra social en la posicion n
                 
                if( verOs(venta) = verNombre(os1)):                            #Se compara la obra social en la posi n con la venta en la posi i
                    monto_final= VerTot(os1) + VerImporte (venta)                #se acumula el monto que recaudo esa venta de la = obra social
                    modificarTot(os_aux, monto_final)
                    j= True                                                    #Se activa la bandera, y se aborta la repitición condicional. 
                                                                                    #Por lo q se incrementa la var de control una unica vez     
                    i=i+1                                                               
                
                else:
                    n=n+1

            #Se verifica si se activo la flag
            if(j != True):
                cargar_os_nueva(venta, lista_recaudado_os)           #Carga el nom y monto de OS, de la venta q no encontro ninguna equivalencia antes
                i=i+1
    
    
    return lista_recaudado_os


                 
                
            

          
            

        



