class Curso:
    """
    Clase que representa un curso en el sistema.
    """

    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor  # Se espera que sea un diccionario o un objeto con 'nombre' y 'apellido'
        self.estudiantes = []     # Se espera que sean objetos con 'nombre' y 'apellido'
        self.tareas = []          # Se espera que sean diccionarios con 'nombre'

    def agregar_estudiante(self, estudiante):
        """Agrega un estudiante al curso si no está ya inscrito."""
        if estudiante not in self.estudiantes:
            self.estudiantes.append(estudiante)
            return True
        return False

    def agregar_tarea(self, tarea):
        """Agrega una tarea al curso."""
        if isinstance(tarea, dict) and 'nombre' in tarea:
            self.tareas.append(tarea)
            return True
        return False
    
    def get_nombre(self):
        """Devuelve el nombre del curso."""
        return self.nombre
    
    def get_profesor(self):
        """Devuelve el nombre completo del profesor del curso."""
        if isinstance(self.profesor, dict):
            return f"{self.profesor.get('nombre', 'Desconocido')} {self.profesor.get('apellido', 'Desconocido')}"
        return "Profesor desconocido"
    
    def get_estudiantes(self):
        """Devuelve una lista con los nombres completos de los estudiantes inscritos en el curso."""
        return [f"{estudiante.get('nombre', 'Desconocido')} {estudiante.get('apellido', 'Desconocido')}" for estudiante in self.estudiantes]
    
    def get_tareas(self):
        """Devuelve una lista con los nombres de las tareas del curso."""
        return [tarea.get('nombre', 'Tarea sin nombre') for tarea in self.tareas]

    def get_info(self):
        """Devuelve la información del curso en forma de diccionario."""
        return {
            "nombre": self.nombre,
            "profesor": self.get_profesor(),
            "num_estudiantes": len(self.estudiantes),
            "num_tareas": len(self.tareas)
        }

