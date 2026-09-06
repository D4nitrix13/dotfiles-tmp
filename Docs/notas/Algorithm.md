# Explicación sencilla del algoritmo de Peterson (y qué es la “sección crítica”)

**Sección crítica** = el trozo de código donde dos hilos/procesos comparten algo que **no puede usarse a la vez** (por ejemplo: escribir en un mismo archivo, sumar al mismo contador, actualizar un saldo).
Si dos entran al mismo tiempo ahí, salen resultados corruptos.

---

## Idea del algoritmo de Peterson (para 2 hilos)

Peterson propone una forma _solo con software_ para que **nunca** entren los dos a la vez a la sección crítica.

Usa dos cosas:

1. **flag\[2]**: cada hilo pone su bandera en `true` cuando _quiere entrar_.
2. **turn**: una variable que dice a quién **cede el turno** si los dos quieren entrar al mismo tiempo.

Para el hilo `i` (donde `i` es 0 o 1 y `j` es el otro):

```c
// QUIERO ENTRAR
flag[i] = true;      // levanto mi bandera
turn    = j;         // cedo el turno al otro
while (flag[j] && turn == j) {
    // espero mientras el otro también quiera
    // y sea "su turno"
}

// === SECCIÓN CRÍTICA ===
// ... usar el recurso compartido ...

flag[i] = false;     // ya salí; bajo mi bandera
// === RESTO DEL CÓDIGO ===
```

### ¿Por qué funciona?

- **Exclusión mutua**: si los dos quieren entrar, `turn` rompe el empate: solo uno pasa; el otro se queda en el `while`.
- **Sin deadlock**: si al menos uno quiere entrar y el otro no, entra sin trabarse.
- **Espera acotada (fairness básica)**: si alternan su deseo de entrar, no se “congelan” para siempre; se van turnando.

---

## Ejemplo cotidiano (fácil de visualizar)

Imagina dos personas, **Daniel (0)** y **Carol (1)**, que comparten **una impresora** (la impresora es la sección crítica):

1. Daniel quiere imprimir → `flag[0]=true`, pone `turn=1` (cede el paso si Carol también quiere).
2. Carol también quiere → `flag[1]=true`, pone `turn=0`.
3. Si los dos quieren **a la vez**, el que **no** tenga el `turn` se queda esperando en el `while`.
4. El que tiene el `turn` entra, imprime y al salir pone su `flag` en `false`.
5. El otro ve que la `flag` del primero ya es `false` y entra después.
   **Resultado:** nunca imprimen a la vez; se ordenan solitos.

---

## Mini-ejemplo con contador compartido (intuitivo)

Supón un contador global `contador=0`. Dos hilos quieren hacer `contador++` mil veces cada uno.

- **Sin** exclusión: terminas con valores incorrectos (condiciones de carrera).
- **Con Peterson** rodeando el `contador++` como sección crítica, **terminas con 2000** exactamente.

---

## Qué debes recordar

- **Sección crítica**: el bloque donde tocas datos/recursos compartidos y deben entrar **de uno en uno**.
- **Peterson**: cada hilo “levanta bandera” (quiere entrar) y “cede turno” al otro; si los dos quieren, **el turno decide** quién pasa primero.

---

## Ventajas y limitaciones (en corto)

**+** Solo software, demuestra los conceptos clave (mutua exclusión, progreso, espera acotada).
**−** Solo vale para **2 hilos** tal cual; hace **busy-wait** (consume CPU mientras espera); en hardware moderno necesitas cuidado con **memoria/orden de lectura** (barreras/atómicos). En la práctica se usan **mutex/semáforos** del sistema.

---

## Resumen en una frase

Peterson asegura que, si dos hilos quieren entrar a un recurso compartido, **solo uno entra** (el turno rompe empates) y el otro **espera** hasta que el primero salga, evitando choques en la sección crítica.
