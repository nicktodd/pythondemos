from pyspark import SparkContext 
from pyspark.sql import SQLContext 
from pyspark.sql import functions as F
from util import readWeatherData

sc = SparkContext("local[*]", "Spark DataFrames Solution")
sqlContext = SQLContext(sc)

df = readWeatherData(sqlContext, "weatherWithHeader.csv")


# 1. Create a DataFrame with the following info:
#    - Days where the precipitation was > 30mm
#    - Eliminate any duplicates
#    - Sort the results by descending precipitation
#    - Only return the 10 wettest days
wetDF = df.filter(df.Precipitation > 30) \
          .distinct() \
          .orderBy(df.Precipitation.desc()) \
          .limit(10)
wetDF.show()


# 2. Get the following statisical info:
#    - The highest maximum temperature
#    - The lowest minimum temperature
#    - The average precipitation, to 2 decimal places
stats = df.agg(
            F.max(df.MaxTemp).alias("Highest temp"), 
            F.min(df.MinTemp).alias("Lowest temp"), 
            F.round(F.mean(df.Precipitation), 2).alias("Avg Precip")
        )
stats.show()


# 3. Create a DataFrame with the following info:
#    - Data for the first 31 days of the year (i.e. January)
#    - The day of the month
#    - The precipitation
#    - A string indicating if a day was DRY (0mm rainfall), DAMP (<10mm rainfall), or WET.
preciptationCategorizedDF = df.limit(31) \
                              .select(df.DayOfMonth, 
                                      df.Precipitation,
                                      F.when(df.Precipitation == 0, "DRY") \
                                      .when(df.Precipitation < 10, "DAMP") \
                                      .otherwise("WET")
                                      .alias("Category")
                                     )
preciptationCategorizedDF.show(31)


# 4. Create a DataFrame with info in Americanized units as follows:
#    - The maximum temperature in Fahrenheit
#    - The minimum temperature in Fahrenheit 
#    - The precipitation in inches
usaDF = df.selectExpr(
                "ROUND((32.0 + MaxTemp * 9 / 5),2) AS MaxTemp_Fahr", 
                "ROUND((32.0 + MinTemp * 9 / 5),2) AS MinTemp_Fahr",
                "ROUND((Precipitation * 0.254),2)  AS Precip_Inches")
usaDF.show()                


sc.stop()
