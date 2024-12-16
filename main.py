from main_controller import MainController


def init_data():
    """Inicializa los datos de prueba."""
    usuarios = [
        {"username": "admin", "password": "admin123", "nombre": "Admin", "apellido": "Principal", "edad": 35, "role": "Admin"},
        {"username": "prof1", "password": "prof123", "nombre": "Juan", "apellido": "Perez", "edad": 40, "role": "Profesor"},
        {"username": "est1", "password": "est123", "nombre": "María", "apellido": "García", "edad": 20, "role": "Estudiante", "carrera": "Ingeniería"},
    ]
    cursos = []

    print("Datos de prueba inicializados con éxito.")
    return usuarios, cursos

def main():
    """Función principal para ejecutar el controlador principal."""
    usuarios, cursos = init_data()
    main_controller = MainController(usuarios, cursos)
    main_controller.main()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error durante la ejecución del programa: {e}")
