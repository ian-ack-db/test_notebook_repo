# Databricks notebook source
# MAGIC %pip install mlflow

# COMMAND ----------

import mlflow
import time

# Create a basic run and metric
with mlflow.start_run() as mlflow_run:
  mlflow_client = mlflow.MlflowClient()
  mlflow_client.log_metric(mlflow_run.info.run_id, "test_metric", 0.99, step=0)
