from models.user import User


class Profesor(User):
    """
    Clase que representa a un profesor en el sistema.
    """

    def __init__(self, username, password, nombre, apellido, edad):
        super().__init__(username, password, nombre, apellido, edad)
        self.cursos = []  # Lista para almacenar los cursos asignados al profesor

    def get_role(self):
        """Devuelve el rol del usuario ("Profesor")."""
        return "Profesor"

    def agregar_curso(self, curso):
        """Agrega un curso a la lista de cursos del profesor."""
        if curso not in self.cursos:
            self.cursos.append(curso)
            return True
        return False

    def agregar_tarea_a_curso(self, curso, tarea):
        """Agrega una tarea a un curso específico del profesor."""
        if curso in self.cursos:
            curso.agregar_tarea(tarea)
            return True
        return False

    def get_cursos(self):
        """Devuelve una lista con los nombres de los cursos que imparte el profesor."""
        return [curso.get_nombre() for curso in self.cursos]

    def get_nombre_completo(self):
        """Devuelve el nombre completo del profesor."""
        return f"{self.nombre} {self.apellido}"

