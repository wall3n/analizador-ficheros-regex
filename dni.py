import regex

er_dni1 = r"(?P<formato1>(?P<num>\d{8})(?P<letra>[A-Z]))\s*"
er_dni2 = r"(?P<formato2>(?P<letra>[A-Z])-(?P<num>\d{8}))\s*"
re_dni = regex.compile(f'{er_dni1}|{er_dni2}')

class DNI:
    """
    Clase que representa y valida DNI's
    """

    def __init__(self):
        self.numero = ''
        self.letra = ''
        self.validado = False

    """
    Precondicion: cadena ha de ser un nif valido
    Efecto: Valida la cadena y la almacena
    Resultado: No retorna nada
    """
    def validar_dni(self, cadena):
        if DNI.dni_valido(cadena):
            self.validado = True

    def formato1(self):
        return f'{self.numero}{self.letra}'
    def formato2(self):
        return f'{self.letra}-{self.numero}'

    """
    Precondicion: nif ha de ser una cadena de texto que contenga un dni valido
    Efecto: Calcula la letra correspondiente a un nif valido
    Resultado: Retorna la letra correspondiente al nif
    """
    @staticmethod
    def letra_dni(nif):
        extranjeros = ['X', 'Y', 'Z']
        dni = nif
        if(nif[0] in extranjeros):
            dni = str(extranjeros.index(nif[0])) + nif[1:]
        letras = ['T','R','W','A','G','M','Y','F','P','D','X','B', 'N', 'J','Z','S','Q','V','H','L','C','K','E']
        res = int(dni) % 23
        return letras[res]

    """
    Precondicion: dni ha de ser una cadena de texto qeu contenga un nif valido
    Efecto: Valida el nif
    Resultado: Devuelve la validez del nif
    """
    @staticmethod
    def dni_valido(dni):
        match = re_dni.fullmatch(dni)
        return match and match['letra'] == DNI.letra_dni(match['num'])

    """
    Precondicion: dn1 y dni2 han de ser cadenas de texto que contengan nif validos
    Efecto: Comprueba las dos cadenas y comprueba su igualdad
    Resultado: retorna la igualdad de los nif
    """
    @staticmethod
    def is_equal(dni1, dni2):
        m1 = re_dni.fullmatch(dni1)
        m2 = re_dni.fullmatch(dni2)
        return m1['num'] == m2['num'] and m1['letra'] == m2['letra']

