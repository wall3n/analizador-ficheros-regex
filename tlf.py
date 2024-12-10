import regex

tlf1 = r"(\d{3})\s(\d{3})\s(\d{3})"
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


