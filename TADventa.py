#TadCompuestoVenta
venta = [0,"","","",0,0.0,None]

#ORDEN: Codigo de droga (int),Nombre (str),droga (str),obra social (str) ,plan(int, plan=1 o plan =2),importe (float),
# fechayhora(none, identificando que esta vacio y que espera otro tipo de dato no estandar)

def crearVenta():          #Crea una venta vacia
    venta = [0,"","","",0,0.0,None]
    return venta

#Ingreso de datos
def cargarVenta(venta,codigo,nombre,droga,obraSocial,plan,importe,fechaHora):   #Asigna valor a una nueva venta 
#la variable fechaHora es de tipo datetime
    venta[0]=codigo
    venta[1]=nombre
    venta[2]=droga
    venta[3]=obraSocial
    venta[4]=plan
    venta[5]=importe
    venta[6]=fechaHora

#Salida de información
def verCodigo(venta):            #imprime el código del medicamento de una venta
    return venta[0]

def verNombre(venta):           #imprime el nombre del medicamento de una venta
    return venta[1]

def verDroga(venta):            #imprime la droga del medicamento de una venta
    return venta[2]

def verObraSocial(venta):       #imprime la obra social referente a una venta
    return venta[3]

def verPlan(venta):             #imprime el plan de la obra social referente a una venta
    return venta[4]

def verImporte(venta):          #imprime el importe de una venta
    return venta[5]

def verFechaHora(venta):        #imprime la fecha y hora de realización de una venta
    return venta[6]

#Procesamiento de datos
def asignarVenta(venta1,venta2): #copia los datos de la venta1 a la venta2 
    venta2[0]=venta1[0]
    venta2[1]=venta1[1]
    venta2[2]=venta1[2]
    venta2[3]=venta1[3]
    venta2[4]=venta1[4]
    venta2[5]=venta1[5]
    venta2[6]=venta1[6]

def cambiarCodigo(venta,nuevoCod):       #modifica el codigo de un medicamento referente a una venta
    venta[0] = nuevoCod

def cambiarNombre(venta,nuevoNom):       #modifica el nombre de un medicamento referente a una venta
    venta[1] = nuevoNom

def cambiarDroga(venta,nuevaDroga):        #modifica la droga de un medicamento referente a una venta
    venta[2] = nuevaDroga

def cambiarObraSocial(venta,nuevaOS):   #modifica la obra social referente a una venta
    venta[3] = nuevaOS

def cambiarPlan(venta,nuevoPlan):         #modifica el plan de la obra social referente a una venta
    venta[4] = nuevoPlan

def cambiarImporte(venta,nuevoImp):      #modifica el importe de una venta
    venta[5] = nuevoImp

def cambiarFechaHora(venta,nuevaFecha):    #modifica la fecha y hora de una venta
    venta[6] = nuevaFecha
