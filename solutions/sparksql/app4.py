from pyspark import SparkContext 
from pyspark.sql import SQLContext 
from pyspark.sql.types import StructType, StructField, IntegerType, DoubleType

sc = SparkContext("local[*]", "Spark SQL Solution")
sqlContext = SQLContext(sc)

weatherSchema = StructType([
	StructField("DayOfMonth", IntegerType(), False),
	StructField("MinTemp", DoubleType(), False),
	StructField("MaxTemp", DoubleType(), False),
	StructField("Precipitation", DoubleType(), False)
])

df = sqlContext.read \
               .schema(weatherSchema) \
               .option("delimiter", ";") \
               .option("header", "true") \
               .csv("weatherWithHeader.csv")

df.createOrReplaceTempView("weather")

result = sqlContext.sql("FROM weather SELECT DayOfMonth, MaxTemp, MinTemp")
result.show()

sc.stop()
