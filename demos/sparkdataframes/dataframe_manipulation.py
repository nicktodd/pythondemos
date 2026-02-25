from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, round, avg, sum, max, min, count, concat, upper

# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("DataFrame Manipulation Demo") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# ---------------------------------------------------------------------------
# 1. Read JSON into a DataFrame
# ---------------------------------------------------------------------------
print("\n===== 1. Read JSON =====")
df = spark.read.json("../sparksql/json/employees.json")
df.printSchema()
df.show()

# ---------------------------------------------------------------------------
# 2. Select specific columns
# ---------------------------------------------------------------------------
print("\n===== 2. Select columns =====")
df.select("name", "salary").show()

# ---------------------------------------------------------------------------
# 3. Filter rows
# ---------------------------------------------------------------------------
print("\n===== 3. Filter: salary > 2000 =====")
df.filter(col("salary") > 2000).show()

print("\n===== 3b. Filter: age between 42 and 43 =====")
df.filter(col("age").between(42, 43)).show()

# ---------------------------------------------------------------------------
# 4. Add computed columns with withColumn
# ---------------------------------------------------------------------------
print("\n===== 4. Add computed columns =====")

# Tax at 20%, annual bonus of 10% of salary, and uppercase name
enriched = df \
    .withColumn("tax",   round(col("salary") * lit(0.20), 2)) \
    .withColumn("bonus", round(col("salary") * lit(0.10), 2)) \
    .withColumn("take_home", round(col("salary") - col("salary") * lit(0.20), 2)) \
    .withColumn("name_upper", upper(col("name")))

enriched.show()

# ---------------------------------------------------------------------------
# 5. Aggregations — sum, avg, max, min, count across the whole dataset
# ---------------------------------------------------------------------------
print("\n===== 5. Whole-dataset aggregations =====")
df.select(
    sum("salary").alias("total_salary"),
    avg("salary").alias("avg_salary"),
    max("salary").alias("max_salary"),
    min("salary").alias("min_salary"),
    count("id").alias("employee_count"),
).show()

# ---------------------------------------------------------------------------
# 6. GroupBy + aggregation
# ---------------------------------------------------------------------------
print("\n===== 6. GroupBy age, sum and avg salary =====")
df.groupBy("age") \
    .agg(
        sum("salary").alias("total_salary"),
        avg("salary").alias("avg_salary"),
        count("id").alias("headcount")
    ) \
    .orderBy("age") \
    .show()

# ---------------------------------------------------------------------------
# 7. Sort / orderBy
# ---------------------------------------------------------------------------
print("\n===== 7. Order by salary descending =====")
df.orderBy(col("salary").desc()).show()

# ---------------------------------------------------------------------------
# 8. Drop a column
# ---------------------------------------------------------------------------
print("\n===== 8. Drop the 'id' column =====")
df.drop("id").show()

# ---------------------------------------------------------------------------
# 9. Rename a column
# ---------------------------------------------------------------------------
print("\n===== 9. Rename 'salary' to 'annual_salary' =====")
df.withColumnRenamed("salary", "annual_salary").show()

# ---------------------------------------------------------------------------
# 10. Descriptive statistics
# ---------------------------------------------------------------------------
print("\n===== 10. Describe (basic stats) =====")
df.describe("age", "salary").show()

spark.stop()
