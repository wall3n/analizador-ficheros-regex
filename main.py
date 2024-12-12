import sys
from dni import DNI
from tratamiento_ficheros import GestorFicheros
from fecha_y_hora import FechaYHora
from coordenadas import Coordenadas
from tlf import TLF

"""
Precondicion: fichero ha de ser un archivo válido existente
Efecto: recorre el fichero y normaliza las lineas
Resultado: imprime por pantalla las lineas validas normalizadas
"""
def opcion_n(fichero):
    lineas_validadas = GestorFicheros.validar_fichero(fichero)
    for linea in lineas_validadas:
        fecha = FechaYHora()
        fecha.validar_fecha(linea['fecha_hora'])
        coordenada = Coordenadas()
        coordenada.validar_coordenada(linea['coordenadas'])
        print(f"{linea['telefono']}; {linea['nif']}; {fecha.formato1()}; {coordenada.formato_gps()}; {linea['dispositivo']}; {linea['precio']}") 
        
    
"""
Precondicion: telefono ha de ser un telefono válido y fichero un fichero válido existente
Efecto: recorre el fichero y filtra las lineas que coinciden con el telefono
Resultado: imprime por pantalla las lineas que cumplen el criterio
"""
def opcion_sphone(telefono, fichero):
    lineas_validadas = GestorFicheros.validar_fichero(fichero)
    for linea in lineas_validadas:
        if TLF.is_equal(linea['telefono'], telefono):
            print(f"{linea['telefono']}; {linea['nif']}; {linea['fecha_hora']}; {linea['coordenadas']}; {linea['dispositivo']}; {linea['precio']}") 
            
"""
Precondicion: nif ha de ser un DNI valido y fichero un archivo válido
Efecto: recorre el fichero filtrando las lineas que coinciden con el nif
Resultado: Imprime por pantalla las lineas que cumplen el criterio
"""
def opcion_snif(nif, fichero):
    lineas_validadas = GestorFicheros.validar_fichero(fichero)
    for linea in lineas_validadas:
        if DNI.is_equal(linea['nif'], nif):
            print(f"{linea['telefono']}; {linea['nif']}; {linea['fecha_hora']}; {linea['coordenadas']}; {linea['dispositivo']}; {linea['precio']}") 

"""
Precondición: desde y hasta deben de ser dos instantes temporales válidos, fichero debe de ser un fichero válido
Efecto: recorre las lineas del ficheros filtrando las lineas que se encuentre dos instantes temporales
Resultado: imprime por pantalla las lineas que cumplenn el criterio
"""
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

"""
Precondicion: desde debe de ser una coordenada valida, hasta tiene que ser un numero entero que representa los kilometros y el fichero debe de ser un fichero existente
Efecto: Recorre las lineas del fichero filtrando las lineas cuya localización entra dentro del rango
Resultado: Imprime por pantalla las lineas que cumplen la condición
"""
def opcion_slocation(desde, hasta, fichero):
    lineas_validadas = GestorFicheros.validar_fichero(fichero)

    for linea in lineas_validadas: 
        coordenada1 = Coordenadas()
        coordenada1.validar_coordenada(desde)

        coordenada2 = Coordenadas()
        coordenada2.validar_coordenada(linea['coordenadas'])
        if coordenada1.distancia_entre_coordenadas(coordenada2) <= float(hasta):
            print(f"{linea['telefono']}; {linea['nif']}; {linea['fecha_hora']}; {linea['coordenadas']}; {linea['dispositivo']}; {linea['precio']}") 

        
            
        
"""
Precondicion:
Efecto: Comprueba el numero de argumentos y e incova la funcion correspondiente
Resultado: No devuelve nada
"""
def verificar_argumentos():
    if len(sys.argv) == 3 and sys.argv[1] == '-n':
        opcion_n(sys.argv[2])
    elif len(sys.argv) == 4 and sys.argv[1] == '-sphone':
        opcion_sphone(sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 4 and sys.argv[1] == '-snif':
        opcion_snif(sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 5 and sys.argv[1] == '-stime':
        opcion_stime(sys.argv[2], sys.argv[3], sys.argv[4])
    elif len(sys.argv) == 5 and sys.argv[1] == '-slocation':
        opcion_slocation(sys.argv[2], sys.argv[3], sys.argv[4])

if __name__ == '__main__':
    verificar_argumentos()
