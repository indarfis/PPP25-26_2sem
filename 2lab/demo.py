from itertools import islice, chain

from generators import *
from transforms import *
from filters import *
from aggregators import *
from visualize import *
from zip_utils import *

# ------------------------------------------------
# 1. Генерация
# ------------------------------------------------

rects = list(islice(gen_rectangle(), 7))
tris = list(islice(gen_triangle(), 7))
hexs = list(islice(gen_hexagon(), 7))

visualize(rects, "Rectangles")
visualize(tris, "Triangles")
visualize(hexs, "Hexagons")

# ------------------------------------------------
# 2. Трансформации
# ------------------------------------------------

band1 = list(
    map(
        tr_rotate(20),
        rects
    )
)

band2 = list(
    map(
        tr_translate(0, 5),
        band1
    )
)

band3 = list(
    map(
        tr_translate(0, 10),
        band1
    )
)

visualize(
    chain(band1, band2, band3),
    "Three parallel bands"
)

# ------------------------------------------------
# 3. Пересекающиеся ленты
# ------------------------------------------------

cross1 = list(
    map(
        tr_rotate(30),
        tris
    )
)

cross2 = list(
    map(
        tr_rotate(-30),
        tris
    )
)

cross2 = list(
    map(
        tr_translate(5, 3),
        cross2
    )
)

visualize(
    chain(cross1, cross2),
    "Crossed bands"
)

# ------------------------------------------------
# 4. Симметрия
# ------------------------------------------------

sym1 = tris

sym2 = list(
    map(
        tr_symmetry('x'),
        sym1
    )
)

visualize(
    chain(sym1, sym2),
    "Symmetric triangles"
)

# ------------------------------------------------
# 5. Масштабирование
# ------------------------------------------------

scaled = list(
    map(
        tr_homothety,
        [0.5, 1, 1.5, 2]
    )
)

scaled_polys = [
    transform(rects[i])
    for i, transform in enumerate(scaled)
]

visualize(
    scaled_polys,
    "Homothety"
)

# ------------------------------------------------
# 6. Фильтры
# ------------------------------------------------

filtered = list(
    filter(
        flt_short_side(1.5),
        chain(rects, tris, hexs)
    )
)

visualize(filtered, "Filtered")

# ------------------------------------------------
# 7. Aggregators
# ------------------------------------------------

all_polys = list(
    chain(rects, tris, hexs)
)

print(
    "Nearest:",
    agr_origin_nearest(all_polys)
)

print(
    "Max side:",
    agr_max_side(all_polys)
)

print(
    "Min area:",
    agr_min_area(all_polys)
)

print(
    "Total perimeter:",
    agr_perimeter(all_polys)
)

print(
    "Total area:",
    agr_area(all_polys)
)

# ------------------------------------------------
# 8. ZIP POLYGONS
# ------------------------------------------------

zipped = list(
    zip_polygons(rects, tris)
)

visualize(
    zipped,
    "Zipped polygons"
)