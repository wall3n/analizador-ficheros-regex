import regex

class DNI:
    er_dni1 = r"(?P<formato1>(?P<num>\d{8})(?P<letra>[A-Z]))"
    er_dni2 = r"(?P<formato2>(?P<letra>[A-Z])-(?P<num>\d{8}))"
    re_dni = regex.compile(f'{er_dni1}|{er_dni2}')
    def __init__(self):
        self.numero = ''
        self.letra = ''
        self.validado = False

    # Metodos de clase
    def validar_dni(self, cadena):
        if DNI.dni_valido(cadena):
            self.numero = m['numero']
            self.letra = m['letra']
            self.validado = True

    # Metodos de formato
    def formato1(self):
        return f'{self.numero}{self.letra}'
    def formato2(self):
        return f'{self.letra}-{self.numero}'

    # Metodos estáticos
    @staticmethod
    def letra_dni(nif):
        extrangeros = ['X', 'Y', 'Z']
        dni = nif
        if(nif[0] in extrangeros):
            dni = str(extrangeros.index(nif[0])) + nif[1:]
        letras = ['T','R','W','A','G','M','Y','F','P','D','X','B', 'N', 'J','Z','S','Q','V','H','L','C','K','E']
        res = int(dni) % 23
        return letras[res]

    # Rehacer
    @staticmethod
    def dni_valido(dni):
        match = re_dni.fullmatch(dni)
        return m and m['letra'] == DNI.letra_dni(m['num'])

