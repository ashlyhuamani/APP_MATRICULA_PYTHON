"""
- registrar alumnos
- generar fichas de matricula
- mostrar lista de todos las matriculas
- filtrar matriculados por programa de estudio
"""
#lista_alumnos=[]
#while True:
#    opcion=input{"""elige lo que desas hacer
#                escribe  (s) si deseas registrar un alumno
#                escribe  (n) si deseas salir del programa 
#                 escribir tu respuesta: """}
#   if opcion. lower()=="n":
#      break
#nombre=input("ingrese el nombre del alumno: ")
#apellido=input("ingrese el apellido del alumno: ")
#alumno=(
#    "nombre":nombre,
#    "apellido":apellido 
#)
#lista_alumnos.append(alumno)
#print(lista_alumnos)


         lista_alumnos.append(alumno)
while True:
   menu_opciones=input(mensaje_menu())

   if menu_opciones.lower() == "n":
       print("saliendo del sistema")
       break
   elif menu_opciones.lower() == "s":
       ingresar_datos_alumno()
   else:
        print("opciones erronea")

print(lista_alumnos)


