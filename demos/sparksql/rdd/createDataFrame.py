from pyspark import SparkContext 
from pyspark.sql import SQLContext, Row
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Create Spark objects.
sc = SparkContext("local[*]", "Create DataFrame Demo")
sqlContext = SQLContext(sc)

# Read data from a CSV file.
linesRDD = sc.textFile("employees.csv")

# Map to an RDD of Spark SQL rows.
rowsRDD = linesRDD.map(lambda row: row.split(",")) \
                  .map(lambda cols: Row(int(cols[0]), 
                                        cols[1], 
                                        int(cols[2]),
                                        int(cols[3])))

# Define the schema for employee data.
schema = StructType([
	StructField("id", IntegerType(), False),
	StructField("name", StringType(), False),
	StructField("age", IntegerType(), False),
	StructField("salary", IntegerType(), False)
])

# Read the data into a Spark SQL DataFrame.
rowsDF = sqlContext.createDataFrame(rowsRDD, schema)

# Create or replace a temporary view, select fields, and display result.
rowsDF.createOrReplaceTempView("employee")
result = sqlContext.sql("SELECT id, name, age, salary FROM employee")
result.show()

sc.stop()
