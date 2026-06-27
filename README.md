# TPI Programación 1 — Gestión de Datos de Países

Aplicación en consola desarrollada en **Python 3** para gestionar información de países: lectura desde CSV, altas, actualizaciones, búsquedas, filtros, ordenamientos y estadísticas.

## Integrantes

- **Mariano Avendaño** (trabajo individual)

## Estructura del proyecto

```
TPI_Paises/
├── Avendaño_Mariano_TPI.py      # Código fuente principal
├── paises.csv                   # Dataset base (15 países)
├── Avendaño_Mariano_TPI_Informe.pdf  # Informe académico
└── README.md                    # Este archivo
```

## Requisitos

- Python 3.x
- **No requiere librerías externas ni módulos adicionales.** Solo usa funciones nativas de Python (`open`, `print`, `input`, `sorted`, etc.).

## Cómo ejecutar

1. Clonar o descargar el repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar:

```bash
python Avendaño_Mariano_TPI.py
```

En Windows, si `python` no responde:

```bash
py Avendaño_Mariano_TPI.py
```

> **Nota:** el archivo `paises.csv` debe estar en la misma carpeta que el script. Si no existe, el programa lo crea automáticamente vacío.

## Formato del CSV

El archivo `paises.csv` usa el siguiente encabezado:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,America
Brasil,213993437,8515767,America
```

| Campo       | Tipo   | Descripción                      |
|-------------|--------|----------------------------------|
| nombre      | string | Nombre del país                  |
| poblacion   | int    | Cantidad de habitantes (> 0)     |
| superficie  | int    | Superficie en km² (> 0)          |
| continente  | string | Continente al que pertenece      |

Las filas con formato inválido se ignoran con una advertencia; la carga del resto continúa normalmente.

## Menú principal

| Opción | Función                                  |
|--------|------------------------------------------|
| 1      | Mostrar todos los países                 |
| 2      | Agregar un país (sin campos vacíos)      |
| 3      | Actualizar población y superficie        |
| 4      | Buscar por nombre (exacta o parcial)     |
| 5      | Filtrar por continente, población o superficie |
| 6      | Ordenar por nombre, población o superficie     |
| 7      | Mostrar estadísticas                     |
| 8      | Recargar datos desde CSV                 |
| 9      | Salir                                    |

Los cambios realizados mediante las opciones 2 y 3 se guardan automáticamente en `paises.csv`.

## Ejemplos de uso

### Inicio del programa

```
-> Se cargaron 15 países desde 'paises.csv'.

==================================================
GESTIÓN DE DATOS DE PAÍSES
==================================================
1. Mostrar todos los países
...
==================================================
Seleccione una opción:
```

### Opción 1 — Mostrar todos los países

```
--- Listado de países ---
Nombre             Población     Superficie Continente
------------------------------------------------------------
Argentina           45,376,763    2,780,400 America
Brasil             213,993,437    8,515,767 America
...
Total: 15 país(es).
```

### Opción 4 — Búsqueda parcial

```
Ingrese el nombre o parte del nombre a buscar: arg
¿Búsqueda exacta (E) o parcial (P)? [P]: P

--- Resultados de búsqueda (parcial) ---
Nombre             Población     Superficie Continente
------------------------------------------------------------
Argentina           45,376,763    2,780,400 America

Total: 1 país(es).
```

### Opción 5 — Filtrar por rango de población

```
--- Filtros ---
1. Por continente
2. Por rango de población
3. Por rango de superficie
Seleccione una opción: 2
Población mínima: 50000000
Población máxima: 300000000

--- Población entre 50,000,000 y 300,000,000 ---
Nombre             Población     Superficie Continente
------------------------------------------------------------
Brasil             213,993,437    8,515,767 America
Alemania            83,149,300      357,022 Europa
...
```

### Opción 6 — Ordenar por superficie descendente

```
--- Ordenamiento ---
1. Por nombre
2. Por población
3. Por superficie
Seleccione una opción: 3
Orden ascendente (A) o descendente (D)? D

--- Países ordenados por superficie (descendente) ---
Nombre             Población     Superficie Continente
------------------------------------------------------------
Canada              38,008,000    9,984,670 America
Brasil             213,993,437    8,515,767 America
Australia           25,687,000    7,692,024 Oceania
...
```

### Opción 7 — Estadísticas

```
--- Estadísticas ---
País con mayor población: India (1,380,004,385 hab.)
País con menor población: Uruguay (3,473,730 hab.)
Promedio de población: 168,978,909.53 hab.
Promedio de superficie: 2,716,785.27 km²

Cantidad de países por continente:
  - Africa: 3
  - America: 6
  - Asia: 2
  - Europa: 3
  - Oceania: 1
```

### Opción 2 — Agregar un país (con validaciones)

```
Ingrese el nombre del país: Japón
Ingrese el continente: Asia
Ingrese la población: -500
-> Error: La población debe ser un entero mayor a 0.
```

```
Ingrese el nombre del país: Argentina
-> Error: 'Argentina' ya se encuentra registrado.
```

## Manejo de errores

El sistema valida:

- **CSV**: filas con cantidad incorrecta de campos, valores no numéricos o negativos → se omiten con advertencia.
- **Alta**: nombre vacío, país duplicado, continente vacío, población o superficie ≤ 0.
- **Actualización**: país no encontrado, valores numéricos inválidos.
- **Búsqueda**: criterio vacío, modo de búsqueda inválido.
- **Filtros**: continente vacío, rango mínimo > máximo.
- **Menú**: entradas no numéricas o fuera de rango.

## Documentación académica

El informe completo (marco teórico, decisiones técnicas, diagrama de flujo, capturas y conclusiones) está disponible en:

- **PDF en el repositorio:** `Avendaño_Mariano_TPI_Informe.pdf`
- **Enlace directo:** _(agregar enlace al PDF en GitHub una vez subido)_

## Video demostrativo

> **Enlace al video:** _(agregar URL de YouTube una vez publicado)_

El video cubre: presentación del proyecto, recorrido del código, demostración de todas las funcionalidades y manejo de casos de error.

## Repositorio GitHub

> **URL:** _(agregar URL del repositorio una vez publicado)_

## Notas para la entrega

El `.zip` de entrega contiene:

- `Avendaño_Mariano_TPI.py` — código fuente completo
- `paises.csv` — dataset base
- `Avendaño_Mariano_TPI_Informe.pdf` — informe académico
- `README.md` — este archivo

