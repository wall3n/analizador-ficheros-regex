import regex

er_nombre = r"\p{L}+"
er_precio = r"\d+,?\d*€"
re_nombre = regex.compile(er_nombre)
re_precio = regex.compile(er_precio)

class Producto:

    @staticmethod
    def validar_nombre_producto(producto):
        match = re_nombre.fullmatch(producto)
        if match:
            return True
        else:
            return False 

    @staticmethod
    def validar_precio(precio):
        match = re_precio.fullmatch(precio)
        if match: 
            return True
        else:
            return False
