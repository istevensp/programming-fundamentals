# Mapa curricular — Fundamentos de Programación

## Fuente y criterio de diseño

Este mapa traduce las directrices de la pestaña `Contenidos` de `FP2026-II Ayudantes.xlsx` a una estructura apta para un repositorio educativo. El orden, el alcance y las restricciones provienen de Coordinación. Los resultados de aprendizaje y las evidencias se redactaron para volver esas directrices enseñables y verificables, sin ampliar el temario.

## Propósito formativo

Al finalizar la materia, el estudiante podrá descomponer problemas básicos, representar datos con tipos y colecciones simples, construir soluciones con funciones y estructuras de control, organizar información en diccionarios de un nivel y realizar procesamiento elemental de datos tabulares con Pandas.

## Reglas transversales

1. El material obligatorio debe limitarse al alcance definido por Coordinación.
2. Los ejemplos y ejercicios deben ser comprensibles para estudiantes sin experiencia previa.
3. Las listas se trabajan en un solo nivel.
4. Los diccionarios se trabajan en un solo nivel; se permite una lista simple como valor.
5. Las funciones no deben depender de variables globales.
6. En estructuras de control no se utilizan `break`, `continue` ni `pass`.
7. No se utiliza manejo de excepciones con `try-except`.
8. En ciclos `while` se evitan banderas booleanas como mecanismo de control.
9. La visualización con Pandas o Matplotlib es complementaria y no evaluable.
10. Los temas tachados por Coordinación no deben convertirse en lecciones obligatorias.

## Progresión

```text
Unidad 01: Introducción y herramientas
    ↓
Unidad 02: Datos, strings y listas simples
    ↓
Unidad 03: Funciones y lógica booleana
    ↓
Unidad 04: Decisiones, iteración y composición de estructuras
    ↓
Unidad 05: Diccionarios de un nivel
    ↓
Unidad 06: Procesamiento tabular con Pandas
```

## Unidad 01 — Introducción a Python

**Propósito:** presentar Python como herramienta para resolver problemas y preparar el entorno de trabajo.

**Contenidos obligatorios**

- Introducción a Python.
- Ejemplos de programación aplicada a proyectos de diferentes carreras.
- Uso inicial de Spyder y Google Colab.

**Resultados de aprendizaje**

- Explicar qué papel cumple Python en la resolución de problemas.
- Reconocer aplicaciones de la programación en distintas disciplinas.
- Crear, ejecutar y revisar un programa básico en Spyder o Colab.

**Evidencias sugeridas**

- Ejecución de un programa corto en uno de los entornos autorizados.
- Explicación del problema, la entrada, el proceso y la salida de un ejemplo aplicado.

## Unidad 02 — Variables, tipos y colecciones simples

**Propósito:** representar y transformar datos utilizando los recursos básicos del lenguaje.

**Contenidos obligatorios**

- Definición de variables.
- Conversión entre tipos de datos.
- Manipulación de strings: eliminación, reemplazo y cambio de mayúsculas/minúsculas.
- Definición de listas de un nivel.
- Búsqueda de elementos, considerando valores repetidos.
- Aleatoriedad con `randint`, `choice`, `choices`, `sample` y `shuffle`.
- Salida formateada con `f-strings` o `str.format()`.

**Resultados de aprendizaje**

- Elegir tipos apropiados para datos simples.
- Convertir valores cuando una operación lo requiera.
- Transformar strings con operaciones básicas.
- Crear y consultar listas planas.
- Distinguir entre selección con reemplazo, sin reemplazo y reordenamiento aleatorio.
- Presentar resultados de manera legible.

**Límite:** no introducir listas anidadas.

## Unidad 03 — Funciones

**Propósito:** dividir una solución en operaciones reutilizables con entradas, resultados y responsabilidades claras.

**Contenidos obligatorios**

- Creación de funciones.
- Parámetros, incluidos parámetros por defecto.
- Retorno de múltiples valores.
- Funciones sin dependencia de variables globales.
- Funciones booleanas.

**Resultados de aprendizaje**

- Definir funciones con nombres y responsabilidades claras.
- Utilizar parámetros obligatorios y predeterminados.
- Retornar uno o varios resultados sin modificar estado global.
- Encapsular verificaciones en funciones booleanas.

**Fuera de alcance**

- Creación de módulos o librerías.
- Análisis profundo de parámetros por valor y referencia.
- Debate sobre ventajas y desventajas de IA.
- Vibe coding y calidad de prompts.

