#TAD Lista de Ventas - Implementación

def crearListaVentas():
    lista = []
    return lista 

def agregarVenta(lista, venta):
    lista.append(venta)

def eliminarVenta(lista, venta):
    lista.remove(venta)

def recuperarVenta(lista, i):
    return lista[i-1]

def tamanio(lista):
    return len(lista)

