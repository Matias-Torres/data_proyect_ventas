# Databricks notebook source
# MAGIC %sql
# MAGIC -- CREAR LA TABLA ventas_helados_bronze
# MAGIC DROP TABLE IF EXISTS catalog_ventas.raw.ventas_heladeria_bronze;
# MAGIC
# MAGIC CREATE TABLE catalog_ventas.raw.ventas_heladeria_bronze (
# MAGIC   succodigo STRING,
# MAGIC   turno INT,
# MAGIC   caja INT,
# MAGIC   venta INT,
# MAGIC   comprobante STRING,
# MAGIC   vtaoperacion STRING,
# MAGIC   clinombre STRING,
# MAGIC   vtaestado STRING,
# MAGIC   vtafecha STRING,
# MAGIC   usulogin STRING,
# MAGIC   condvtapos STRING,
# MAGIC   delivery STRING,
# MAGIC   articulo INT,
# MAGIC   descrip STRING,
# MAGIC   precio STRING,
# MAGIC   cant INT,
# MAGIC   total STRING,
# MAGIC   sucursal INT,
# MAGIC   cliente INT,
# MAGIC   _rescued_data STRING,
# MAGIC   _ingestion_ts TIMESTAMP,
# MAGIC   _source_file STRING
# MAGIC )
# MAGIC USING DELTA
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- VERIFICAR TABLA CREADA
# MAGIC --SHOW TABLES IN catalog_ventas.raw
