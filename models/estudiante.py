from models.user import User


class Estudiante(User):
    """
    Clase que representa a un estudiante en el sistema.
    """

    def __init__(self, username, password, nombre, apellido, edad, carrera):
        super().__init__(username, password, nombre, apellido, edad)
        self.carrera = carrera
        self.cursos = []  # Se espera que los cursos sean objetos de la clase Curso

    def get_role(self):
        """Devuelve el rol del usuario ("Estudiante")."""
        return "Estudiante"

    def get_nombre_completo(self):
        """Devuelve el nombre completo del estudiante."""
        return f"{self.nombre} {self.apellido}"

    def get_carrera(self):
        """Devuelve la carrera del estudiante."""
        return self.carrera

    def get_curso(self, nombre_curso):
        """Devuelve el curso con el nombre indicado."""
        for curso in self.cursos:
            if curso.get_nombre() == nombre_curso:
                return curso
        return None

    def inscribir_curso(self, curso):
        """Inscribe al estudiante en un curso."""
        if curso not in self.cursos:
            self.cursos.append(curso)
            curso.agregar_estudiante(self)
            return True
        return False

    def get_cursos(self):
        """Devuelve una lista con los nombres de los cursos en los que está inscrito."""
        return [curso.get_nombre() for curso in self.cursos]

