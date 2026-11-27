"""Funciones compartidas para mapas H3 de la ZM de Querétaro."""
import numpy as np
import h3
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
from matplotlib.colors import BoundaryNorm, ListedColormap

REFERENCIAS = {
    "Centro histórico": (20.593, -100.392),
    "Juriquilla": (20.710, -100.450),
    "El Pueblito\n(Corregidora)": (20.539, -100.444),
    "La Cañada\n(El Marqués)": (20.613, -100.326),
    "Huimilpan": (20.372, -100.276),
}


def poligonos(celdas):
    """Contorno (lon, lat) de cada celda H3."""
    return [[(lng, lat) for lat, lng in h3.cell_to_boundary(c)] for c in celdas]


def base_mapa(celdas, figsize=(10, 11), pad=0.01, mapa_base=True):
    """Figura con límites ajustados a las celdas y mapa base gris de Esri (sin API key)."""
    polys = poligonos(celdas)
    xs = [x for p in polys for x, _ in p]
    ys = [y for p in polys for _, y in p]
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xlim(min(xs) - pad, max(xs) + pad)
    ax.set_ylim(min(ys) - pad, max(ys) + pad)
    ax.set_aspect(1 / np.cos(np.radians(20.6)))
    ax.set_axis_off()
    if mapa_base:
        try:
            import contextily as ctx
            ctx.add_basemap(ax, crs="EPSG:4326", source=ctx.providers.Esri.WorldGrayCanvas,
                            zoom=12, attribution_size=7)
        except Exception as e:
            print("Sin mapa base:", e)
    return fig, ax, polys


def capa_hex(ax, polys, **kwargs):
    """Dibuja los hexágonos; acepta array/cmap/norm o facecolors."""
    estilo = dict(edgecolor="white", linewidth=0.3, alpha=0.85)
    estilo.update(kwargs)
    coll = PolyCollection(polys, **estilo)
    ax.add_collection(coll)
    return coll


def escala_por_clases(bordes, colores):
    """Colormap discreto + norma para clases [b0, b1), [b1, b2), ..."""
    cmap = ListedColormap(colores)
    return cmap, BoundaryNorm(bordes, cmap.N)


def barra_clases(fig, ax, coll, bordes, etiquetas, titulo):
    cbar = fig.colorbar(coll, ax=ax, shrink=0.5,
                        ticks=[(a + b) / 2 for a, b in zip(bordes[:-1], bordes[1:])])
    cbar.ax.set_yticklabels(etiquetas)
    cbar.set_label(titulo)
    return cbar


def referencias(ax, puntos=REFERENCIAS):
    for nombre, (la, lo) in puntos.items():
        ax.plot(lo, la, "o", ms=4, color="#14213D")
        ax.annotate(nombre, (lo, la), xytext=(6, 6), textcoords="offset points", fontsize=10,
                    color="#14213D", fontweight="bold",
                    bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.75))
