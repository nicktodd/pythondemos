from pyspark import SparkContext 
from pyspark.sql import SQLContext 
from pyspark.sql.types import StructType, StructField, IntegerType, DoubleType
from pyspark.sql.functions import col, round

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

result = sqlContext.sql("FROM weather SELECT DayOfMonth, MaxTemp, MinTemp") \
                   .withColumn("DiurnalRange", round(col("MaxTemp") - col("MinTemp"), 2))
result.show()

result2 = sqlContext.sql("FROM weather SELECT DayOfMonth, MaxTemp, MinTemp, ROUND(MaxTemp - MinTemp, 2) as DiurnalRange")
result2.show()

sc.stop()
