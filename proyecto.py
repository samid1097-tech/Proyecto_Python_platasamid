import json
from datetime import datetime
import funciones


def registrar_materia():
    try:
        with open("horario.json", "r") as archivo:
            horario = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        horario = []

    materia = input("Por favor ingrese el nombre de la materia: ").lower()
    dia = input("Por favor ingrese el día de esta materia: ").lower()

    while True:
        hora_inicio = input(
            "Por favor ingrese la hora de inicio de la materia (hh:mm): "
        )
        hora_fin = input(
            "Por favor ingrese la hora final de la materia (hh:mm): "
        )
        try:
            hora_i = datetime.strptime(hora_inicio, "%H:%M")
            hora_f = datetime.strptime(hora_fin, "%H:%M")

            if hora_f <= hora_i:
                print("La hora de inicio no puede ser mayor o igual que la hora final.")
            else:
                break

        except ValueError:
            print(
                "Por favor ingresa un formato válido. "
                "Recuerda que tiene que ser así: (hh:mm)"
            )

    salon = input("Por favor ingrese el salón de la materia: ")

    for materia_guardada in horario:
        if materia_guardada["dia"] == dia:

            hora_inicio_guardada = datetime.strptime(
                materia_guardada["hora_inicio"], "%H:%M"
            )

            hora_fin_guardada = datetime.strptime(
                materia_guardada["hora_fin"], "%H:%M"
            )

            if hora_i < hora_fin_guardada and hora_f > hora_inicio_guardada:
                print("No se puede registrar la materia.")
                print(
                    f"Esta materia ya está registrada: "
                    f"{materia_guardada['materia']} "
                    f"el {dia} de "
                    f"{materia_guardada['hora_inicio']} "
                    f"a {materia_guardada['hora_fin']}."
                )
                return

    nueva_materia = {
        "materia": materia,
        "dia": dia,
        "hora_inicio": hora_inicio,
        "hora_fin": hora_fin,
        "salon": salon
    }

    horario.append(nueva_materia)

    with open("horario.json", "w") as archivo:
        json.dump(horario, archivo, indent=4)

    print("Materia registrada correctamente.")


while True:
    print("   GENERADOR DE HORARIOS PARA ESTUDIANTES")
    print("1. Registrar una materia o actividad")
    print("2. Ver horario semanal")
    print("3. Modificar una materia o una actividad")
    print("4. Eliminar una materia o una actividad")
    print("5. Hacer reporte del horario")
    print("6. Salir")

    try:
        opcion = int(input("\nSeleccione una opción: "))
    except ValueError:
        print("Por favor ingrese un número.")
        continue

    if opcion == 1:
        registrar_materia()
    elif opcion == 2:
        funciones.ver_horario()
    elif opcion == 3:
        funciones.modificar_materia()
    elif opcion == 4:
        funciones.eliminar_materia()
    elif opcion == 5:
        funciones.hacer_reporte()
    elif opcion == 6:
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida.")