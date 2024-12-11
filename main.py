import sys
from dni import DNI
from tratamiento_ficheros import GestorFicheros
from fecha_y_hora import FechaYHora
from coordenadas import Coordenadas
from tlf import TLF

def opcion_n(fichero):
    lineas_validadas = GestorFicheros.validar_fichero(fichero)
    for linea in lineas_validadas:
        fecha = FechaYHora()
        fecha.validar_fecha(linea['fecha_hora'])
        coordenada = Coordenadas()
        coordenada.validar_coordenada(linea['coordenadas'])
        print(f"{linea['telefono']}; {linea['nif']}; {fecha.formato1()}; {coordenada.formato_gps()}; {linea['dispositivo']}; {linea['precio']}") 
        
    
def opcion_sphone(telefono, fichero):
    lineas_validadas = GestorFicheros.validar_fichero(fichero)
    for linea in lineas_validadas:
        if TLF.is_equal(linea['telefono'], telefono):
            print(f"{linea['telefono']}; {linea['nif']}; {linea['fecha_hora']}; {linea['coordenadas']}; {linea['dispositivo']}; {linea['precio']}") 
            
def opcion_snif(nif, fichero):
    lineas_validadas = GestorFicheros.validar_fichero(fichero)
    for linea in lineas_validadas:
        if DNI.is_equal(linea['nif'], nif):
            print(f"{linea['telefono']}; {linea['nif']}; {linea['fecha_hora']}; {linea['coordenadas']}; {linea['dispositivo']}; {linea['precio']}") 

def opcion_stime(desde, hasta, fichero):
    lineas_validadas = GestorFicheros.validar_fichero(fichero)
    fechaI = FechaYHora()
    fechaI.validar_fecha(desde)
    fechaF = FechaYHora()
    fechaF.validar_fecha(hasta)
    for linea in lineas_validadas:
        fecha = FechaYHora()
        fecha.validar_fecha(linea['fecha_hora'])
        if fechaI.compare(fecha) == -1 and fechaF.compare(fecha) == 1:
            print(f"{linea['telefono']}; {linea['nif']}; {linea['fecha_hora']}; {linea['coordenadas']}; {linea['dispositivo']}; {linea['precio']}") 
            
        
def verificar_argumentos():
    if len(sys.argv) == 3 and sys.argv[1] == '-n':
        opcion_n(sys.argv[2])
    elif len(sys.argv) == 4 and sys.argv[1] == '-sphone':
        opcion_sphone(sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 4 and sys.argv[1] == '-snif':
        opcion_snif(sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 5 and sys.argv[1] == '-stime':
        opcion_stime(sys.argv[2], sys.argv[3], sys.argv[4])

if __name__ == '__main__':
    verificar_argumentos()
