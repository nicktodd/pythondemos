from pyspark import SparkContext 
from pyspark.sql import SQLContext 

sc = SparkContext("local[*]", "Spark SQL Solution")
sqlContext = SQLContext(sc)

df = sqlContext.read.csv("weather.csv")
df.show()

sc.stop()
