# Deberes — Fundamentos de Programación (CCPG1043) · 2026-II

Cuadernos de Google Colab (`.ipynb`) que los estudiantes abren, resuelven y entregan en Canvas.
Cada deber respeta el alcance de su unidad definido por Coordinación (ver [`CURRICULUM_MAP.md`](../CURRICULUM_MAP.md)):
un deber solo exige contenidos de su unidad o de unidades anteriores, y en el caso de una unidad
dada a medias, solo lo ya visto en clase.

## Estructura

```text
deberes/
├── README.md                                          este documento
├── 01-introduccion-python/
│   ├── Deber_U01_Introduccion_Python.ipynb            publicado
│   └── Deber_U01_Introduccion_Python_SOLUCIONARIO.ipynb      local, ignorado por git
├── 02-variables-tipos-colecciones/
│   ├── Deber_U02_parte1_Variables_Tipos_Input.ipynb   publicado
│   ├── Deber_U02_parte1_Variables_Tipos_Input_SOLUCIONARIO.ipynb   local, ignorado
│   ├── Deber_U02_parte1_Adicional_7_Programas.ipynb   publicado
│   └── Deber_U02_parte1_Adicional_7_Programas_SOLUCIONARIO.ipynb   local, ignorado
└── _generador/                                        local, ignorado
    ├── gen_deberes.py                                 genera U01 y U02 parte 1
    └── gen_adicional.py                               genera U02 adicional
```

Reglas del `.gitignore` que protegen las soluciones:

```gitignore
*_SOLUCIONARIO.ipynb
deberes/_generador/
```

Los generadores también se ignoran porque contienen las soluciones en su código.

> ⚠️ Los solucionarios y los generadores existen **solo en la computadora del docente**; no están en
> GitHub. Para trabajar desde otro equipo hay que copiarlos a mano o respaldarlos aparte.

## Deberes disponibles

| Deber | Alcance permitido | Ejercicios | Comprobación | Archivo de entrega |
|---|---|---|---|---|
| **U01** — Introducción a Python | `print()` y comentarios | 5 partes (A–E) | revisión manual | `Apellido_Nombre_U01.ipynb` |
| **U02 parte 1** — Variables, tipos e input | variables, tipos, conversión, `input()`, `print()` | 4 secciones | 6 celdas 🔎 + revisión manual | `Apellido_Nombre_U02_parte1.ipynb` |
| **U02 adicional** — 7 programas | igual que U02 parte 1 | 7 programas | 3 celdas 🔎 (ej. 1–3) + ejemplo de ejecución (ej. 4–7) | `Apellido_Nombre_U02_adicional.ipynb` |

### U01 — Introducción a Python
Solo `print()` y comentarios; sin variables.
- **A.** Algoritmo vs. programa; escribir un algoritmo propio.
- **B.** Predecir salida, ordenar un algoritmo, tarjeta de presentación, cartel con `print()`.
- **C.** Errores intencionales para corregir: comilla sin cerrar, `Print`, texto sin comillas, paréntesis sin cerrar, comillas tipográficas. Python reporta primero los tres `SyntaxError` (de arriba hacia abajo) y al final el `NameError`, porque este ocurre en ejecución.
- **D.** Entrada–proceso–salida (cafetería), concretar un problema amplio, problema de la propia carrera con prototipo de salida.
- **E.** Mismo programa en Spyder y Colab; tabla comparativa.

### U02 parte 1 — Variables, tipos e input
Cubre lo dado hasta el momento: variables, tipos, conversión e `input()`.
Excluye lo que falta de la unidad: métodos de strings, listas, `random`, f-strings y `str.format()`.
- **1. Variables:** ficha del estudiante, nombres válidos, reasignación, intercambio con auxiliar.
- **2. Tipos:** predecir `type()`, elegir el tipo adecuado (cédula y teléfono como `str` por el 0 inicial).
- **3. Conversión:** ocho expresiones "¿funciona o da error?" (`int("3.9")`, `float("1,72")`, `bool("False")`…), mensaje con `str()`, corregir `"40" + "35"`.
- **4. `input()`:** comprobar que devuelve `str`, corregir un `TypeError`, edad, promedio, °C → °F, consumo eléctrico.

