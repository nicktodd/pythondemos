from pyspark import SparkContext 
from pyspark.sql import SQLContext, SparkSession
from employee import Employee

# Create Spark objects.
sc = SparkContext("local[*]", "toDF Demo")
sparksession = SparkSession(sc)
sqlContext = SQLContext(sc)

# Read data from a CSV file, and map to an RDD. 
employeeRDD = sc.textFile("employees.csv") \
                .map(lambda row: row.split(",")) \
                .map(lambda cols: Employee(int(cols[0]), 
                                           cols[1], 
                                           int(cols[2]),
                                           int(cols[3])))

# Create a Spark SQL DataFrame from the RDD.
employeeDF = employeeRDD.toDF()

# Create/replace a temporary view, select fields, and display result.
employeeDF.createOrReplaceTempView("employee")
result = sqlContext.sql("SELECT id, name, age, salary FROM employee")
result.show()

sc.stop()
