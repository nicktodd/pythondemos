from pyspark import SparkContext 
from pyspark.sql import SQLContext 

# Create a SQLContext object.
sc = SparkContext("local[*]", "JSON Demo")
sqlContext = SQLContext(sc)

# Create a DataFrame containing data read in from a json file.
employeeDF = sqlContext.read.json("employees.json")

# Create or replace a temporary view.
employeeDF.createOrReplaceTempView("employee")

# Select fields from the table.
result = sqlContext.sql("FROM employee SELECT id, name, age, salary")

# Display the result.
result.show()

sc.stop()
