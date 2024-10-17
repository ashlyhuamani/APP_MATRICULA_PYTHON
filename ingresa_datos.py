
def ingresar_datos_alumno():
    id =len(lista_alumnos)+1
    cui =int(input("ingrese el numero de dni: "))
    nombre =input("ingrese el nombre del alumno: ")
    apellido =input("ingrese el apellido del alumno: ")
    numero_celular =int(input("ingrese el numero de celular: "))
    programa_estudio =input("ingrese el programa de estudio")
    ciclo_academico =input("ingrese su ciclo academico. ")
    email =input("ingrese su correo electronico")
    return(id,cui,nombre,apellido,numero_celular,programa_estudio,ciclo_academico,email)