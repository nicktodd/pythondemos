from pyspark import SparkContext 
from pyspark.sql import SQLContext 
from util import readWeatherData

sc = SparkContext("local[*]", "Spark DataFrames Lab")
sqlContext = SQLContext(sc)

df = readWeatherData(sqlContext, "weatherWithHeader.csv")

# ------------------------------------------------------------------------------------------
# Add your code in this file, as indicated by the comments below...
# ------------------------------------------------------------------------------------------


# 1. Create a DataFrame with the following info:
#    - Days where the precipitation was > 30mm
#    - Eliminate any duplicates
#    - Sort the results by descending precipitation
#    - Only return the 10 wettest days



# 2. Get the following statisical info:
#    - The highest maximum temperature
#    - The lowest minimum temperature
#    - The average precipitation, to 2 decimal places



# 3. Create a DataFrame with the following info:
#    - Data for the first 31 days of the year (i.e. January)
#    - The day of the month
#    - The precipitation
#    - A string indicating if a day was DRY (0mm rainfall), DAMP (<10mm rainfall), or WET.



# 4. Create a DataFrame with info in Americanized units as follows:
#    - The maximum temperature in Fahrenheit
#    - The minimum temperature in Fahrenheit 
#    - The precipitation in inches


sc.stop()
