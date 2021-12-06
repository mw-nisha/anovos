import sys
import os

import pytest
from pyspark.sql import SparkSession

sys.path.insert(0, './dist/anovos.zip')
sys.path.insert(0, os.path.abspath("./main"))
print(sys.path)

@pytest.fixture(scope="session")
def spark_session():
    spark_jars_packages = ["io.github.histogrammar:histogrammar_2.11:1.0.20",
                           "io.github.histogrammar:histogrammar-sparksql_2.11:1.0.20",
                           "org.apache.spark:spark-avro_2.11:2.4.0"]
    spark_builder = SparkSession.builder.master("local[*]").appName("anovos_test")
    spark_builder.config('spark.jars.packages', ','.join(list(spark_jars_packages)))
    spark = spark_builder.getOrCreate()
    return spark