En el 3.2, dos celdas producen `ValueError` a propósito; el estudiante debe comentarlas con `#` después de observar el error, para que "Reiniciar y ejecutar todo" termine sin errores.

### U02 adicional — 7 programas
Solo código, mismo alcance que la parte 1.

| # | Programa | Comprobación |
|---|---|---|
| 1 | Compra en la papelería (subtotal, IVA 15 %, total) | 🔎 |
| 2 | 135 min → 2 h y 15 min, usando `int()` (sin `//` ni `%`) | 🔎 |
| 3 | Etiqueta de un lote con `+` y `str()` | 🔎 |
| 4 | Índice de masa corporal | ejemplo de ejecución |
| 5 | Velocidad promedio (1 h 45 min = 1.75 h) | ejemplo de ejecución |
| 6 | Nota ponderada 35/35/30 | ejemplo de ejecución |
| 7 | Dividir la cuenta con propina | ejemplo de ejecución |

**Supuestos a revisar:** la ponderación 35/35/30 del ejercicio 6 y la tarifa de 0.10 USD/kWh del ejercicio 4.6 de la parte 1 son valores de ejemplo, y así se indica en los enunciados.

## Diseño común de los cuadernos

- **Portada:** nombre del estudiante, paralelo y fecha de entrega.
- **Instrucciones**, siempre con la misma estructura: **Cómo trabajar · ✅ Debes · ❌ No debes · 📤 Entrega**. Allí se declara el alcance permitido y lo prohibido de cada deber, junto con las reglas comunes:
  - no modificar las celdas de enunciado ni las de comprobación;
  - no escribir resultados a mano;
  - no entregar código que no se pueda explicar;
  - entregar solo el `.ipynb`.
- **Espacios de trabajo:** `# TU CÓDIGO AQUÍ`, variables inicializadas en `None` y celdas de texto con _Tu respuesta:_.
- **Celdas 🔎 Comprobación:** usan `assert` con mensajes que orientan la corrección y muestran ✅ cuando el ejercicio está bien. Son infraestructura de revisión: usan `assert` y, en algún mensaje, un f-string, aunque los estudiantes todavía no conocen esa sintaxis.
- **Ejercicios con `input()`:** no tienen comprobación automática. Llevan un ejemplo de ejecución que el estudiante debe reproducir.

## Solucionarios y regeneración

Los cuadernos **no se editan a mano**: se generan con los scripts de `_generador/`, que producen la
versión del estudiante y el solucionario desde la misma fuente. Así, enunciado y solución
quedan siempre alineados.

Para regenerar después de cambiar un script, ejecuta esto desde la raíz del repositorio:

```powershell
python deberes/_generador/gen_deberes.py $env:TEMP\deberes_gen
python deberes/_generador/gen_adicional.py $env:TEMP\deberes_gen
```

Después copia cada `.ipynb` generado a la carpeta de su unidad. Los scripts escriben los seis
archivos en una sola carpeta.

Al ejecutarse, cada script verifica y muestra en consola lo siguiente:
1. el solucionario se ejecuta completo sin errores, con `input()` simulado;
2. todas las celdas 🔎 del solucionario muestran ✅;
3. la versión del estudiante sin resolver falla donde debe;
4. en el adicional, las salidas de los ejemplos de ejecución coinciden exactamente con la ejecución real;
5. las soluciones no contienen construcciones fuera de alcance. Para U01: asignaciones, `input`, `if`, ciclos, funciones, listas e `import`. Para U02: `if`, ciclos, `def`, `import`, f-strings, `.format()`, métodos de strings, listas, `round`, `break`, `continue`, `pass`, `try` y `global`.

Antes de publicar un cambio, todas esas verificaciones deben pasar.

## Publicación

### Enlaces para abrir en Colab
Colab abre cuadernos directamente desde este repositorio público, sin descargar ni subir archivos:

```text
https://colab.research.google.com/github/istevensp/programming-fundamentals/blob/main/deberes/<carpeta>/<archivo>.ipynb
```

