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



lista_alumnos=[]
def mensaje_menu():
    menu_opciones = """
    ------------Bienvenido al sistema------------
    -------------Registra tu alumno--------------
    
1. escribe  (s) si deseas registrar un alumno
2. escribe  (n) si deseas salir del programa 
escribe la accion que deseas realizar: """
    return menu_opciones

def ingresar_datos_alumno():
    id =len(lista_alumnos)+1
    cui =int(input("ingrese el numero de dni: "))
    nombre =input("ingrese el nombre del alumno: ")
    apellido =input("ingrese el apellido del alumno: ")
    numero_celular =int(input("ingrese el numero de celular: "))
    programa_estudio =input("ingrese el programa de estudio")
    ciclo_academico =input("ingrese su ciclo academico. ")
    email =input("ingrese su correo electronico")

def guardar_datos_alumno(id,cui,nombre,apellido,numero_celular,programa_estudio,ciclo_academico,email):
         alumno={
                "id":id,
                "cui":cui,
                "nombre":nombre,
                "apellido":apellido,
                "numero_celular":numero_celular,
                "programa_estudio":programa_estudio,
                "ciclo_academico":ciclo_academico,
                "email":email
               }
        
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


