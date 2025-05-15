def crearColaObraSoc():
    return []

def esVacia(cola):
    return len(cola)==0

def encolar(cola, elem):
    cola.append(elem)

def desencolar(cola):
    elem=cola[0]
    del cola[0]
    return elem

def tamanioCola(cola):
    return len(cola)

def copiarCola(cola1,cola2):
#Copia los datos de una cola a otra
    aux=crearColaObraSoc() 
    while not esVacia(cola2):
        elem=desencolar(cola2)
        encolar(aux,elem) 
    while not esVacia(aux):
        elem=desencolar(aux)
        encolar(cola1,elem)
        encolar(cola2,elem) 