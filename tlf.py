import regex

tlf1 = r"(\d{3})\s(\d{3})\s(\d{3})\s*"
re_tlf = regex.compile(tlf1)

class TLF:

    def __init__(self):
        self.tlf = ''
        self.validado = False

    def validar_tlf(self, cadena):
        if TLF.tlf_valido(cadena):
            self.tlf = cadena
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
        return m1[1] == m2[1] and m1[2] == m2[2] and m1[3] == m2[3]


