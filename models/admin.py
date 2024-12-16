from models.user import User


class Admin(User):
    """
    Clase que representa a un administrador en el sistema.
    """

    def get_role(self):
        """Devuelve el rol del usuario ("Admin")."""
        return "Admin"


    def get_info(self):
        """Devuelve información del administrador."""
        return super().get_info()

