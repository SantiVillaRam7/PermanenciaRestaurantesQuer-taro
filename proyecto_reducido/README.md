# Proyecto reducido · Rotación de restaurantes en la ZM de Querétaro, 2020 → 2025

Versión acotada del caso de titulación. Usa solo las dos ediciones del DENUE que incorporan un Censo Económico
(**04/2020** y **05/2025**), porque son las únicas en las que el directorio registra el cambio real de los negocios.

**Pregunta:** ¿qué características de la zona se asocian con que los restaurantes permanezcan o roten entre 2020 y 2025?
¿Los generadores de tráfico (escuelas, salud, oficinas, gobierno, comercio grande, ocio) explican más que la población?

## Notebooks (correr en orden, desde `notebooks/`)

| Notebook | Qué hace | Salida principal |
|---|---|---|
| `00_datos_origen` | Copia del proyecto anterior (o descarga) el DENUE 2020 y 2025, el Censo 2020 y los centroides de manzana | `data/raw/` |
| `01_ingesta` | Limpia las dos ediciones; separa restaurantes y administración pública | `restaurantes_zmq.parquet` |
| `02_poblacion_hexagonos` | Censo 2020 por hexágono H3 (res. 8) y tipo de zona | `hex_res8_base_2020.parquet` |
| `03_enlace_2020_2025` | Sigue a cada restaurante de 2020: continúa, reemplazo o salida; entradas; validación | `transiciones_…`, `entradas_…`, `matriz_…` |
| `04_rotacion_y_generadores` | Índice de rotación y generadores de tráfico (2020) por hexágono | `hex_res8_modelo.parquet` |
| `05_modelo_explicativo` | Modelo A (logístico, permanencia) y modelo B (Poisson, rotación) | `modelo_*.csv` y figuras |
| `06_datos_monetarios` | Descarga Censos Económicos 2024 (Querétaro) y ENIGH 2024 (hogares) | `ce2024_restaurantes`, `enigh2024_hogares_urbanos` |
| `07_oferta_ingresos` | Ventas y utilidad estimadas de cada restaurante; oferta en pesos por hexágono | `restaurantes_ingresos_*`, `oferta_hex8` |
| `08_demanda_gasto` | Gasto en comer fuera de residentes y trabajadores por hexágono; saturación | `demanda_hex8` |
| `09_recomendacion` | Probabilidad de seguir 5 años, ventas, utilidad y valor esperado por zona × tipo (dos alternativas de ventas); validación espacial y prueba hacia atrás | `recomendaciones_hex_tipo` |

## Entorno

```bash
conda env update -n tesis-qro -f environment.yml    # agrega statsmodels al entorno que ya tienes
conda activate tesis-qro
```

## Relación con el proyecto anterior

Esta carpeta vive dentro de `tesis_queretaro/`. El notebook 00 reutiliza los archivos de `tesis_queretaro/data/`
para no volver a descargar. La nota de investigación (todas las ediciones) sigue en la carpeta principal.
