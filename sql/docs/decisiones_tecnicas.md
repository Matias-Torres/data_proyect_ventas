# Decisiones Técnicas – Pipeline de Ventas (Heladería)

## 1. Arquitectura de Datos

Se adopta una arquitectura **Medallion** en tres capas:

- **Bronze:** datos crudos provenientes del sistema de ventas (sin transformaciones, tipado mayormente `STRING`).
- **Silver:** datos limpios, normalizados y tipados.
- **Gold:** modelo analítico orientado a negocio (KPIs y agregaciones).

Esta separación permite:

- Trazabilidad del dato original  
- Reprocesamiento sin pérdida de información  
- Aislamiento de la lógica de limpieza  

---

## 2. Motor y Formato

- **Motor:** Apache Spark (Databricks)  
- **Formato de almacenamiento:** Delta Lake  

Se utiliza **Delta Lake** por:

- Soporte de `MERGE` (upsert incremental)  
- Control de versiones (**Time Travel**)  

---

## 3. Elección del Modelo

Se eligió un **Star Schema** debido a:

- Optimización para consultas de negocio (KPIs)  
- Buen rendimiento en agregaciones y filtros por dimensiones  
- Separación clara entre **hechos** y **dimensiones**  

---

## 4. Estrategia de Ingesta

La ingesta hacia **Bronze** es **append-only**.

- No se aplican validaciones en esta capa  
- Se preserva el dato tal como llega del sistema fuente  

---

## 5. Limpieza y Normalización (Bronze → Silver)

### 5.1 Tipado de Columnas

Conversión explícita de tipos:

- `precio` → DOUBLE  
- `total` → DOUBLE  
- `vtafecha` → TIMESTAMP  

---

### 5.2 Valores Nulos

Se detecta un bajo porcentaje de valores nulos en la columna `comprobante`,  
los cuales no afectan el análisis principal.

---

### 5.3 Control de Valores Inválidos

Se filtran registros con:

- `precio = 0.01`  
- `total = 0.01`  

Estos valores corresponden a inconsistencias del sistema fuente.

---

### 5.4 Normalización de Texto

Se aplican procesos de limpieza:

- Normalización a minúsculas  
- Eliminación de espacios extra  
- Eliminación de tildes  
- Remoción de caracteres especiales  

---

### 5.5 Derivación de Columnas de Negocio

Se generan nuevas variables:

- **cliente:** `socio` / `no_socio` / `gastronomico`  
- **turno:** `mañana` (10–18) / `noche`  
- **medio_pago:** `tarjeta` / `qr` / `efectivo` / `multiple_opciones` / `cancelado`  
- **categoria:** clasificación de productos  

---

## 6. Manejo de Duplicados

Se define la unicidad del registro mediante la clave compuesta:

(venta, articulo)

Se aplica:

- `ROW_NUMBER()` para conservar el registro más reciente  
- Hash MD5 para detección de cambios y soporte (SCD Type 2) con `MERGE` incremental  


