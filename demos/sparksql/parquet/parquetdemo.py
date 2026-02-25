from pyspark import SparkContext 
from pyspark.sql import SQLContext

# Create a SQLContext object.
sc = SparkContext("local[*]", "Parquet Demo")
sqlContext = SQLContext(sc)

# Create a DataFrame from a JSON file, then write out in Parquet format.
jsonDF = sqlContext.read.json("employees.json")
jsonDF.write.parquet("employees.parquet")

# Create a DataFrame containing data read in from Parquet.
parquetDF = sqlContext.read.parquet("employees.parquet")

# Create or replace a temporary view.
parquetDF.createOrReplaceTempView("employee")

# Select fields from the table.
result = sqlContext.sql("SELECT * FROM employee")

# Display the result.
result.show()

sc.stop()
