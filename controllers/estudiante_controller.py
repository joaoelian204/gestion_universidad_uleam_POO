from models.curso import (
    Curso,  # Asegúrate de importar la clase Curso si no está ya importada
)
from views.menu import UIPrinter


class EstudianteController:
    """Controlador para gestionar las acciones del estudiante."""

    def __init__(self, cursos=[], tareas=[]):
        self.cursos = cursos
        self.tareas = tareas

    def menu_estudiante(self, estudiante):
        """Muestra el menú principal para el estudiante."""
        while True:
            UIPrinter().imprimir_banner_uleam()
            UIPrinter().imprimir_encabezado(f"Menú de Estudiante - {estudiante['nombre']} {estudiante['apellido']}")
            UIPrinter().imprimir_menu([
                "Ver mis cursos",
                "Inscribirse en un curso",
                "Ver tareas de un curso",
            ])

            opcion = input("\nIngrese una opción: ")

            if opcion == "1":
                self.mostrar_cursos_estudiante(estudiante)
            elif opcion == "2":
                self.inscribir_curso(estudiante)
            elif opcion == "3":
                self.ver_tareas_curso(estudiante)
            elif opcion == "0":
                break
            else:
                UIPrinter().imprimir_error("Opción no válida. Intente de nuevo.")

    def mostrar_cursos_estudiante(self, estudiante):
        """Muestra los cursos en los que está inscrito el estudiante."""
        cursos_inscritos = [curso for curso in self.cursos if estudiante in curso.estudiantes]

        if cursos_inscritos:
            UIPrinter().imprimir_encabezado("Cursos en los que estás inscrito")
            for curso in cursos_inscritos:
                print(f"- {curso.get_nombre()}")
        else:
            UIPrinter().imprimir_error("No estás inscrito en ningún curso actualmente.")
        input("\nPresione Enter para continuar...")

    def inscribir_curso(self, estudiante):
        """Inscribe al estudiante en un curso."""
        UIPrinter().imprimir_encabezado("Lista de Cursos Disponibles")
        cursos_disponibles = [curso for curso in self.cursos if isinstance(curso, Curso)]

        if not cursos_disponibles:
            UIPrinter().imprimir_error("No hay cursos disponibles para inscribirse.")
            input("\nPresione Enter para continuar...")
            return

        for idx, curso in enumerate(cursos_disponibles, 1):
            print(f"{idx}. {curso.get_nombre()}")

        try:
            opcion = int(input("\nIngrese el número del curso al que desea inscribirse: ")) - 1
            if 0 <= opcion < len(cursos_disponibles):
                curso = cursos_disponibles[opcion]
                if estudiante not in curso.estudiantes:
                    curso.agregar_estudiante(estudiante)
                    UIPrinter().imprimir_exito(f"Te has inscrito con éxito en el curso: {curso.get_nombre()}")
                else:
                    UIPrinter().imprimir_error("Ya estás inscrito en este curso.")
            else:
                UIPrinter().imprimir_error("Opción no válida.")
        except ValueError:
            UIPrinter().imprimir_error("Por favor, ingrese un número válido.")
        
        input("\nPresione Enter para continuar...")

    def ver_tareas_curso(self, estudiante):
        """Muestra las tareas de un curso específico para el estudiante."""
        cursos_inscritos = [curso for curso in self.cursos if estudiante in curso.estudiantes]

        if not cursos_inscritos:
            UIPrinter().imprimir_error("No estás inscrito en ningún curso actualmente.")
            input("\nPresione Enter para continuar...")
            return

        for idx, curso in enumerate(cursos_inscritos, 1):
            print(f"{idx}. {curso.get_nombre()}")

        try:
            opcion = int(input("\nIngrese el número del curso para ver sus tareas: ")) - 1
            if 0 <= opcion < len(cursos_inscritos):
                tareas = cursos_inscritos[opcion].get_tareas()
                if tareas:
                    UIPrinter().imprimir_encabezado(f"Tareas del curso '{cursos_inscritos[opcion].get_nombre()}'")
                    for tarea in tareas:
                        print(f"- {tarea}")
                else:
                    UIPrinter().imprimir_error("No hay tareas asignadas en este curso.")
            else:
                UIPrinter().imprimir_error("Opción no válida.")
        except ValueError:
            UIPrinter().imprimir_error("Por favor, ingrese un número válido.")
        
        input("\nPresione Enter para continuar...")




