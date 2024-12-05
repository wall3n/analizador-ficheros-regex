import regex

class FechaYHora:

    f_formato1 = r"(?P<formato1>(?P<ano>\d{4})-(?P<mes>\d{2})-(?P<dia>\d{2})\s(?P<hora>\d{2}):(?P<minutos>\d{2}))"
    f_formato2 = r"(?P<formato2>(?P<mes>[A-Z][a-z]+)\s(?P<dia>\d{1,2}),\s(?P<ano>\d{1,4})\s(?P<hora>\d{1,2}):(?P<minutos>\d{2})\s(?P<franja>AM|PM))"
    f_formato3 = r"(?P<formato3>(?P<hora>\d{2}):(?P<minutos>\d{2}):(?P<segundos>\d{2})\s(?P<dia>\d{2})/(?P<mes>\d{2})/(?P<ano>\d{4}))"
    er_tiempo = regex.compile(f'{f_formato1}|{f_formato2}|{f_formato3}')

    def __init__(self):
        self.año = 0
        self.mes = 1
        self.dia = 1
        self.hora = 0
        self.minutos = 0
        self.segundos = 0
        self.validada = False

    def validar_fecha(self, cadena):
        match = er_tiempo.fullmatch(cadena)
        if match:
            if match['formato1']:
                if FechaYHora.fecha_correcta(match['ano'], match['mes'], match['dia']) and FechaYHora.hora_correcta(match['hora'], match['minutos'], self.segundos):
                    self.año = match['ano']
                    self.mes = match['mes']
                    self.dia = match['dia']
                    self.hora = match['hora']
                    self.minutos = match['minutos']
                    self.validada = True

            if match['formato2']:
                if match['franja'] == "PM":
                    match['hora'] += 12
                match['mes'] = FechaYHora.transformar_mes_int(match['mes'])

                if FechaYHora.fecha_correcta(match['ano'], match['mes'], match['dia']) and FechaYHora.hora_correcta(match['hora'], match['minutos'], self.segundos):
                    self.año = match['ano']
                    self.mes = match['mes']
                    self.dia = match['dia']
                    self.hora = match['hora']
                    self.minutos = match['minutos']
                    self.validada = True
                    
            if match['formato3']:
                if FechaYHora.fecha_correcta(match['ano'], match['mes'], match['dia']) and FechaYHora.hora_correcta(match['hora'], match['minutos'], match['segundos']):
                    self.año = match['ano']
                    self.mes = match['mes']
                    self.dia = match['dia']
                    self.hora = match['hora']
                    self.minutos = match['minutos']
                    self.validada = True

    @staticmethod
    def es_bisiesto(año):
        return año % 4 == 0 and (not(año % 100 == 0) or año % 400 == 0)
    @staticmethod
    def fecha_correcta(año, mes, dia):
        if(año < 0):
            return False
        if(mes < 0 or 12 < mes):
            return False
        if(dia <= 0):
            return False
        if(mes in [1, 3, 5, 7, 8, 10, 12] and 31 < dia):
            return False
        if(mes not in [1, 3, 5, 7, 8, 10, 12] and 30 < dia and mes != 2):
            return False
        if(mes == 2 and not FechaYHora.es_bisiesto(año) and 28 < dia):
            return False
        if(mes == 2 and FechaYHora.es_bisiesto(año) and 29 < dia):
            return False
        return True

    @staticmethod
    def hora_correcta(hora,minuto,segundo):
        if(hora < 0 or 24 < hora):
            return False
        if(minuto < 0 or not (minuto < 60)):
            return False
        if(segundo < 0 or not (segundo < 60)):
            return False
        return True

    @staticmethod
    def transformar_mes_int(mes):
        meses = ["january", "february", "march", "april", "june", "july", "august", "september", "november", "december"]
        return meses.index(str(mes).lower()) + 1 

    @staticmethod
    def compara_fechas(año1,mes1,dia1,hora1,min1,seg1,año2,mes2,dia2,hora2,min2,seg2):
        if(año1 < año2):
            return -1
        elif(año2 < año1):
            return 1
        else:
            if(mes1 < mes2):
                return -1
            elif(mes2 < mes1):
                return 1
            else:
                if(dia1 < dia2):
                    return -1
                elif(dia2 < dia1):
                    return 1
                else:
                    if(hora1 < hora2):
                        return -1
                    elif(hora2 < hora1):
                        return 1
                    else:
                        if(min1 < min2):
                            return -1
                        elif(min2 < min1):
                            return 1
                        else:
                            if(seg1 < seg2):
                                return -1
                            elif(seg2 < seg1):
                                return 1
                            else:
                                return 0
