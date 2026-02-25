from pyspark import SparkContext 
from pyspark.sql import SQLContext 

sc = SparkContext("local[*]", "Spark SQL Solution")
sqlContext = SQLContext(sc)

df = sqlContext.read \
               .option("delimiter", ";") \
               .option("header", "true") \
               .csv("weatherWithHeader.csv")
               
df.show()

sc.stop()
