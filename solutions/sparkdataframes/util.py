from pyspark.sql.types import StructType, StructField, IntegerType, DoubleType

def readWeatherData(sqlContext, filename) :
    
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
                   .csv(filename)

    return df
