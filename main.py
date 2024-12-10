import sys
from tratamiento_ficheros import GestorFicheros
from fecha_y_hora import FechaYHora

def opcion_n(fichero):
    lineas_validadas = GestorFicheros.validar_fichero(fichero)
    for linea in lineas_validadas:
        fecha = FechaYHora()
        fecha.validar_fecha(linea['fecha_hora'])
        print(f"{linea['telefono']}; {linea['nif']}; {fecha.formato1()}; {linea['coordenadas']}; {linea['dispositivo']}; {linea['precio']}") 
        
    
def opcion_sphone(telefono, fichero):
    pass

def opcion_snif(nif, fichero):
    pass
def opcion_stime(desde, hasta, fichero):
    pass

def verificar_argumentos():
    if len(sys.argv) == 3 and sys.argv[1] == '-n':
        opcion_n(sys.argv[2])
    elif len(sys.argv) == 4 and sys.argv[1] == '-sphone':
        opcion_sphone(sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 4 and sys.argv[1] == '-snif':
        opcion_snif(sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 4 and sys.argv[1] == '-stime':
        opcion_stime(sys.argv[2], sys.argv[3], sys.argv[4])

if __name__ == '__main__':
    verificar_argumentos()
