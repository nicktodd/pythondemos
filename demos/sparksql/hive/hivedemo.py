from pyspark import SparkContext 
from pyspark.sql import HiveContext

# Create a SQLContext object.
sc = SparkContext("local[*]", "Hive Demo")
sqlContext = HiveContext(sc)

# Create Table using HiveQL.
sqlContext.sql(
    "CREATE TABLE IF NOT EXISTS employee(id INT, name STRING, age INT, salary INT) " + 
    "ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' " + 
    "LINES TERMINATED BY '\n'")

# Load data into table using HiveQL.
sqlContext.sql("LOAD DATA LOCAL INPATH 'employees.txt' INTO TABLE employee")

# Select fields from the table.
result = sqlContext.sql("FROM employee SELECT id, name, age, salary")

# Display the result.
result.show()

sc.stop()
