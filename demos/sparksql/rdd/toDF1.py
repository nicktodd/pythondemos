from pyspark import SparkContext 
from pyspark.sql import SQLContext, SparkSession
from employee import Employee

# Create a SparkContext object.
sc = SparkContext("local[*]", "toDF Demo")

# Create a collection of data.
employees = [
    Employee(101, "Simon Putz", 41, 1000),
    Employee(102, "Julie Evan", 42, 2000),
    Employee(103, "Micky Bale", 43, 3000),
    Employee(104, "Sarah Hill", 44, 4000)
]

# Create an RDD on the data.
employeeRDD = sc.parallelize(employees)

# Create a SparkSession, which adds toDF() method to RDD.
print("DIAGNOSTIC MESSAGE: RDD has toDF() method? %s" % hasattr(employeeRDD, "toDF"))
sparksession = SparkSession(sc)
print("DIAGNOSTIC MESSAGE: RDD has toDF() method? %s" % hasattr(employeeRDD, "toDF"))

# Create a Spark SQL DataFrame from the RDD. 
employeeDF = employeeRDD.toDF()

# Create a SQLContext object.
sqlContext = SQLContext(sc)

# Create/replace a temporary view, select fields, and display result.
employeeDF.createOrReplaceTempView("employee")
result = sqlContext.sql("SELECT id, name, age, salary FROM employee")
result.show()

sc.stop()
