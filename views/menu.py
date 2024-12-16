from colorama import Fore, Style


def decorador_con_borde(func):
    def wrapper(*args, **kwargs):
        print("=" * 50)
        func(*args, **kwargs)
        print("=" * 50)
    return wrapper

class UIPrinter:
    """Clase para manejar impresiones visuales de menús y banners."""
    
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UIPrinter, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def imprimir_banner_uleam():
        """Imprime un banner de bienvenida."""
        banner = f"""{Fore.CYAN}
 _    _ _      ______          __  __ 
| |  | | |    |  ____|   /\   |  \/  |
| |  | | |    | |__     /  \  | \  / |
| |  | | |    |  __|   / /\ \ | |\/| |
| |__| | |____| |____ / ____ \| |  | |
 \____/|______|______/_/    \_\_|  |_|

Universidad Laica Eloy Alfaro de Manabí
{Style.RESET_ALL}"""
        print(banner)

    @staticmethod
    def imprimir_encabezado(texto):
        """Imprime un encabezado con formato decorativo."""
        print("\n" + "=" * 50)
        print(f"{texto:^50}")
        print("=" * 50)

    @staticmethod
    def imprimir_menu(opciones):
        """Imprime un menú de opciones numeradas."""
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion}")
        print("0. Salir")

    @staticmethod
    @decorador_con_borde
    def imprimir_error(mensaje):
        """Imprime un mensaje de error en color rojo."""
        print(f"{Fore.RED}{mensaje}{Style.RESET_ALL}")

    @staticmethod
    @decorador_con_borde
    def imprimir_exito(mensaje):
        """Imprime un mensaje de éxito en color verde."""
        print(f"{Fore.GREEN}{mensaje}{Style.RESET_ALL}")
