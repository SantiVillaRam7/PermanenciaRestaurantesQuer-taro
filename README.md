# Permanencia y reemplazo de restaurantes en la Zona Metropolitana de Querétaro, 2020–2025

Conjunto de datos y código de un caso de investigación de titulación en Ciencia de Datos (ITAM).
Sigue a cada restaurante (SCIAN 722) registrado en el DENUE 04/2020 hasta el DENUE 05/2025 y
clasifica qué hay en su ubicación: el mismo negocio, otro negocio o ningún sucesor.

Autor: Santiago Villaseñor Ramírez · ORCID: [0000-0000-0000-0000]

## Contenido

| Carpeta | Qué contiene |
|---|---|
| `data/raw/` | Descargas del INEGI: DENUE de Querétaro (7 ediciones) y Censo 2020 por manzana |
| `data/processed/` | Registros del conjunto (ver tabla abajo) |
| `data/validacion/` | Pruebas de validación y muestra para revisión manual |
| `notebooks/` | Cuadernos 00–03 que reproducen todo desde la descarga |
| `figures/` | Figuras generadas por los cuadernos |
| Raíz | Nota de investigación, nota de datos y entorno de Python |

## Registros principales (`data/processed/`)

| Archivo | Unidad | Filas |
|---|---|---|
| `transiciones_restaurantes_2020_2025.parquet` | Restaurante de 04/2020 | 8,536 |
| `entradas_restaurantes_2020_2025.parquet` | Restaurante nuevo en 05/2025 | 5,479 |
| `matriz_hex8_tipo_2020_2025.parquet` | Hexágono H3 res. 8 × tipo | 6,490 |
| `hex_res8_base_2020.parquet` | Hexágono H3 res. 8 | 644 |

El diccionario de variables está en la nota de datos (`Nota_de_datos_restaurantes_ZMQ.docx`, Tablas 3–5).

## Cómo reproducir

```bash
conda env create -f environment.yml
conda activate tesis-qro
```

Después ejecuta los cuadernos en orden: `00_descarga_denue`, `01_ingesta_restaurantes`,
`02_poblacion_vs_restaurantes`, `03_panel_y_matriz`. Los parámetros del enlace están al inicio del cuaderno 03.

## Fuentes y licencia

Datos de origen: INEGI (DENUE, Censo de Población y Vivienda 2020, Marco Geoestadístico 2020),
sujetos a los Términos de Libre Uso de la Información del INEGI. Datos derivados: [CC BY 4.0].
