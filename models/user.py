class User:
    """
    Clase base para representar un usuario en el sistema.
    """

    def __init__(self, username, password, nombre, apellido, edad):
        self.username = username
        self.password = password
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def get_role(self):
        """Devuelve el rol del usuario."""
        return "Usuario"

    def get_info(self):
        """Devuelve un diccionario con la información del usuario."""
        return {
            "username": self.username,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "role": self.get_role()
        }