| Deber | Enlace |
|---|---|
| U01 | <https://colab.research.google.com/github/istevensp/programming-fundamentals/blob/main/deberes/01-introduccion-python/Deber_U01_Introduccion_Python.ipynb> |
| U02 parte 1 | <https://colab.research.google.com/github/istevensp/programming-fundamentals/blob/main/deberes/02-variables-tipos-colecciones/Deber_U02_parte1_Variables_Tipos_Input.ipynb> |
| U02 adicional | <https://colab.research.google.com/github/istevensp/programming-fundamentals/blob/main/deberes/02-variables-tipos-colecciones/Deber_U02_parte1_Adicional_7_Programas.ipynb> |

Colab abre el cuaderno sin pedir inicio de sesión. El estudiante debe guardar su copia
(**Archivo → Guardar una copia en Drive**) antes de trabajar; si no lo hace, pierde los cambios al
cerrar la pestaña. Si se corrige un cuaderno ya publicado, el enlace muestra la versión nueva, pero
quien ya guardó su copia conserva la anterior.

### Canvas
1. Crea la tarea y, en **Tipo de entrega**, elige **Carga de archivos** con extensión `ipynb`.
2. Cambia el editor al modo HTML (ícono `</>`) y pega la plantilla de abajo.
3. Reemplaza `PEGA_AQUI_EL_LINK_DE_COLAB` y `[código]` (`U01`, `U02_parte1` o `U02_adicional`).
4. Revisa el botón desde la **vista de estudiante** antes de publicar.

Canvas elimina `<style>` y `<script>`, por eso la plantilla usa solo estilos *inline*. Haz los cambios
siempre desde el editor HTML: si guardas desde el editor visual, Canvas puede limpiar parte del código.
La app móvil puede ignorar los bordes redondeados.

<details>
<summary>Plantilla HTML para Canvas</summary>

