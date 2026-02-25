from pyspark import SparkContext 
from pyspark.sql import SQLContext
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Define the schema for employee data.
employeeSchema = StructType([
	StructField("id", IntegerType(), False),
	StructField("name", StringType(), False),
	StructField("age", IntegerType(), False),
	StructField("salary", IntegerType(), False)
])

# Create a SQLContext object.
sc = SparkContext("local[*]", "JSON Demo With Schema")
sqlContext = SQLContext(sc)

# Create a DataFrame containing data read in from a json file.
employeeDF = sqlContext.read.schema(employeeSchema).json("employees.json")

# Create or replace a temporary view.
employeeDF.createOrReplaceTempView("employee")

# Select fields from the table.
result = sqlContext.sql("FROM employee SELECT id, name, age, salary")

# Display the result.
result.show()

sc.stop()
