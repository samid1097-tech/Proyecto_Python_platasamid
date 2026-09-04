import json
from datetime import datetime

def ver_horario():
    try:
        with open("horario.json", "r") as archivo:
            horario = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        horario = []

    if not horario:
        print("No hay materias registradas.")
        return

    dias = [
        "lunes",
        "martes",
        "miércoles",
        "miercoles",
        "jueves",
        "viernes",
        "sábado",
        "sabado",
        "domingo"
    ]

    print("\n---------- HORARIO SEMANAL ----------")

    for dia in dias:
        materias_dia = []

        for materia in horario:
            if materia["dia"] == dia:
                materias_dia.append(materia)
        if materias_dia:
            print(f"\n {dia.upper()} ")
            for materia in materias_dia:
                print(
                    f"Materia: {materia['materia']}\n"
                    f"Hora: {materia['hora_inicio']} - {materia['hora_fin']}\n"
                    f"Salón: {materia['salon']}\n"
                )


def modificar_materia():
    try:
        with open("horario.json", "r") as archivo:
            horario = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        horario = []
    if not horario:
        print("No hay materias registradas.")
        return
    print("\n---------- MATERIAS REGISTRADAS ----------")

    for i, materia in enumerate(horario):
        print(
            f"{i + 1}. {materia['materia']} | "
            f"{materia['dia']} | "
            f"{materia['hora_inicio']} - {materia['hora_fin']} | "
            f"Salón: {materia['salon']}"
        )

    while True:
        try:
            numero = int(input("\nIngrese el número de la materia que desea modificar: "))
            if numero >= 1 and numero <= len(horario):
                break
            else:
                print("Ingrese un número válido.")
        except ValueError:
            print("Debe ingresar un número.")

    materia = horario[numero - 1]

    print("\n¿Qué desea modificar?")
    print("1. Nombre de la materia")
    print("2. Día")
    print("3. Hora")
    print("4. Salón")
    print("5. Modificar todo")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        materia["materia"] = input(
            "Ingrese el nuevo nombre: "
        ).lower()
    elif opcion == "2":
        materia["dia"] = input(
            "Ingrese el nuevo día: "
        ).lower()

    elif opcion == "3":
        while True:
            hora_inicio = input("Nueva hora de inicio (hh:mm): ")
            hora_fin = input("Nueva hora final (hh:mm): ")
            try:
                hora_i = datetime.strptime(hora_inicio, "%H:%M")
                hora_f = datetime.strptime(hora_fin, "%H:%M")
                if hora_f <= hora_i:
                    print("La hora final debe ser mayor que la inicial.")
                else:
                    materia["hora_inicio"] = hora_inicio
                    materia["hora_fin"] = hora_fin
                    break
            except ValueError:
                print("Formato incorrecto. Use hh:mm.")
    elif opcion == "4":
        materia["salon"] = input(
            "Ingrese el nuevo salón: "
        )
    elif opcion == "5":
        materia["materia"] = input(
            "Nuevo nombre de la materia: "
        ).lower()
        materia["dia"] = input(
            "Nuevo día: "
        ).lower()

        while True:
            hora_inicio = input("Nueva hora de inicio (hh:mm): ")
            hora_fin = input("Nueva hora final (hh:mm): ")
            try:
                hora_i = datetime.strptime(hora_inicio, "%H:%M")
                hora_f = datetime.strptime(hora_fin, "%H:%M")
                if hora_f <= hora_i:
                    print("La hora final debe ser mayor que la inicial.")
                else:
                    materia["hora_inicio"] = hora_inicio
                    materia["hora_fin"] = hora_fin
                    break
            except ValueError:
                print("Formato incorrecto. Use hh:mm.")
        materia["salon"] = input(
            "Nuevo salón: "
        )
    else:
        print("Opción no válida.")
        return
    with open("horario.json", "w") as archivo:
        json.dump(horario, archivo, indent=4)

    print("Materia modificada correctamente.")

def eliminar_materia():
    try:
        with open("horario.json", "r") as archivo:
            horario = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        horario = []
    if not horario:
        print("No hay materias registradas.")
        return

    print("\n---------- MATERIAS REGISTRADAS ----------")
    for i, materia in enumerate(horario):
        print(
            f"{i + 1}. {materia['materia']} | "
            f"{materia['dia']} | "
            f"{materia['hora_inicio']} - {materia['hora_fin']} | "
            f"Salón: {materia['salon']}"
        )

    while True:
        try:
            numero = int(
                input("\nIngrese el número de la materia que desea eliminar: ")
            )
            if numero >= 1 and numero <= len(horario):
                break
            else:
                print("Ingrese un número válido.")
        except ValueError:
            print("Debe ingresar un número.")

    materia = horario[numero - 1]
    print(
        f"\nMateria seleccionada: {materia['materia']}"
    )
    confirmar = input(
        "¿Está seguro de que desea eliminarla? (si/no): "
    ).lower()
    if confirmar == "si":
        horario.pop(numero - 1)
        with open("horario.json", "w") as archivo:
            json.dump(horario, archivo, indent=4)
        print("Materia eliminada correctamente.")
    else:
        print("No se eliminó la materia.")

def hacer_reporte():
    try:
        with open("horario.json", "r") as archivo:
            horario = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        horario = []
    if not horario:
        print("No hay materias registradas.")
        return

    cantidad_materias = len(horario)
    horas_totales = 0

    for materia in horario:
        hora_inicio = datetime.strptime(
            materia["hora_inicio"], "%H:%M"
        )
        hora_fin = datetime.strptime(
            materia["hora_fin"], "%H:%M"
        )
        diferencia = hora_fin - hora_inicio
        horas_totales += diferencia.total_seconds() / 3600

    print("\n---------- REPORTE DEL HORARIO ----------")
    print(
        f"Cantidad de materias o actividades: {cantidad_materias}"
    )
    print(
        f"Cantidad total de horas semanales: {horas_totales:.2f}"
    )
    print("\nMaterias registradas:")

    for materia in horario:
        print(
            f"- {materia['materia']} | "
            f"{materia['dia']} | "
            f"{materia['hora_inicio']} - "
            f"{materia['hora_fin']} | "
            f"Salón: {materia['salon']}"
        )