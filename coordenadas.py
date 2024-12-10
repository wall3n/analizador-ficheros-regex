import regex

class Coordenadas:
    er_formato1 = r"(?P<formato1>(?P<latitud>[\+\-]?\d{1,2}\.\d+)\s*,\s*(?P<longitud>[\+\-]?\d{1,3}\.\d+))"
    er_formato2 = r"(?P<formato2>(?P<latitud>(?P<grados>\d{1,2})°\s*(?P<minutos>\d{1,2})‘\s*(?P<segundos>\d{1,2}\.\d{4})\"\s+(?P<orientacion>[NS]),\s*)(?P<longitud>(?P<grados1>\d{1,2})°\s*(?P<minutos1>\d{1,2})‘\s*(?P<segundos1>\d{1,2}\.\d{4})\"\s+(?P<orientacion1>[WE])))"
    er_formato3 = r"(?P<formato3>(?P<latitud>(?P<grados>\d{3})(?P<minutos>\d{2})(?P<segundos>\d{2}\.\d{4})(?P<orientacion>[NS]))(?P<longitud>(?P<grados1>\d{3})(?P<minutos1>\d{2})(?P<segundos1>\d{2}\.\d{4})(?P<orientacion1>[WE])))"
    re_coordenadas = regex.compile(f'{er_formato1}|{er_formato2}|{er_formato3}')
    
    def __init__(self):
        self.latitud = 0.0000
        self.longitud = 0.0000
        self.validado = False

    @staticmethod
    def coordenada_valida(coordenada):
        match = re_coordenadas.fullmatch(coordenada)
        if match:
            if match['formato1']:
                return abs(match['latitud']) <= 90.00 and abs(match['longitud']) <= 180.00
            if match['formato2'] or match['formato3']:
                return match['grados'] <= 90 and match['grados1'] <= 180 and match['minutos'] < 60 and match['minutos1'] < 60 and match['segundos'] < 60.00 and match['segundos1'] < 60.00
        return False