## Unidad 04 — Estructuras de control

**Propósito:** construir algoritmos que tomen decisiones y repitan operaciones sin atajos que oculten el flujo.

**Contenidos obligatorios**

- `if`, `if-else` e `if-elif-else`.
- `for` con `range`, colecciones y `enumerate`.
- Anidamiento de estructuras.
- Búsqueda del mayor y menor valor, con y sin empates.
- Estrategias para mantener listas sin repetidos.
- List comprehensions únicamente cuando el estudiante pueda explicar su funcionamiento.
- `while`, ubicado al final de la unidad.
- Condiciones compuestas y funciones booleanas como alternativas a banderas.

**Restricciones**

- No usar `break`, `continue` ni `pass`.
- Evitar banderas booleanas para controlar un `while`.
- No usar `try-except`.

**Resultados de aprendizaje**

- Seleccionar la estructura de control apropiada para cada problema.
- Recorrer secuencias conservando índice y valor cuando sea necesario.
- Combinar decisiones e iteraciones sin alterar artificialmente el flujo.
- Resolver máximos, mínimos, empates y duplicados mediante lógica explícita.
- Formular condiciones de terminación verificables para ciclos `while`.

## Unidad 05 — Diccionarios

**Propósito:** modelar relaciones clave–valor y resolver tareas sencillas de conteo, transformación y filtrado.

**Contenidos obligatorios**

- Diccionarios de un nivel; como máximo, una lista simple como valor.
- Conteo de frecuencias.
- Creación desde listas o cadenas con formato conocido.
- Creación a partir de otros diccionarios.
- Recorrido y filtrado.
- Inversión de claves y valores, explicando colisiones y pérdida de información.

**Resultados de aprendizaje**

- Elegir claves y valores apropiados para un problema.
- Construir tablas de frecuencia.
- Transformar información secuencial en un diccionario.
- Filtrar pares según condiciones.
- Determinar cuándo un diccionario puede invertirse de forma segura.

**Límite:** no introducir diccionarios anidados.

## Unidad 06 — Procesamiento de datos con Pandas

**Propósito:** crear, consultar, transformar y resumir datos tabulares básicos.

**Bloques obligatorios**

1. **Series y DataFrame**
   - Creación desde listas, diccionarios y arreglos unidimensionales.
   - Índices numéricos y no numéricos.
   - Selección de filas con `.loc` e `.iloc`.
   - Selección y creación de columnas.
   - `.info()`, `.describe()`, `.mean()`, `.sum()`, `.min()`, `.max()`, `.head()` y `.tail()`.
2. **Archivos CSV**
   - `pd.read_csv()` con `sep`, `header` e `index_col`.
   - `DataFrame.to_csv()` o `Series.to_csv()`.
3. **Operaciones aritméticas y lógicas**
   - Operaciones entre Series.
   - Comparaciones y filtros booleanos con `&` y `|`.
   - `.mask()` y, opcionalmente, `np.select()`.
   - `.idxmax()` y `.idxmin()`.
4. **Agregaciones y estadísticas**
   - `.sort_values()` para una o varias columnas, incluyendo `inplace=True`.
   - `.unique()`, `.value_counts()` e `.isin()`.
   - `.groupby()` por categoría.

**Resultados de aprendizaje**

- Crear y consultar estructuras tabulares sencillas.
- Seleccionar filas y columnas con criterios explícitos.
- Importar y exportar datos CSV con parámetros básicos.
- Construir filtros combinados correctamente.
- Ordenar, agrupar y resumir datos por categoría.

**Complementario y no evaluable**

- `.plot()` en Series y DataFrame.
- Gráficos de líneas, barras, histogramas y boxplots.
- Visualización de top N y bottom N.
- Gráficos agrupados por categoría.

## Criterios para generar lecciones y ejercicios

- Cada lección debe declarar su relación con un tópico `core` del YAML.
- Todo ejemplo debe respetar las restricciones globales y las de su unidad.
- Los ejercicios deben poder resolverse únicamente con contenidos ya presentados.
- Una solución que use una construcción prohibida no se considera solución modelo.
- Los contenidos complementarios deben mostrarse con una etiqueta visible de “No evaluable”.
- Los temas excluidos pueden conservarse en metadatos para prevenir su incorporación accidental, pero no deben publicarse como lecciones regulares.

