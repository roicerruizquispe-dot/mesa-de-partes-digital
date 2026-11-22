# main.py - Programa principal y menú (Figura 1).
# Mesa de partes digital - I.E. Andrés Avelino Cáceres (Baños del Inca, Cajamarca)
# Alternativa A: arreglos paralelos, archivo de texto con "|", búsqueda secuencial y selección.
from . import datos
from .validacion import pedir_entero
from .archivo import cargar_archivo, guardar_archivo
from .expedientes import registrar_tramite, buscar_expediente
from .ordenamiento import ordenar_seleccion
from .reportes import mostrar_reporte


def main():
    cargar_archivo()
    print("Expedientes cargados desde el archivo:", datos.cantidad())
    opcion = 0
    try:
        while opcion != 4:
            print("\n========== MESA DE PARTES DIGITAL ==========")
            print("1. Registrar trámite")
            print("2. Buscar expediente por código")
            print("3. Ordenar por código y mostrar reporte")
            print("4. Guardar y salir")
            opcion = pedir_entero("Elija una opción: ", 1, 4)
            if opcion == 1:
                registrar_tramite()
            elif opcion == 2:
                buscar_expediente()
            elif opcion == 3:
                ordenar_seleccion()
                mostrar_reporte()
            else:
                guardar_archivo()
                print("Datos guardados en", datos.ARCHIVO, "- Hasta pronto.")
    except (EOFError, KeyboardInterrupt):
        # corrección de la prueba 15: cierre controlado si se corta la entrada
        print("\nEntrada cerrada. Guardando datos antes de salir...")
        guardar_archivo()
        print("Datos guardados en", datos.ARCHIVO, "- Hasta pronto.")


if __name__ == "__main__":
    main()
