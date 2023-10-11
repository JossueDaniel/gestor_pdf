import os
import PyPDF2
from PyPDF2 import PdfReader, PdfWriter


def separar_pdf():
    while True:
        try:
            nombre_documento = input("Ingrese el documento que desea separar\n")
            os.system("clear")
            pdf_reader = PdfReader(f"{nombre_documento}.pdf")
            paginas = []
            while True:
                print(f"\nPáginas del documento {nombre_documento}:", len(pdf_reader.pages), "\n")
                print("\t\t\tOpciones de Páginas")
                print("\tSeparar todas", "_" * 15, sep=" ", end=" 1\n")
                print("\tPersonalizado", "_" * 15, sep=" ", end=" 2\n")
                try:
                    opcion = int(input("\nIngrese una opción: "))
                    if opcion == 1:
                        print("\nSeparar todas las páginas")
                        archivo = pdf_reader.pages
                        break
                    elif opcion == 2:
                        print("\n\tPersonalizar páginas a separar")
                        while True:
                            try:
                                pag = int(input("\nIngrese el número de página que desea separar\n")) - 1
                                paginas.append(pdf_reader.pages[pag])
                                while True:
                                    try:
                                        separar_otra_pagina = int(input("\nIngrese '1' si desea separar "
                                                                        "más páginas o '0' si ha finalizado\n"))
                                        if 0 <= separar_otra_pagina <= 1:
                                            break
                                        else:
                                            os.system("clear")
                                            print("\nOpción no válida")
                                    except ValueError:
                                        os.system("clear")
                                        print("\nError: opción incorrecta, debe ser un número")
                                if separar_otra_pagina == 0:
                                    archivo = list(paginas)
                                    break
                            except ValueError:
                                os.system("clear")
                                print("\nError: No es un número de página")
                            except IndexError:
                                os.system("clear")
                                print("\nEl número de página no existe en el documento")
                        break
                    else:
                        os.system("clear")
                        print("\nOpción no válida")
                except ValueError:
                    os.system("clear")
                    print("\nError: opción incorrecta, debe ser un número")

            for index, page in enumerate(archivo):
                pdf_writer = PdfWriter()
                pdf_writer.add_page(page)
                with open(f"{nombre_documento}_page_{index + 1}.pdf", "wb") as out:
                    pdf_writer.write(out)
        except FileNotFoundError:
            print("\nNo existe el documento\n")
        else:
            break


def unir_pdf():
    archivos = []

    while True:
        try:
            documento = input("\nIngrese el documento que desea unir\n")
            archivos.append(f"{documento}.pdf")
            while True:
                try:
                    unir_otra_pagina = int(input("\nIngrese '1' si desea unir más páginas o '0' si ha finalizado\n"))
                    if 0 <= unir_otra_pagina <= 1:
                        break
                    else:
                        os.system("clear")
                        print("\nOpción no válida")
                except ValueError:
                    os.system("clear")
                    print("\nError: Se debe ingresar una opción válida marcada")
            if unir_otra_pagina == 0:
                nombre_salida = "pdf_unido.pdf"
                pdf_final = PyPDF2.PdfMerger()
                for nombre_archivo in archivos:
                    pdf_final.append(nombre_archivo)
                pdf_final.write(nombre_salida)
                pdf_final.close()
                break
        except FileNotFoundError:
            os.system("clear")
            print("\nNo existe el documento")
