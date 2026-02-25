from pyspark import SparkContext 
from pyspark.sql import SQLContext 
from util import readWeatherData

sc = SparkContext("local[*]", "Spark DataFrames Solution")
sqlContext = SQLContext(sc)

df = readWeatherData(sqlContext, "weatherWithHeader.csv")

# 1. Show the DataFrame initially, to make sure it looks good.
df.show()


# 2. Display the column names.
cols = df.columns
print("DataFrame column names: %s" % cols)


# 3. Display the column data types.
dtypes = df.dtypes
print("DataFrame column types: %s" % dtypes)


# 4. 'Explain' the logical and physical plan of the DataFrame.
df.explain(True)


# 5. Print the schema of the DataFrame.
df.printSchema()


# 6. 'Describe' the temperature columns in the DataFrame.
df.describe("MaxTemp", "MinTemp").show()


# 7. Take the first 5 rows and display each row.
for row in df.take(5):
    print(row)



sc.stop()
