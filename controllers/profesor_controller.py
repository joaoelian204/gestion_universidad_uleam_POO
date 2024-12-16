from views.menu import UIPrinter


class ProfesorController:
    """Controlador para gestionar las acciones del profesor."""

    def __init__(self, cursos=[]):
        self.cursos = cursos

    def menu_profesor(self, profesor):
        """Muestra el menú principal para el profesor."""
        while True:
            UIPrinter().imprimir_banner_uleam()
            UIPrinter().imprimir_encabezado(f"Menú de Profesor - {profesor['nombre']} {profesor['apellido']}")
            UIPrinter().imprimir_menu([
                "Ver mis cursos",
                "Crear tarea",
                "Listar estudiantes de un curso",
            ])

            opcion = input("\nIngrese una opción: ")

            if opcion == "1":
                self.mostrar_cursos_profesor(profesor)
            elif opcion == "2":
                self.crear_tarea(profesor)
            elif opcion == "3":
                self.listar_estudiantes_curso(profesor)
            elif opcion == "0":
                break
            else:
                UIPrinter().imprimir_error("Opción no válida. Intente de nuevo.")

    def mostrar_cursos_profesor(self, profesor):
        """Muestra los cursos que imparte el profesor."""
        cursos_profesor = [curso for curso in self.cursos if curso.profesor == profesor]

        if cursos_profesor:
            UIPrinter().imprimir_encabezado("Cursos que impartes")
            for curso in cursos_profesor:
                print(f"- {curso.get_nombre()}")
        else:
            UIPrinter().imprimir_error("No impartes ningún curso actualmente.")
        input("\nPresione Enter para continuar...")

    def crear_tarea(self, profesor):
        """Crea una nueva tarea para un curso específico."""
        UIPrinter().imprimir_encabezado("Crear Tarea para un Curso")
        cursos_profesor = [curso for curso in self.cursos if curso.profesor == profesor]

        if not cursos_profesor:
            UIPrinter().imprimir_error("No impartes ningún curso actualmente.")
            input("\nPresione Enter para continuar...")
            return

        for idx, curso in enumerate(cursos_profesor, 1):
            print(f"{idx}. {curso.get_nombre()}")

        try:
            opcion = int(input("\nIngrese el número del curso: ")) - 1
            if 0 <= opcion < len(cursos_profesor):
                descripcion_tarea = input("Ingrese la descripción de la tarea: ")
                cursos_profesor[opcion].agregar_tarea({"nombre": descripcion_tarea})
                UIPrinter().imprimir_exito("Tarea creada con éxito.")
            else:
                UIPrinter().imprimir_error("Opción no válida.")
        except ValueError:
            UIPrinter().imprimir_error("Por favor, ingrese un número válido.")
        
        input("\nPresione Enter para continuar...")

    def listar_estudiantes_curso(self, profesor):
        """Lista los estudiantes inscritos en un curso específico del profesor."""
        UIPrinter().imprimir_encabezado("Listar Estudiantes de un Curso")
        cursos_profesor = [curso for curso in self.cursos if curso.profesor == profesor]

        if not cursos_profesor:
            UIPrinter().imprimir_error("No impartes ningún curso actualmente.")
            input("\nPresione Enter para continuar...")
            return

        for idx, curso in enumerate(cursos_profesor, 1):
            print(f"{idx}. {curso.get_nombre()}")

        try:
            opcion = int(input("\nIngrese el número del curso: ")) - 1
            if 0 <= opcion < len(cursos_profesor):
                estudiantes = cursos_profesor[opcion].get_estudiantes()
                if estudiantes:
                    UIPrinter().imprimir_encabezado(f"Estudiantes en el curso '{cursos_profesor[opcion].get_nombre()}'")
                    for estudiante in estudiantes:
                        print(f"- {estudiante}")
                else:
                    UIPrinter().imprimir_error("No hay estudiantes inscritos en este curso.")
            else:
                UIPrinter().imprimir_error("Opción no válida.")
        except ValueError:
            UIPrinter().imprimir_error("Por favor, ingrese un número válido.")

        input("\nPresione Enter para continuar...")


