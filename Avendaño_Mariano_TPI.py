''' Gestion de Datos de Paises - TPI Programacion 1
============================================================
Estructura de datos: paises[] => lista de diccionarios
Cada elemento: {'nombre': str, 'poblacion': int, 'superficie': int, 'continente': str}
============================================================'''

ARCHIVO_CSV = "paises.csv"
def crear_csv():
    """Crea un archivo CSV vacio con los encabezados."""
    try:
        with open(ARCHIVO_CSV, "w") as archivo:
            archivo.write("nombre,poblacion,superficie,continente\n")
        print(f"-> Archivo '{ARCHIVO_CSV}' creado exitosamente.")
        return []
    except IOError as e:
        print(f"-> Error al crear el archivo: {e}")
        return []


def cargar_paises_desde_csv():
    """Carga paises desde el archivo CSV. Si no existe, lo crea vacio."""
    paises = []
    try:
        with open(ARCHIVO_CSV, "r") as archivo:
            lineas = archivo.readlines()

        for numero_fila in range(1, len(lineas)):
            linea = lineas[numero_fila].strip()
            if not linea:
                continue
            try:
                partes = linea.split(",")
                if len(partes) != 4:
                    raise ValueError("Cantidad incorrecta de campos")

                nombre = partes[0].strip()
                poblacion = int(partes[1].strip())
                superficie = int(partes[2].strip())
                continente = partes[3].strip()

                if poblacion <= 0 or superficie <= 0:
                    raise ValueError("Valores numericos no positivos")

                paises.append({
                    "nombre": nombre,
                    "poblacion": poblacion,
                    "superficie": superficie,
                    "continente": continente,
                })
            except (ValueError, IndexError):
                print(f"-> Advertencia: Fila {numero_fila + 1} ignorada por formato invalido.")
    except FileNotFoundError:
        print("-> El archivo no existe. Creando uno nuevo...")
        return crear_csv()

    if not paises:
        print("-> El archivo CSV esta vacio. Use la opcion 2 para agregar paises.")
    else:
        print(f"-> Se cargaron {len(paises)} paises desde '{ARCHIVO_CSV}'.")

    return paises


# ----- FUNCION 3: Guardado en CSV -----------------------------------
def guardar_paises_en_csv(paises):
    """Se guardan los datos en el archivo CSV."""
    try:
        with open(ARCHIVO_CSV, "w") as archivo:
            archivo.write("nombre,poblacion,superficie,continente\n")
            for pais in paises:
                archivo.write(f"{pais['nombre']},{pais['poblacion']},{pais['superficie']},{pais['continente']}\n")
        print("-> Datos guardados correctamente en el CSV.")
        return True

    except OSError as e:
        print(f"-> Error al guardar el archivo CSV: {e}")
        return False


# ----- FUNCION 4: Visualizacion -----------------------------------
def mostrar_paises(lista, titulo="Listado de paises"):
    if not lista:
        print("-> No hay paises para mostrar.")
        return

    print(f"\n--- {titulo} ---")
    print(f"{'Nombre':<18} {'Poblacion':>14} {'Superficie':>12} {'Continente':<12}")
    print("-" * 60)
    for pais in lista:
        print(
            f"{pais['nombre']:<18} {pais['poblacion']:>14,} "
            f"{pais['superficie']:>12,} {pais['continente']:<12}"
        )
    print(f"\nTotal: {len(lista)} pais(es).")


