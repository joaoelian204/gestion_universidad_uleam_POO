from models.curso import Curso
from views.menu import UIPrinter


class AdminController:
    def __init__(self, usuarios, cursos=[]):
        self.usuarios = usuarios
        self.cursos = cursos

    def menu_admin(self, admin):
        """Muestra el menú principal para el administrador."""
        while True:
            UIPrinter().imprimir_banner_uleam()
            UIPrinter().imprimir_encabezado(f"Menú de Administrador - {admin['nombre']} {admin['apellido']}")
            UIPrinter().imprimir_menu([
                "Registrar Estudiante",
                "Registrar Profesor",
                "Crear Curso",
                "Listar Profesores",
                "Listar Estudiantes",
                "Listar Cursos",
                "Inscribir Estudiante en Curso",
            ])
            
            opcion = input("\nIngrese una opción: ")

            if opcion == "1":
                self.registrar_estudiante()
            elif opcion == "2":
                self.registrar_profesor()
            elif opcion == "3":
                self.crear_curso()
            elif opcion == "4":
                self.listar_profesores()
            elif opcion == "5":
                self.listar_estudiantes()
            elif opcion == "6":
                self.listar_cursos()
            elif opcion == "7":
                self.inscribir_curso()
            elif opcion == "0":
                break

    def registrar_estudiante(self):
        """Registra un nuevo estudiante."""
        username = input("Ingrese el nombre de usuario del estudiante: ")
        password = input("Ingrese la contraseña del estudiante: ")
        nombre = input("Ingrese el nombre del estudiante: ")
        apellido = input("Ingrese el apellido del estudiante: ")
        
        try:
            edad = int(input("Ingrese la edad del estudiante: "))
        except ValueError:
            UIPrinter().imprimir_error("Edad no válida. Debe ser un número entero.")
            return

        carrera = input("Ingrese la carrera del estudiante: ")

        estudiante = {
            "username": username,
            "password": password,
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "role": "Estudiante",
            "carrera": carrera
        }

        self.usuarios.append(estudiante)
        UIPrinter().imprimir_exito("Estudiante registrado con éxito.")

    def registrar_profesor(self):
        """Registra un nuevo profesor."""
        username = input("Ingrese el nombre de usuario del profesor: ")
        password = input("Ingrese la contraseña del profesor: ")
        nombre = input("Ingrese el nombre del profesor: ")
        apellido = input("Ingrese el apellido del profesor: ")

        try:
            edad = int(input("Ingrese la edad del profesor: "))
        except ValueError:
            UIPrinter().imprimir_error("Edad no válida. Debe ser un número entero.")
            return

        profesor = {
            "username": username,
            "password": password,
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "role": "Profesor"
        }

        self.usuarios.append(profesor)
        UIPrinter().imprimir_exito("Profesor registrado con éxito.")

    def crear_curso(self):
        """Crea un nuevo curso."""
        nombre_curso = input("Ingrese el nombre del curso: ")
        profesor_username = input("Ingrese el nombre de usuario del profesor: ")

        profesor = next((u for u in self.usuarios if u['username'] == profesor_username and u['role'] == 'Profesor'), None)
        if profesor:
            # Crear el curso como un objeto de la clase Curso
            curso = Curso(nombre_curso, profesor)
            self.cursos.append(curso)
            UIPrinter().imprimir_exito(f"Curso '{nombre_curso}' creado con éxito.")
        else:
            UIPrinter().imprimir_error("Profesor no encontrado.")

    def listar_profesores(self):
        """Lista todos los profesores."""
        profesores = [u for u in self.usuarios if u['role'] == 'Profesor']
        UIPrinter().imprimir_encabezado("Lista de Profesores")
        for profesor in profesores:
            print(f"{profesor['nombre']} {profesor['apellido']} (Username: {profesor['username']})")

    def listar_estudiantes(self):
        """Lista todos los estudiantes."""
        estudiantes = [u for u in self.usuarios if u['role'] == 'Estudiante']
        UIPrinter().imprimir_encabezado("Lista de Estudiantes")
        for estudiante in estudiantes:
            print(f"{estudiante['nombre']} {estudiante['apellido']} (Username: {estudiante['username']})")

    def listar_cursos(self):
        """Lista todos los cursos."""
        UIPrinter().imprimir_encabezado("Lista de Cursos")
        for curso in self.cursos:
            if isinstance(curso, Curso):
                print(f"{curso.get_nombre()} - Profesor: {curso.profesor['nombre']} {curso.profesor['apellido']}")
            else:
                UIPrinter().imprimir_error("Error: El curso no es una instancia de la clase Curso.")

    def inscribir_curso(self):
        """Inscribe a un estudiante en un curso."""
        self.listar_estudiantes()
        username_estudiante = input("\nIngrese el nombre de usuario del estudiante: ")
        estudiante = next((u for u in self.usuarios if u['username'] == username_estudiante and u['role'] == 'Estudiante'), None)

        if not estudiante:
            UIPrinter().imprimir_error("Estudiante no encontrado.")
            return

        UIPrinter().imprimir_encabezado("Lista de Cursos Disponibles")
        for idx, curso in enumerate(self.cursos, 1):
            if isinstance(curso, Curso):
                print(f"{idx}. {curso.get_nombre()}")
            else:
                UIPrinter().imprimir_error("Error: El curso no es una instancia válida.")

        try:
            opcion = int(input("\nIngrese el número del curso al que desea inscribirse: ")) - 1
            if 0 <= opcion < len(self.cursos):
                curso = self.cursos[opcion]
                if isinstance(curso, Curso):
                    if estudiante not in curso.estudiantes:
                        curso.agregar_estudiante(estudiante)
                        UIPrinter().imprimir_exito(f"El estudiante '{estudiante['nombre']}' se inscribió con éxito en el curso: {curso.get_nombre()}")
                    else:
                        UIPrinter().imprimir_error("El estudiante ya está inscrito en este curso.")
                else:
                    UIPrinter().imprimir_error("Error: Curso no válido.")
            else:
                UIPrinter().imprimir_error("Opción no válida.")
        except ValueError:
            UIPrinter().imprimir_error("Por favor, ingrese un número válido.")

        input("\nPresione Enter para continuar...")


