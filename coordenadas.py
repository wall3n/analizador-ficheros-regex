import regex
import math

er_formato1 = r"(?P<formato1>(?P<latitud>[\+\-]?\d{1,2}\.\d+)\s*,\s*(?P<longitud>[\+\-]?\d{1,3}\.\d+))\s*"
er_formato2 = r"(?P<formato2>(?P<latitud>(?P<grados>\d{1,2})°\s*(?P<minutos>\d{1,2})‘\s*(?P<segundos>\d{1,2}\.\d{4})\"\s+(?P<orientacion>[NS]),\s*)(?P<longitud>(?P<grados1>\d{1,2})°\s*(?P<minutos1>\d{1,2})‘\s*(?P<segundos1>\d{1,2}\.\d{4})\"\s+(?P<orientacion1>[WE])))\s*"
er_formato3 = r"(?P<formato3>(?P<latitud>(?P<grados>\d{3})(?P<minutos>\d{2})(?P<segundos>\d{2}\.\d{4})(?P<orientacion>[NS]))(?P<longitud>(?P<grados1>\d{3})(?P<minutos1>\d{2})(?P<segundos1>\d{2}\.\d{4})(?P<orientacion1>[WE])))\s*"
re_coordenadas = regex.compile(f'{er_formato1}|{er_formato2}|{er_formato3}')

# Latitud Y Longitud X

class Coordenadas:
    """
    Clase que representa coordenadas, las valida y las compara
    """
    
    def __init__(self):
        self.gradosX = 0
        self.minutosX = 0
        self.segundosX = 0.0
        self.orientacionX = ""
        self.gradosY = 0
        self.minutosY = 0
        self.segundosY = 0.0
        self.orientacionY = ""
        self.validado = False

    """
    Precondicion: coordenada ha de ser una cadena que contenga una coordenada valida
    Efecto: valida la coordenada en sus distintos formatos y la almacena en formarto sexagesimal
    Resultado: Este metodo no devuelve nada ya que modifica los atributos de clase
    """
    def validar_coordenada(self, coordenada):
        if Coordenadas.coordenada_valida(coordenada):
            match = re_coordenadas.fullmatch(coordenada)
            if match['formato1']:
                latitud = float(match['latitud'])
                self.orientacionY = "S" if latitud < 0 else "N"
                
                restoM, grados = math.modf(abs(latitud))
                self.gradosY = int(grados)

                restoS, minutos = math.modf(restoM * 60.00)
                self.minutosY = int(minutos)

                self.segundosY = restoS * 60.00

                longitud = float(match['longitud'])
                self.orientacionX = "W" if longitud < 0 else "E"

                restoM, grados = math.modf(abs(longitud))
                self.gradosX = int(grados)

                restoS, minutos = math.modf(restoM * 60.00)
                self.minutosX = int(minutos)

                self.segundosX = restoS * 60.00
            if match['formato2']:
                self.gradosX = int(match['grados1'])
                self.minutosX = int(match['minutos1'])
                self.segundosX = float(match['segundos1'])
                self.orientacionX = match['orientacion1']
                self.gradosY = int(match['grados'])
                self.minutosY = int(match['minutos'])
                self.segundosY = float(match['segundos'])
                self.orientacionY = match['orientacion']
            if match['formato3']:
                self.gradosX = int(match['grados1'])
                self.minutosX = int(match['minutos1'])
                self.segundosX = float(match['segundos1'])
                self.orientacionX = match['orientacion1']
                self.gradosY = int(match['grados'])
                self.minutosY = int(match['minutos'])
                self.segundosY = float(match['segundos'])
                self.orientacionY = match['orientacion']
    """
    Precondicion: los atributos de la clase han de estar correctamente rellenados
    Efecto: Transforma los artributos de clase en el formato gps
    Resultado: Retorna una cadena con la coordenada en formato gps
    """
    def formato_gps(self):
        resto, modulo = math.modf(float(self.segundosY))
        resto = f'{resto:.4f}'
        latitud = f'{str(self.gradosY).zfill(3)}{str(self.minutosY).zfill(2)}{str(int(modulo)).zfill(2)}.{resto[2:]}{self.orientacionY.upper()}'
        resto, modulo = math.modf(float(self.segundosX))
        resto = f'{resto:.4f}'
        longitud = f'{str(self.gradosX).zfill(3)}{str(self.minutosX).zfill(2)}{str(int(modulo)).zfill(2)}.{resto[2:]}{self.orientacionX.upper()}'
        return f'{latitud}{longitud} ' 

    """
    Precondicion: coordenada ha de ser un objeto coordenada valido
    Efecto: Usando la formula de haversine calcula la distancia entre ambas coordenadas
    Resultado: Retorna la distancia entre ambas coordenadas en kilometros
    """
    def distancia_entre_coordenadas(self, coordenada):
        R = 6378
        latitud1 = float(self.gradosY + (self.minutosY + self.segundosY/60.00) / 60.00)
        latitud1 = latitud1 if self.orientacionY == "N" else -latitud1
        longitud1 = float(self.gradosX + (self.minutosX + self.segundosX/60.00) / 60.00)
        longitud1 = longitud1 if self.orientacionX == "E" else -longitud1

        latitud2 = float(coordenada.gradosY + (coordenada.minutosY + coordenada.segundosY/60.00) / 60.00)
        latitud2 = latitud2 if coordenada.orientacionY == "N" else -latitud2
        longitud2 = float(coordenada.gradosX + (coordenada.minutosX + coordenada.segundosX/60.00) / 60.00)
        longitud2 = longitud2 if coordenada.orientacionX == "E" else -longitud2 
        
        dif_lon = math.radians(longitud2 - longitud1)
        dif_lat = math.radians(latitud2 - latitud1)
        
        h = (math.sin(dif_lat/2) ** 2) + math.cos(math.radians(latitud1)) * math.cos(math.radians(latitud2)) * (math.sin(dif_lon/2) ** 2)
        d = 2 * R * math.asin(math.sqrt(h))
        
        return d

    """
    Precondicion: la coordenada ha de ser una cadena de texto con una coordenada en un formato valido
    Efecto: Comprueba si la coordenada es valida y cumple alguno de los formatos descritos
    Resultado: Retorna la validez de la coordenada
    """
    @staticmethod
    def coordenada_valida(coordenada):
        match = re_coordenadas.fullmatch(coordenada)
        if match:
            if match['formato1']:
                return abs(float(match['latitud'])) <= 90.00 and abs(float(match['longitud'])) <= 180.00
            if match['formato2'] or match['formato3']:
                return int(match['grados']) <= 90 and int(match['grados1']) <= 180 and int(match['minutos']) < 60 and int(match['minutos1']) < 60 and float(match['segundos']) < 60.00 and float(match['segundos1']) < 60.00
        return False