# ----- FUNCION 5: Alta de pais -----------------------------------
def agregar_pais(paises):
    """Registra un pais nuevo."""
    while True:
        try:
            nombre = input("Ingrese el nombre del pais: ").strip().title()
            if not nombre:
                raise ValueError("El nombre no puede estar vacio.")
            for caracter in nombre:
                if caracter.isdigit():
                    raise ValueError("El nombre no puede contener numeros.")
            for pais in paises:
                if pais["nombre"].lower() == nombre.lower():
                    raise ValueError(f"'{nombre}' ya se encuentra registrado.")

            continente = input("Ingrese el continente: ").strip().title()
            if not continente:
                raise ValueError("El continente no puede estar vacio.")
            for caracter in continente:
                if caracter.isdigit():
                    raise ValueError("El continente no puede contener numeros.")
            poblacion_str = input("Ingrese la poblacion: ").strip()
            if not poblacion_str:
                raise ValueError("La poblacion no puede estar vacia.")
            if not poblacion_str.isdigit():
                raise ValueError("La poblacion debe ser un numero entero.")
            poblacion = int(poblacion_str)
            if poblacion <= 0:
                raise ValueError("La poblacion debe ser un entero mayor a 0.")

            superficie_str = input("Ingrese la superficie en km2: ").strip()
            if not superficie_str:
                raise ValueError("La superficie no puede estar vacia.")
            if not superficie_str.isdigit():
                raise ValueError("La superficie debe ser un numero entero.")
            superficie = int(superficie_str)
            if superficie <= 0:
                raise ValueError("La superficie debe ser un entero mayor a 0.")

        except ValueError as e:
            print(f"-> Error: {e}")
            continue

        break

    paises.append({
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente,
    })
    print(f"-> Pais '{nombre}' agregado con exito.")
    guardar_paises_en_csv(paises)


# ----- FUNCION 6: Actualizacion -----------------------------------
def actualizar_pais(paises):
    """Actualiza poblacion y superficie de un pais existente."""
    if not paises:
        print("-> No hay paises cargados.")
        return

    while True:
        try:
            nombre = input("Ingrese el nombre del pais a actualizar: ").strip()
            if not nombre:
                raise ValueError("El nombre no puede estar vacio.")
            for caracter in nombre:
                if caracter.isdigit():
                    raise ValueError("El nombre no puede contener numeros.")

            indice = -1
            for i, pais in enumerate(paises):
                if pais["nombre"].lower() == nombre.lower():
                    indice = i
                    break

            if indice == -1:
                raise ValueError(f"'{nombre}' no se encuentra registrado.")

            poblacion_str = input(f"Nueva poblacion para '{paises[indice]['nombre']}': ").strip()
            if not poblacion_str:
                raise ValueError("La poblacion no puede estar vacia.")
            if not poblacion_str.isdigit():
                raise ValueError("La poblacion debe ser un numero entero.")
            poblacion = int(poblacion_str)
            if poblacion <= 0:
                raise ValueError("La poblacion debe ser un entero mayor a 0.")

            superficie_str = input(f"Nueva superficie en km2 para '{paises[indice]['nombre']}': ").strip()
            if not superficie_str:
                raise ValueError("La superficie no puede estar vacia.")
            if not superficie_str.isdigit():
                raise ValueError("La superficie debe ser un numero entero.")
            superficie = int(superficie_str)
            if superficie <= 0:
                raise ValueError("La superficie debe ser un entero mayor a 0.")

        except ValueError as e:
            print(f"-> Error: {e}")
            continue

        break

    paises[indice]["poblacion"] = poblacion
    paises[indice]["superficie"] = superficie
    print(f"-> Datos de '{paises[indice]['nombre']}' actualizados con exito.")
    guardar_paises_en_csv(paises)


# ----- FUNCION 7: Busqueda -----------------------------------
def buscar_pais(paises):
    """Busca paises por nombre con coincidencia exacta o parcial."""
    if not paises:
        print("-> No hay paises cargados.")
        return

    try:
        criterio = input("Ingrese el nombre o parte del nombre a buscar: ").strip()
        if not criterio:
            raise ValueError("El criterio de busqueda no puede estar vacio.")

        modo = input("Busqueda exacta (E) o parcial (P)?: ").strip().upper()
        if modo not in ("", "E", "P"):
            raise ValueError("Debe ingresar 'E' para exacta o 'P' para parcial.")

        if not modo:
            modo = "P"

    except ValueError as e:
        print(f"-> Error: {e}")
        return

    resultados = []
    for pais in paises:
        nombre = pais["nombre"].lower()
        busqueda = criterio.lower()

        if modo == "E" and nombre == busqueda:
            resultados.append(pais)
        elif modo == "P" and busqueda in nombre:
            resultados.append(pais)

    if not resultados:
        print(f"-> No se encontraron paises que coincidan con '{criterio}'.")
        return

    tipo = "exacta" if modo == "E" else "parcial"
    mostrar_paises(resultados, f"Resultados de busqueda ({tipo})")


