from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext("local[*]", "Spark SQL Lab")
sqlContext = SQLContext(sc)

# Add your code here :-)

sc.stop()

