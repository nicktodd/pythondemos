from pyspark import SparkContext 
from pyspark.sql import SQLContext

# Specify JDBC connection info.
jdbcUrl    = "jdbc:derby://localhost:1527/C:/PySparkDev/MyDatabase"
tableName  = "MySchema.Employees"
properties = { 
    "driver": "org.apache.derby.jdbc.ClientDriver"
#   "user": "someUser",
#   "password": "somePassword"
}

# Create a SQLContext object.
sc = SparkContext("local[*]", "RDBMS Demo")
sqlContext = SQLContext(sc)

# Create a DataFrame containing data read in from a table in a relational database.
jdbcDF = sqlContext.read.jdbc(url=jdbcUrl, table=tableName, properties=properties)

# Create or replace a temporary view.
jdbcDF.createOrReplaceTempView("employee")

# Select fields from the table.
result = sqlContext.sql("FROM employee SELECT EMPLOYEEID, NAME, SALARY, REGION")

# Display the result.
result.show()

# Stop the SparkContext.
sc.stop()