```html
<div style="max-width: 720px; margin: 0 auto; font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #1f2937; line-height: 1.5;">

  <!-- Encabezado -->
  <div style="background-color: #1e3a8a; color: #ffffff; padding: 22px 26px; border-radius: 14px 14px 0 0;">
    <p style="margin: 0; font-size: 13px; letter-spacing: 1.5px; text-transform: uppercase; color: #bfdbfe;">Fundamentos de Programación</p>
    <h2 style="margin: 6px 0 0 0; font-size: 24px; color: #ffffff;">🐍 Cómo realizar y entregar este deber</h2>
  </div>

  <div style="border: 1px solid #dbe3f0; border-top: none; border-radius: 0 0 14px 14px; padding: 22px 26px; background-color: #ffffff;">

    <!-- Paso 1 -->
    <div style="margin-bottom: 18px;">
      <span style="display: inline-block; width: 30px; height: 30px; line-height: 30px; text-align: center; border-radius: 50%; background-color: #2563eb; color: #ffffff; font-weight: bold; margin-right: 10px;">1</span>
      <strong style="font-size: 16px;">Abre el cuaderno</strong>
      <p style="margin: 10px 0 10px 40px;">
        <!-- ▼▼ CAMBIA PEGA_AQUI_EL_LINK_DE_COLAB POR EL ENLACE DEL DEBER ▼▼ -->
        <a href="PEGA_AQUI_EL_LINK_DE_COLAB" target="_blank" style="display: inline-block; background-color: #f9ab00; color: #1f2937; text-decoration: none; font-weight: bold; padding: 10px 22px; border-radius: 8px; font-size: 15px;">🚀 Abrir en Google Colab</a>
      </p>
      <p style="margin: 0 0 0 40px;">Antes de escribir nada, guarda tu propia copia:
        <span style="background-color: #eff6ff; border: 1px solid #bfdbfe; border-radius: 6px; padding: 2px 8px; font-family: Consolas, monospace; font-size: 13px; white-space: nowrap;">Archivo → Guardar una copia en Drive</span>
      </p>
      <p style="margin: 8px 0 0 40px; font-size: 14px; color: #92400e; background-color: #fffbeb; border-radius: 6px; padding: 6px 10px;">⚠️ Si no guardas tu copia, tus cambios se pierden al cerrar la pestaña.</p>
    </div>

    <!-- Paso 2 -->
    <div style="margin-bottom: 18px;">
      <span style="display: inline-block; width: 30px; height: 30px; line-height: 30px; text-align: center; border-radius: 50%; background-color: #2563eb; color: #ffffff; font-weight: bold; margin-right: 10px;">2</span>
      <strong style="font-size: 16px;">Resuelve</strong>
      <p style="margin: 6px 0 0 40px;">Sigue las instrucciones que están <strong>dentro del cuaderno</strong>.</p>
    </div>

    <!-- Paso 3 -->
    <div style="margin-bottom: 18px;">
      <span style="display: inline-block; width: 30px; height: 30px; line-height: 30px; text-align: center; border-radius: 50%; background-color: #2563eb; color: #ffffff; font-weight: bold; margin-right: 10px;">3</span>
      <strong style="font-size: 16px;">Verifica</strong>
      <p style="margin: 6px 0 0 40px;">Antes de entregar, ejecuta
        <span style="background-color: #eff6ff; border: 1px solid #bfdbfe; border-radius: 6px; padding: 2px 8px; font-family: Consolas, monospace; font-size: 13px; white-space: nowrap;">Entorno de ejecución → Reiniciar y ejecutar todo</span>
        y comprueba que <strong>no haya errores</strong>.
      </p>
    </div>

    <!-- Paso 4 -->
    <div style="margin-bottom: 4px;">
      <span style="display: inline-block; width: 30px; height: 30px; line-height: 30px; text-align: center; border-radius: 50%; background-color: #2563eb; color: #ffffff; font-weight: bold; margin-right: 10px;">4</span>
      <strong style="font-size: 16px;">Entrega</strong>
      <p style="margin: 6px 0 0 40px;">Descarga tu cuaderno con
        <span style="background-color: #eff6ff; border: 1px solid #bfdbfe; border-radius: 6px; padding: 2px 8px; font-family: Consolas, monospace; font-size: 13px; white-space: nowrap;">Archivo → Descargar → Descargar .ipynb</span>
        y súbelo aquí con este nombre:
      </p>
    </div>

    <!-- Nombre del archivo -->
    <div style="margin: 12px 0 0 40px; background-color: #ecfdf5; border-left: 5px solid #10b981; border-radius: 8px; padding: 12px 16px;">
      <span style="font-size: 13px; color: #047857; font-weight: bold;">📄 NOMBRE DEL ARCHIVO</span><br>
      <span style="font-family: Consolas, monospace; font-size: 17px; color: #064e3b;">Apellido_Nombre_[código].ipynb</span>
    </div>

  </div>
</div>
```

</details>

## Decisión: carpeta en GitHub en lugar de GitHub Classroom

Para las primeras unidades se usa una carpeta en este repositorio con enlaces "Abrir en Colab", y la
entrega se hace en Canvas. Se descartó GitHub Classroom por tres razones:
- obligaría a estudiantes que recién empiezan a crear cuenta en GitHub y a usar Git;
- las celdas 🔎 ya cubren la comprobación automática básica;
- las entregas y las notas quedarían repartidas entre dos plataformas.

Classroom puede reconsiderarse en unidades posteriores (Funciones, Pandas) si se quiere enseñar Git
o calificar con pruebas que el estudiante no pueda modificar.

## Agregar un deber nuevo

1. Confirma el alcance en el YAML del módulo (`content/modules/`) y lo que ya se dio en clase.
2. Escribe el generador en `_generador/` con el mismo bloque de instrucciones y la versión del estudiante y del solucionario.
3. Ejecútalo y comprueba que pasen las cinco verificaciones de la sección anterior.
4. Copia el cuaderno del estudiante y el solucionario a `deberes/<NN>-<slug>/`. El solucionario debe terminar en `_SOLUCIONARIO.ipynb` para que git lo ignore.
5. Registra el cuaderno del estudiante en `content/materials/<NN>-<slug>.yaml` con `type: notebook` y `role: assignment`.
6. Agrega su fila a las tablas de este documento.
7. Antes del commit, confirma con `git status` que no aparezca ningún solucionario.
