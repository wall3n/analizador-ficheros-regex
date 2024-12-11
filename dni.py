import regex

er_dni1 = r"(?P<formato1>(?P<num>\d{8})(?P<letra>[A-Z]))\s*"
er_dni2 = r"(?P<formato2>(?P<letra>[A-Z])-(?P<num>\d{8}))\s*"
re_dni = regex.compile(f'{er_dni1}|{er_dni2}')

class DNI:
    def __init__(self):
        self.numero = ''
        self.letra = ''
        self.validado = False

    # Metodos de clase
    def validar_dni(self, cadena):
        if DNI.dni_valido(cadena):
            self.validado = True

    # Metodos de formato
    def formato1(self):
        return f'{self.numero}{self.letra}'
    def formato2(self):
        return f'{self.letra}-{self.numero}'

    # Metodos estáticos
    @staticmethod
    def letra_dni(nif):
        extranjeros = ['X', 'Y', 'Z']
        dni = nif
        if(nif[0] in extranjeros):
            dni = str(extranjeros.index(nif[0])) + nif[1:]
        letras = ['T','R','W','A','G','M','Y','F','P','D','X','B', 'N', 'J','Z','S','Q','V','H','L','C','K','E']
        res = int(dni) % 23
        return letras[res]

    @staticmethod
    def dni_valido(dni):
        match = re_dni.fullmatch(dni)
        return match and match['letra'] == DNI.letra_dni(match['num'])

    @staticmethod
    def is_equal(dni1, dni2):
        m1 = re_dni.fullmatch(dni1)
        m2 = re_dni.fullmatch(dni2)
        return m1['num'] == m2['num'] and m1['letra'] == m2['letra']

