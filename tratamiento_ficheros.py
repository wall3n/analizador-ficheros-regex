import regex
from tlf import TLF
from dni import DNI 
from fecha_y_hora import FechaYHora
from coordenadas import Coordenadas
from producto import Producto

re_linea = regex.compile(r"(.*); *(.*); *(.*); *(.*); *(.*); *(.*)\n?")

class GestorFicheros:
    """
    Clase que gestiona la apertura de ficheros y la validacion de linea
    """

    """
    Precondición: linea debe ser una cadena de texto que siga el patrón de la expresión regular
    Efecto: si la linea es válida separa sus elementos, los valida individualmente y los devuelve en un diccionario con claves
    Resultado: un diccionario que asocia cada clave con el valor de la linea
    """
    @staticmethod
    def validar_linea(linea):
        m = re_linea.fullmatch(linea)
        if not m:
            return None
        else:
            tlf_validado = TLF.tlf_valido(m[1])
            nif_validado = DNI.dni_valido(m[2])
            fecha_hora_validada = FechaYHora.fecha_valida(m[3])
            coordenadas_validadas = Coordenadas.coordenada_valida(m[4])
            dispositivo_validado = Producto.validar_nombre_producto(m[5])
            precio_validado = Producto.validar_precio(m[6])
            
            if tlf_validado and nif_validado and fecha_hora_validada and coordenadas_validadas and dispositivo_validado and precio_validado:
                return {
                    "telefono": m[1],
                    "nif": m[2],
                    "fecha_hora": m[3],
                    "coordenadas": m[4],
                    "dispositivo": m[5],
                    "precio": m[6]
                }
            else:
                return "Error en la validación de uno o más campos"

    """
    Precondición: fichero debe de ser un nombre de archivo válido existente
    Efecto: Si el archivo válido lo recorre validando cada linea y guardando las líneas válidas en un array
    Resultado: Un array con las lineas válidas
    """
    @staticmethod
    def validar_fichero(fichero): 
        try:
            lineas_validadas = []
            archivo = open(fichero, encoding='utf8')
            for indice, linea in enumerate(archivo):
                linea_validada = GestorFicheros.validar_linea(linea)
                if not linea_validada or type(linea_validada) != type({}):
                    print(f'Linea {indice} incorrecta')
                else:
                    lineas_validadas.append(linea_validada)
            return lineas_validadas
        except:
            print(f'Error leyendo {archivo}')
            exit(2)

