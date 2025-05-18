#TadObraSocial
def crearObraSocial():
     obra_social = ["",0.0]
     return obra_social

def cargarObraSocial(obra_social, nombre, total):
    obra_social[0] = nombre
    obra_social[1] = total

def verNom(obra_social):
    return obra_social[0]

def verTot(obra_social):
    return obra_social[1]

def modificarNom(obra_social,nombre):
    obra_social[0] = nombre
    

def modificarTot(obra_social, tot):
    obra_social[1] = tot

def copiarObraSocial(obra_social1, obra_social2):
    obra_social2[1] = obra_social1[1]
    obra_social2[2] = obra_social1[2]
