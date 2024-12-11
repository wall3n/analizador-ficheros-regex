import regex
import math

er_formato1 = r"(?P<formato1>(?P<latitud>[\+\-]?\d{1,2}\.\d+)\s*,\s*(?P<longitud>[\+\-]?\d{1,3}\.\d+))\s*"
er_formato2 = r"(?P<formato2>(?P<latitud>(?P<grados>\d{1,2})°\s*(?P<minutos>\d{1,2})‘\s*(?P<segundos>\d{1,2}\.\d{4})\"\s+(?P<orientacion>[NS]),\s*)(?P<longitud>(?P<grados1>\d{1,2})°\s*(?P<minutos1>\d{1,2})‘\s*(?P<segundos1>\d{1,2}\.\d{4})\"\s+(?P<orientacion1>[WE])))\s*"
er_formato3 = r"(?P<formato3>(?P<latitud>(?P<grados>\d{3})(?P<minutos>\d{2})(?P<segundos>\d{2}\.\d{4})(?P<orientacion>[NS]))(?P<longitud>(?P<grados1>\d{3})(?P<minutos1>\d{2})(?P<segundos1>\d{2}\.\d{4})(?P<orientacion1>[WE])))\s*"
re_coordenadas = regex.compile(f'{er_formato1}|{er_formato2}|{er_formato3}')

# Latitud Y Longitud X

class Coordenadas:
    
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
                self.gradosX = match['grados1']
                self.minutosX = match['minutos1']
                self.segundosX = match['segundos1']
                self.orientacionX = match['orientacion1']
                self.gradosY = match['grados']
                self.minutosY = match['minutos']
                self.segundosY = match['segundos']
                self.orientacionY = match['orientacion']
            if match['formato3']:
                self.gradosX = match['grados1']
                self.minutosX = match['minutos1']
                self.segundosX = match['segundos1']
                self.orientacionX = match['orientacion1']
                self.gradosY = match['grados']
                self.minutosY = match['minutos']
                self.segundosY = match['segundos']
                self.orientacionY = match['orientacion']
    def formato_gps(self):
        resto, modulo = math.modf(float(self.segundosY))
        resto = f'{resto:.4f}'
        latitud = f'{str(self.gradosY).zfill(3)}{str(self.minutosY).zfill(2)}{str(int(modulo)).zfill(2)}.{resto[2:]}{self.orientacionY.upper()}'
        resto, modulo = math.modf(float(self.segundosX))
        resto = f'{resto:.4f}'
        longitud = f'{str(self.gradosX).zfill(3)}{str(self.minutosX).zfill(2)}{str(int(modulo)).zfill(2)}.{resto[2:]}{self.orientacionX.upper()}'
        return f'{latitud}{longitud} ' 
    @staticmethod
    def coordenada_valida(coordenada):
        match = re_coordenadas.fullmatch(coordenada)
        if match:
            if match['formato1']:
                return abs(float(match['latitud'])) <= 90.00 and abs(float(match['longitud'])) <= 180.00
            if match['formato2'] or match['formato3']:
                return int(match['grados']) <= 90 and int(match['grados1']) <= 180 and int(match['minutos']) < 60 and int(match['minutos1']) < 60 and float(match['segundos']) < 60.00 and float(match['segundos1']) < 60.00
        return False
