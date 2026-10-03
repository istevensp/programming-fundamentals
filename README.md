# Fundamentos de Programación (CCPG1043)

Materiales del curso **CCPG1043 Fundamentos de Programación** (ESPOL, período 2026-II),
organizados por unidad: contenido, práctica, soluciones, ejemplos ejecutables en Python
y un conjunto de datos para la unidad de Pandas.

El alcance, la secuencia y las restricciones de cada unidad provienen de la Coordinación
de Fundamentos de Programación (pestaña `Contenidos` de su hoja de cálculo oficial) — ver
[`CURRICULUM_MAP.md`](CURRICULUM_MAP.md) para una lectura humana del mapa curricular
completo.

Este contenido también se publica, renderizado, en
**[stevensantillan.com/teaching/programming-fundamentals](https://stevensantillan.com/teaching/programming-fundamentals)**.
Este repositorio es la fuente de esos materiales — clónalo si prefieres tenerlos
localmente o revisar el código Python directamente.

## Organización

```
Unidad 01 — Introducción a Python
Unidad 02 — Variables, tipos y colecciones simples
Unidad 03 — Funciones
Unidad 04 — Estructuras de control
Unidad 05 — Diccionarios
Unidad 06 — Procesamiento de datos con Pandas
```

Cada unidad tiene tres archivos asociados:

- `content/modules/<NN>-<slug>.yaml` — alcance detallado: resultados de aprendizaje,
  temas obligatorios, restricciones, temas excluidos/suplementarios, y el mapa de
  páginas de la unidad.
- `content/docs/<NN>-<slug>/*.mdx` — las páginas de la unidad (portada, contenido,
  práctica, soluciones y, cuando aplica, una ampliación suplementaria no evaluable).
- `content/materials/<NN>-<slug>.yaml` — el catálogo de materiales de esa unidad
  (título, tipo, rol y ruta de cada página/ejemplo/dataset).

## Estructura del repositorio

```
content/course.yaml    metadata del curso, política de estados, índice de unidades
content/modules/        alcance curricular por unidad (una fuente de verdad por unidad)
content/docs/            páginas MDX (portada, contenido, práctica, soluciones)
content/materials/       catálogo YAML de materiales, uno por unidad
code/                    ejemplos ejecutables en Python, uno o más por unidad
files/                   datasets públicos usados en las prácticas (CSV)
deberes/                 cuadernos de deberes (.ipynb) para abrir en Google Colab, uno por unidad
```

## Estados de contenido

- `core` — obligatorio y evaluable.
- `supplementary` — publicable, pero no evaluable (rotulado visiblemente "No evaluable").
- `excluded` — fuera del alcance oficial, no publicado como lección.
- `prohibited` — construcción que no debe aparecer en ejemplos, prácticas ni soluciones
  (por ejemplo `break`, `continue`, `pass`, `try-except` en la Unidad 04).
- `discouraged` — práctica que la Coordinación pide evitar, con la alternativa
  recomendada explicada en el contenido.

## Licencia

Este repositorio usa dos licencias distintas:

- El código fuente (`code/`) está bajo licencia **MIT** — ver [LICENSE](LICENSE).
- El material docente (`content/`, `files/`) está bajo licencia
  **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 (CC BY-NC-SA 4.0)** — ver
  [LICENSE-CONTENT.md](LICENSE-CONTENT.md).

## Autor

**Steven Santillan Padilla** — Lecturer & Researcher, ESPOL.
[stevensantillan.com](https://stevensantillan.com)
