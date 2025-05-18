#tad lista obra social
def crearListaObraSocial():
    lista_obra_social=[]
    return lista_obra_social

def agregarObraSocial(lista_obra_social, obra_social):
    lista_obra_social.append(obra_social)

def eliminarObraSocial(lista_obra_social, obra_social):
    lista_obra_social.remove(obra_social)

def recuperarObraSocial(lista_obra_social,i):
    return lista_obra_social[i-1]
def tamanioListaObraSocial(lista_obra_social):
    return len(lista_obra_social)
