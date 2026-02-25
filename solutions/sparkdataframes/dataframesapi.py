from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, sum, avg, max, min, count

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("DataFrame API Solutions") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

DATA_PATH = "../../demos/glue-notebooks/data/weatherWithHeader.csv"

# ---------------------------------------------------------------------------
# Exercise 1 — Read and Explore
# ---------------------------------------------------------------------------
print("\n===== Exercise 1: Read and Explore =====")
df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .option("sep", ";") \
    .csv(DATA_PATH)

df.printSchema()
df.show(10)

# ---------------------------------------------------------------------------
# Exercise 2 — Select and Filter
# ---------------------------------------------------------------------------
print("\n===== Exercise 2a: Select DayOfMonth and MaxTemp =====")
df.select("DayOfMonth", "MaxTemp").show()

print("\n===== Exercise 2b: MaxTemp > 8 =====")
df.filter(col("MaxTemp") > 8).show()

print("\n===== Exercise 2c: Frost days (MinTemp < 0) =====")
df.filter(col("MinTemp") < 0).show()

# ---------------------------------------------------------------------------
# Exercise 3 — Add a Computed Column
# ---------------------------------------------------------------------------
print("\n===== Exercise 3: TempRange column =====")
df_range = df.withColumn("TempRange", col("MaxTemp") - col("MinTemp"))
df_range.select("DayOfMonth", "MinTemp", "MaxTemp", "TempRange").show()

# ---------------------------------------------------------------------------
# Exercise 4 — Categorise with a Computed Column
# ---------------------------------------------------------------------------
print("\n===== Exercise 4: RainCategory column =====")
df_rain = df.withColumn(
    "RainCategory",
    when(col("Precipitation") > 20, "Heavy")
    .when(col("Precipitation") >= 5, "Moderate")
    .otherwise("Light")
)
df_rain.select("DayOfMonth", "Precipitation", "RainCategory").show()

# ---------------------------------------------------------------------------
# Exercise 5 — Aggregations
# ---------------------------------------------------------------------------
print("\n===== Exercise 5: Whole-dataset aggregations =====")
df.select(
    sum("Precipitation").alias("total_precipitation"),
    avg("MaxTemp").alias("avg_max_temp"),
    max("MaxTemp").alias("highest_max_temp"),
    min("MinTemp").alias("lowest_min_temp"),
    count("DayOfMonth").alias("total_days")
).show()

# ---------------------------------------------------------------------------
# Exercise 6 — Find Specific Days
# ---------------------------------------------------------------------------
print("\n===== Exercise 6a: Day with highest MaxTemp =====")
df.orderBy(col("MaxTemp").desc()).limit(1).show()

print("\n===== Exercise 6b: Day with lowest MinTemp =====")
df.orderBy(col("MinTemp").asc()).limit(1).show()

print("\n===== Exercise 6c: Days with no precipitation =====")
df.filter(col("Precipitation") == 0).show()

# ---------------------------------------------------------------------------
# Exercise 7 — Sort and Rank
# ---------------------------------------------------------------------------
print("\n===== Exercise 7a: Top 10 wettest days =====")
df.orderBy(col("Precipitation").desc()).show(10)

print("\n===== Exercise 7b: Biggest TempRange days =====")
df.withColumn("TempRange", col("MaxTemp") - col("MinTemp")) \
    .orderBy(col("TempRange").desc()) \
    .show(10)

# ---------------------------------------------------------------------------
# Exercise 8 — Rename and Drop
# ---------------------------------------------------------------------------
print("\n===== Exercise 8a: Rename MinTemp and MaxTemp =====")
df.withColumnRenamed("MinTemp", "LowTemp") \
    .withColumnRenamed("MaxTemp", "HighTemp") \
    .show()

print("\n===== Exercise 8b: Drop Precipitation column =====")
df.drop("Precipitation").show()

# ---------------------------------------------------------------------------
# Bonus — Descriptive Statistics
# ---------------------------------------------------------------------------
print("\n===== Bonus: Descriptive statistics =====")
df.describe("MinTemp", "MaxTemp", "Precipitation").show()

spark.stop()