# ----- FUNCION 8: Filtros -----------------------------------
def pedir_entero(mensaje):
    """Solicita un entero validado al usuario."""
    while True:
        try:
            valor = int(input(mensaje).strip())
            return valor
        except ValueError:
            print("-> Error: Debe ingresar un numero entero valido.")


def filtrar_por_continente(paises):
    """Filtra paises por continente."""
    continente = input("Ingrese el continente a filtrar: ").strip()
    if not continente:
        print("-> Error: El continente no puede estar vacio.")
        return
    for caracter in continente:
        if caracter.isdigit():
            print("-> Error: El continente no puede contener numeros.")
            return

    resultados = [
        pais for pais in paises
        if pais["continente"].lower() == continente.lower()
    ]

    if not resultados:
        print(f"-> No hay paises registrados en el continente '{continente}'.")
        return

    mostrar_paises(resultados, f"Paises de {continente}")


def filtrar_por_rango_poblacion(paises):
    """Filtra paises dentro de un rango de poblacion."""
    minimo = pedir_entero("Poblacion minima: ")
    maximo = pedir_entero("Poblacion maxima: ")

    if minimo > maximo:
        print("-> Error: La poblacion minima no puede ser mayor que la maxima.")
        return

    resultados = [
        pais for pais in paises
        if minimo <= pais["poblacion"] <= maximo
    ]

    if not resultados:
        print("-> No hay paises dentro del rango de poblacion indicado.")
        return

    mostrar_paises(resultados, f"Poblacion entre {minimo:,} y {maximo:,}")


def filtrar_por_rango_superficie(paises):
    """Filtra paises dentro de un rango de superficie."""
    minimo = pedir_entero("Superficie minima (km2): ")
    maximo = pedir_entero("Superficie maxima (km2): ")

    if minimo > maximo:
        print("-> Error: La superficie minima no puede ser mayor que la maxima.")
        return

    resultados = [
        pais for pais in paises
        if minimo <= pais["superficie"] <= maximo
    ]

    if not resultados:
        print("-> No hay paises dentro del rango de superficie indicado.")
        return

    mostrar_paises(resultados, f"Superficie entre {minimo:,} y {maximo:,} km2")


def filtrar_paises(paises):
    """Submenu de filtros por continente, poblacion o superficie."""
    if not paises:
        print("-> No hay paises cargados.")
        return

    print("\n--- Filtros ---")
    print("1. Por continente")
    print("2. Por rango de poblacion")
    print("3. Por rango de superficie")
    print("4. Volver")

    try:
        opcion = int(input("Seleccione una opcion: ").strip())

        if opcion == 1:
            filtrar_por_continente(paises)
        elif opcion == 2:
            filtrar_por_rango_poblacion(paises)
        elif opcion == 3:
            filtrar_por_rango_superficie(paises)
        elif opcion == 4:
            return
        else:
            raise ValueError("Opcion invalida.")

    except ValueError as e:
        print(f"-> Error: {e}")


# ----- FUNCION 9: Ordenamiento -----------------------------------
def pedir_orden():
    """Pide al usuario si desea orden ascendente o descendente."""
    while True:
        orden = input("Orden ascendente (A) o descendente (D)? ").strip().upper()
        if orden == "A":
            return False
        if orden == "D":
            return True
        print("-> Error: Debe ingresar 'A' o 'D'.")


