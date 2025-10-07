# Analizador de Ficheros con Expresiones Regulares

Este proyecto corresponde a la práctica final de la asignatura Autómatas y Lenguajes Formales, del segundo curso del Grado en Ingeniería Informática (curso 2024/2025).

## Descripción

El proyecto implementa un analizador de ficheros que utiliza expresiones regulares para validar y procesar diferentes tipos de datos en formato específico. El sistema puede manejar y validar:

- Números de teléfono (en formato nacional e internacional)
- DNI/NIF españoles
- Fechas y horas en múltiples formatos
- Coordenadas geográficas
- Nombres de productos y precios

## Funcionalidades

El programa ofrece las siguientes opciones de procesamiento:

1. `-n [archivo]`: Normaliza y muestra todas las líneas válidas del archivo
2. `-sphone [teléfono] [archivo]`: Filtra las líneas que coinciden con el teléfono especificado
3. `-snif [DNI] [archivo]`: Filtra las líneas que coinciden con el DNI/NIF especificado
4. `-stime [desde] [hasta] [archivo]`: Filtra las líneas entre dos instantes temporales
5. `-slocation [desde] [radio] [archivo]`: Filtra las líneas dentro de un radio (en kilómetros) desde una coordenada específica

## Formatos Soportados

### Teléfonos
- Formato nacional: `XXX XXX XXX`
- Formato internacional: `+XX XXXXXXXXX`

### DNI/NIF
- Formato tradicional: `12345678A`
- Formato alternativo: `A-12345678`

### Fechas y Horas
- ISO: `YYYY-MM-DD HH:MM`
- Americano: `Month DD, YYYY HH:MM AM/PM`
- Europeo: `HH:MM:SS DD/MM/YYYY`

### Coordenadas
- Decimal: `±DD.DDDD, ±DDD.DDDD`
- Sexagesimal: `DD°MM'SS.SSSS" N/S, DDD°MM'SS.SSSS" E/W`
- GPS: `DDDMMSS.SSSSN/SDDDMMSS.SSSSE/W`

### Productos
- Nombre: Secuencia de caracteres alfabéticos
- Precio: Número decimal seguido de €

## Estructura del Proyecto

- `main.py`: Punto de entrada del programa y gestión de argumentos
- `tratamiento_ficheros.py`: Gestión de lectura y validación de ficheros
- `dni.py`: Validación y manejo de DNI/NIF
- `fecha_y_hora.py`: Procesamiento de fechas y horas
- `coordenadas.py`: Manejo de coordenadas geográficas
- `tlf.py`: Validación de números de teléfono
- `producto.py`: Validación de nombres de productos y precios

## Uso

```bash
# Normalizar todas las líneas válidas
python main.py -n archivo.txt

# Buscar por teléfono
python main.py -sphone "+34 666666666" archivo.txt

# Buscar por DNI
python main.py -snif "12345678A" archivo.txt

# Filtrar por rango de fechas
python main.py -stime "2024-01-01 00:00" "2024-12-31 23:59" archivo.txt

# Filtrar por ubicación (radio en km)
python main.py -slocation "40.7128,-74.0060" 10 archivo.txt
```

## Requisitos

- Python 3.x
- Módulo `regex`

## Autores

- Francisco Moreno Sánchez
- Arancha Baena León

Curso 2024/2025
Universidad [Nombre de tu Universidad]
