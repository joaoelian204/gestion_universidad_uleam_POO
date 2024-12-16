from controllers.admin_controller import AdminController
from controllers.estudiante_controller import EstudianteController
from controllers.profesor_controller import ProfesorController

# Importar las estrategias desde login_strategies.py
from login_strategies import (
    AdminLoginStrategy,
    EstudianteLoginStrategy,
    ProfesorLoginStrategy,
)
from views.menu import UIPrinter


class MainController:
    def __init__(self, usuarios, cursos):
        # Listas compartidas para almacenar usuarios y cursos
        self.usuarios = usuarios
        self.cursos = cursos
        
        # Instanciar los controladores
        self.admin_controller = AdminController(self.usuarios, self.cursos)
        self.profesor_controller = ProfesorController(self.cursos)
        self.estudiante_controller = EstudianteController(self.cursos)

        # Configurar las estrategias de inicio de sesión
        self.strategies = {
            "Admin": AdminLoginStrategy(),
            "Profesor": ProfesorLoginStrategy(),
            "Estudiante": EstudianteLoginStrategy()
        }

    def crear_usuarios_prueba(self):
        """Crea usuarios de prueba si no existen."""
        usuarios_prueba = [
            {"username": "admin", "password": "admin123", "nombre": "Admin", "apellido": "Principal", "edad": 30, "role": "Admin"},
            {"username": "prof1", "password": "prof123", "nombre": "Juan", "apellido": "Perez", "edad": 40, "role": "Profesor"},
            {"username": "est1", "password": "est123", "nombre": "María", "apellido": "García", "edad": 20, "role": "Estudiante", "carrera": "Ingeniería"},
        ]

        for usuario in usuarios_prueba:
            if not any(u['username'] == usuario['username'] for u in self.usuarios):
                self.usuarios.append(usuario)
                UIPrinter().imprimir_exito(f"Usuario '{usuario['username']}' creado con éxito.")
            else:
                UIPrinter().imprimir_error(f"Usuario '{usuario['username']}' ya existe.")

    def main(self):
        """Función principal que maneja el flujo del programa."""
        self.crear_usuarios_prueba()
        while True:
            UIPrinter().imprimir_banner_uleam()
            UIPrinter().imprimir_encabezado("Bienvenido al sistema de la Universidad ULEAM")
            UIPrinter().imprimir_menu(["Iniciar sesión"])

            opcion = self.validar_entero("\nIngrese la opción: ", (0, 1))

            if opcion == 1:
                self.iniciar_sesion()
            elif opcion == 0:
                UIPrinter().imprimir_encabezado("Gracias por usar el sistema. ¡Hasta pronto!")
                break

    def iniciar_sesion(self):
        """Inicia sesión para los diferentes tipos de usuarios."""
        username = self.validar_cadena("Ingrese su nombre de usuario: ").lower()
        password = self.validar_cadena("Ingrese su contraseña: ")

        user = next((u for u in self.usuarios if u['username'] == username), None)

        if user and user['password'] == password:
            UIPrinter().imprimir_exito("\nInicio de sesión exitoso.")
            role = user['role']
            strategy = self.strategies.get(role)
            if strategy:
                strategy.login(user, self)
            else:
                UIPrinter().imprimir_error("Rol no reconocido.")
        else:
            UIPrinter().imprimir_error("Usuario o contraseña incorrectos.")

    def validar_entero(self, prompt, rango=None, permitir_vacio=False):
        """Valida una entrada de tipo entero."""
        while True:
            entrada = input(prompt).strip()
            if entrada.isdigit() and (rango is None or int(entrada) in range(rango[0], rango[1] + 1)):
                return int(entrada)
            elif permitir_vacio and entrada == "":
                return None
            else:
                UIPrinter().imprimir_error("Por favor, ingrese un número válido.")

    def validar_cadena(self, prompt, rango=None, permitir_vacio=False):
        """Valida una entrada de tipo cadena de texto."""
        while True:
            entrada = input(prompt).strip()
            if rango and not (rango[0] <= len(entrada) <= rango[1]):
                UIPrinter().imprimir_error(f"Por favor, ingrese un texto de {rango[0]} a {rango[1]} caracteres.")
            elif permitir_vacio and entrada == "":
                return None
            else:
                return entrada


if __name__ == "__main__":
    usuarios = []
    cursos = []
    main_controller = MainController(usuarios, cursos)
    main_controller.main()