def ordenar_paises(paises):
    """Ordena y muestra paises por nombre, poblacion o superficie."""
    if not paises:
        print("-> No hay paises cargados.")
        return

    print("\n--- Ordenamiento ---")
    print("1. Por nombre")
    print("2. Por poblacion")
    print("3. Por superficie")
    print("4. Volver")

    try:
        opcion = int(input("Seleccione una opcion: ").strip())
        if opcion == 4:
            return
        if opcion not in (1, 2, 3):
            raise ValueError("Opcion invalida.")

        descendente = pedir_orden()

        if opcion == 1:
            clave = "nombre"
            titulo = "Paises ordenados por nombre"
        elif opcion == 2:
            clave = "poblacion"
            titulo = "Paises ordenados por poblacion"
        else:
            clave = "superficie"
            titulo = "Paises ordenados por superficie"

        ordenados = sorted(paises, key=lambda p: p[clave], reverse=descendente)
        direccion = "descendente" if descendente else "ascendente"
        mostrar_paises(ordenados, f"{titulo} ({direccion})")

    except ValueError as e:
        print(f"-> Error: {e}")


# ----- FUNCION 10: Estadisticas -----------------------------------
def mostrar_estadisticas(paises):
    """Calcula y muestra indicadores clave del dataset."""
    if not paises:
        print("-> No hay paises cargados.")
        return

    mayor = paises[0]
    menor = paises[0]
    total_poblacion = 0
    total_superficie = 0
    por_continente = {}

    for pais in paises:
        total_poblacion += pais["poblacion"]
        total_superficie += pais["superficie"]

        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais

        continente = pais["continente"]
        por_continente[continente] = por_continente.get(continente, 0) + 1

    promedio_poblacion = total_poblacion / len(paises)
    promedio_superficie = total_superficie / len(paises)

    print("\n--- Estadisticas ---")
    print(f"Pais con mayor poblacion: {mayor['nombre']} ({mayor['poblacion']:,} hab.)")
    print(f"Pais con menor poblacion: {menor['nombre']} ({menor['poblacion']:,} hab.)")
    print(f"Promedio de poblacion: {promedio_poblacion:,.2f} hab.")
    print(f"Promedio de superficie: {promedio_superficie:,.2f} km2")
    print("\nCantidad de paises por continente:")
    for continente in sorted(por_continente):
        print(f"  - {continente}: {por_continente[continente]}")


# ----- MENU PRINCIPAL -----------------------------------
def main():
    paises = cargar_paises_desde_csv()
    while True:
        print("\n" + "=" * 50)
        print("GESTION DE DATOS DE PAISES")
        print("=" * 50)
        print("1. Mostrar todos los paises")
        print("2. Agregar un pais")
        print("3. Actualizar poblacion y superficie")
        print("4. Buscar por nombre")
        print("5. Filtrar paises")
        print("6. Ordenar paises")
        print("7. Mostrar estadisticas")
        print("8. Salir")
        print("=" * 50)

        try:
            entrada = input("Seleccione una opcion: ").strip()
            if not entrada:
                continue
            opcion = int(entrada)

        except ValueError:
            print("-> Error: Debe ingresar un numero entero valido.")
            continue

        if opcion == 1:
            mostrar_paises(paises)

        elif opcion == 2:
            print("\n--- Agregar pais ---")
            agregar_pais(paises)

        elif opcion == 3:
            print("\n--- Actualizar pais ---")
            actualizar_pais(paises)

        elif opcion == 4:
            print("\n--- Buscar pais ---")
            buscar_pais(paises)

        elif opcion == 5:
            filtrar_paises(paises)

        elif opcion == 6:
            ordenar_paises(paises)

        elif opcion == 7:
            mostrar_estadisticas(paises)

        elif opcion == 8:
            print("\n-> Sistema cerrado. Hasta luego!")
            break

        else:
            print("-> Error: Opcion invalida. Ingrese un numero del 1 al 8.")


if __name__ == "__main__":
    main()
