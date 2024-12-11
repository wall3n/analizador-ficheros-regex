import regex

tlf1 = r"(?P<formato1>(\d{3})\s(\d{3})\s(\d{3}))\s*"
tlf2 = r"(?P<formato2>\+(\d\s?){9,14}\d)\s*"
re_tlf = regex.compile(f'{tlf1}|{tlf2}')
PREFIJO_DEFAULT = "+34 "

class TLF:

    def __init__(self):
        self.tlf = ''
        self.validado = False

    def validar_tlf(self, cadena):
        if TLF.tlf_valido(cadena):
            m = re_tlf.fullmatch(cadena)
            if m['formato1']:
                self.tlf = PREFIJO_DEFAULT + m['formato1']
            if m['formato2']:
                self.tlf = m['formato2']
            self.validado = True

    @staticmethod
    def tlf_valido(tlf):
        match = re_tlf.fullmatch(tlf)
        if match:
            return True
        else:
            return False
    @staticmethod
    def is_equal(tlf1, tlf2):
        m1 = re_tlf.fullmatch(tlf1)
        m2 = re_tlf.fullmatch(tlf2)
        tl1 = m1['formato2'] if m1['formato2'] else PREFIJO_DEFAULT + m1['formato1']
        tl2 = m2['formato2'] if m2['formato2'] else PREFIJO_DEFAULT + m2['formato1']
        return tl1 == tl2


