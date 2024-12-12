import regex

er_nombre = r"\p{L}+\s*"
er_precio = r"(\d+[,\.]?\d*€)\s*"
re_nombre = regex.compile(er_nombre)
re_precio = regex.compile(er_precio)

class Producto:
    """
    Clase estática para validar el nombre y el producto
    """

    """
    Precondición: producto ha de ser una cadena que cumpla el formato descrito en la expresión regular
    Efecto: Calcula la validez de la cadena
    Resultado: Devuelve el valor de la comprobación de la validez de la cadena
    """
    @staticmethod
    def validar_nombre_producto(producto):
        match = re_nombre.fullmatch(producto)
        return True if match else False

    """
    Precondición: precio ha de ser una cadena que cumpla el formato descrito en la expresión regular
    Efecto: Calcula la validez de la cadena
    Resultado: Devuelve el valor de la comprobación de la validez de la cadena
    """
    @staticmethod
    def validar_precio(precio):
        match = re_precio.fullmatch(precio)
        return True if match else False
