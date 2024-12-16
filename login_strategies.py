class LoginStrategy:
    """Clase base para estrategias de inicio de sesión."""
    def login(self, user, controller):
        """Método abstracto que debe ser implementado por las subclases."""
        pass


class AdminLoginStrategy(LoginStrategy):
    """Estrategia de inicio de sesión para administradores."""
    def login(self, user, controller):
        controller.admin_controller.menu_admin(user)


class ProfesorLoginStrategy(LoginStrategy):
    """Estrategia de inicio de sesión para profesores."""
    def login(self, user, controller):
        controller.profesor_controller.menu_profesor(user)


class EstudianteLoginStrategy(LoginStrategy):
    """Estrategia de inicio de sesión para estudiantes."""
    def login(self, user, controller):
        controller.estudiante_controller.menu_estudiante(user)


# Ejemplo de una posible estrategia adicional para futuros roles
class BibliotecarioLoginStrategy(LoginStrategy):
    """Estrategia de inicio de sesión para bibliotecarios."""
    def login(self, user, controller):
        controller.bibliotecario_controller.menu_bibliotecario(user)


