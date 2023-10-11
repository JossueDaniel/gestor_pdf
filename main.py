import os

from GestorPDF import separar_pdf, unir_pdf


if __name__ == '__main__':
    while True:
        print("\t\t\tGestor PDF")
        print("\tSeparar PDF", "_" * 15, sep=" ", end=" 1\n")
        print("\tUnir PDF", "_" * 15, sep=" " * 4, end=" 2\n")
        print("\tSalir", "_" * 15, sep=" " * 7, end=" 0\n")
        try:
            opcion = int(input("\nIngrese una opción: "))
            if opcion == 1:
                os.system("clear")
                print()
                print("\t\t\tSeparar PDF")
                separar_pdf()
                print("\nSe ha separado satisfactoriamente su documento PDF")
                break
            elif opcion == 2:
                print()
                print("\t\t\tUnir PDF")
                unir_pdf()
                print("\nSe han unido satisfactorimente sus documentos PDF")
                break
            elif opcion == 0:
                print()
                print("Salir")
                break
            else:
                os.system('clear')
                print("\nOpción no válida")
                print()
        except ValueError:
            os.system('clear')
            print("\nError: Debe ingresar una opción válida marcada\n")
