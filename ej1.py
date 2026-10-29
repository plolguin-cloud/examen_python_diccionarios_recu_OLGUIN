notas= {
    "1. Villalobos" : [],
    "2. Salinas": [],
    "3. Olguin": [],
    "4. Barto": [],
    "5. Meoño": []
}
while True:

    print("1. Ver todas las notas Mostrará todas las notas de cada alumno.")
    print("2. Ver notas por alumno Mostrará las notas de un alumno en particular.")
    print("3. Cargar notas Permite seleccionar un alumno por apellido y cargar 5 notas.")
    print("4. Promedio Dado un alumno en particular permite ver su promedio.")

    respuesta = input("Ingrese el numero de lo que desee realizar: ")

    if respuesta == "1":
        for notas in notas.values():
            print(notas)

    elif respuesta == "2":
        nombre = input("Ingrese el nomre del alumno: ")
        if nombre in notas:
            if notas[nombre]:
                print({notas[nombre]})
            else:
                print(f"El alumno {nombre} no tiene las notas cargadas")
        else:
            print("El alumno no se encuentra")
    
    elif respuesta == "3":
        apellido = input("Ingrese el apellido exacto del alumno a cargar: ")
        if apellido in notas:
            notas[apellido] = [] 
            print(f"Ingrese las 5 notas de este alumno:")
            for i in range(1, 6):
                while True:
                        nota = float(input(f"Ingrese la nota {i}: "))
                        if 0 <= nota <= 10:
                            notas[apellido].append(nota)
                            break
                        else:
                            print("DSebe ser una nota del 0 y 10.")
            
            print("Las notas están cargadas")
        else:
            print("No se encuentra el alumno")

    elif respuesta=="4":
        apellido = input("Ingrese el apellido del alumno para ver el promedio: ")
        if apellido in notas:
            if notas[apellido]:
                promedio = sum(notas[apellido]) / len(notas[apellido])
                print(f"El promedio de {apellido} es: {promedio}")
            else:
                print("no tiene notas cargadas")
        else:
            print("El alumno no se encuentra")
            

    elif respuesta == "5":
        print("Saliendo del sistema!")
        break