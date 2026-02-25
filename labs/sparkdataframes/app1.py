from pyspark import SparkContext 
from pyspark.sql import SQLContext 
from util import readWeatherData

sc = SparkContext("local[*]", "Spark DataFrames Lab")
sqlContext = SQLContext(sc)

df = readWeatherData(sqlContext, "weatherWithHeader.csv")

# ------------------------------------------------------------------------------------------
# Add your code in this file, as indicated by the comments below...
# ------------------------------------------------------------------------------------------


# 1. Show the DataFrame initially, to make sure it looks good.


# 2. Display the column names.


# 3. Display the column data types.


# 4. 'Explain' the logical and physical plan of the DataFrame.


# 5. Print the schema of the DataFrame.


# 6. 'Describe' the temperature columns in the DataFrame.


# 7. Take the first 5 rows and display each row.


sc.stop()
