# Sistema de Gestión Universitaria

Este proyecto es una aplicación de consola para gestionar una universidad, permitiendo a administradores, profesores y estudiantes interactuar con el sistema según sus roles.

---

## 📋 **Descripción General**

La aplicación sigue el patrón de arquitectura **MVC (Modelo-Vista-Controlador)** y hace uso de los principios **SOLID** y varios **Patrones de Diseño** para garantizar un código limpio, modular y mantenible.

---

## 🚀 **Características Principales**

- **Administrador**:
  - Registrar estudiantes.
  - Registrar profesores.
  - Crear cursos.
  - Listar profesores, estudiantes y cursos.
  - Inscribir estudiantes en cursos.

- **Profesor**:
  - Ver los cursos que imparte.
  - Crear tareas para sus cursos.
  - Listar estudiantes inscritos en sus cursos.

- **Estudiante**:
  - Ver sus cursos.
  - Inscribirse en cursos.
  - Ver tareas asignadas a sus cursos.

---

## 🛠️ **Tecnologías Utilizadas**

- **Lenguaje**: Python 3
- **Bibliotecas**:
  - `colorama`: Para darle color a la salida en la consola.

---

## 🏗️ **Arquitectura del Proyecto**

El proyecto sigue una estructura **MVC**:

```
POO/
│
├── controllers/
│   ├── __init__.py
│   ├── admin_controller.py
│   ├── estudiante_controller.py
│   └── profesor_controller.py
│
├── models/
│   ├── __init__.py
│   ├── admin.py
│   ├── curso.py
│   ├── estudiante.py
│   ├── profesor.py
│   └── user.py
│
├── views/
│   ├── __init__.py
│   └── menu.py
│
├── login_strategies.py
├── main_controller.py
└── main.py
```

---

## 📐 **Principios SOLID Aplicados**

1. **Single Responsibility Principle (SRP)**:
   - Cada clase tiene una única responsabilidad (por ejemplo, `AdminController` maneja únicamente las funciones del administrador).

2. **Dependency Inversion Principle (DIP)**:
   - `MainController` depende de abstracciones (`LoginStrategy`) en lugar de implementaciones concretas.

---

## 🧩 **Patrones de Diseño Implementados**

1. **Singleton**:
   - `UIPrinter` asegura que solo existe una instancia para manejar las impresiones en consola.

2. **Decorator**:
   - Se utiliza un decorador para agregar bordes decorativos a los métodos `imprimir_exito` e `imprimir_error` de `UIPrinter`.

3. **Strategy**:
   - Se usa el patrón Strategy para manejar el inicio de sesión de diferentes roles (`Admin`, `Profesor`, `Estudiante`).

---

## 🚦 **Instrucciones de Ejecución**

1. **Instalar Dependencias**:

   ```bash
   pip install colorama
   ```

2. **Ejecutar el Programa**:

   ```bash
   python main.py
   ```

---

## 📄 **Ejemplo de Uso**

### **Inicio de Sesión**

1. Ejecuta el programa y selecciona **"Iniciar sesión"**.
2. Ingresa un nombre de usuario y una contraseña.

### **Usuarios de Prueba**

- **Administrador**:  
  - Usuario: `admin`  
  - Contraseña: `admin123`

- **Profesor**:  
  - Usuario: `prof1`  
  - Contraseña: `prof123`

- **Estudiante**:  
  - Usuario: `est1`  
  - Contraseña: `est123`

---

