from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('PySpark Installation Test').getOrCreate()

print("PySpark installed successfully!")
print("Spark version:", spark.version)

# Stop the Spark session
spark.stop()