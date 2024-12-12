import regex

tlf1 = r"(?P<formato1>(\d{3})\s(\d{3})\s(\d{3}))\s*"
tlf2 = r"(?P<formato2>\+(\d\s?){9,14}\d)\s*"
re_tlf = regex.compile(f'{tlf1}|{tlf2}')
PREFIJO_DEFAULT = "+34 "

class TLF:
    """
    Clase que representa los números de telefono, los valida y compara
    """

    """
    Precondición: tlf debe de ser una cadena que contenga un número de teléfono en los formatos descritos por la expresión regular
    Efecto: Se comprueba la validez del telefono
    Resultado: Devuelve la validez del telefono
    """
    @staticmethod
    def tlf_valido(tlf):
        match = re_tlf.fullmatch(tlf)
        return True if match else False

    """
    Precondición: tlf1 y tlf2 deben de ser cadenas que contengan números de teléfono en los formatos descritos por la expresión regular
    Efecto: Si los telefonos son válidos se normalizan al formato internacional y se comparan
    Resultado: Devuelve el resultado de la comparación booleana de ambos telefonos
    """
    @staticmethod
    def is_equal(tlf1, tlf2):
        m1 = re_tlf.fullmatch(tlf1)
        m2 = re_tlf.fullmatch(tlf2)
        if not m1 or not m2:
            return False
        tl1 = m1['formato2'] if m1['formato2'] else PREFIJO_DEFAULT + m1['formato1']
        tl2 = m2['formato2'] if m2['formato2'] else PREFIJO_DEFAULT + m2['formato1']
        return tl1 == tl2


