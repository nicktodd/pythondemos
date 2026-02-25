import shutil
import os
from pyspark import SparkContext

# Remove the output directory if it already exists to avoid write conflicts
if os.path.exists("numbersAsText"):
    shutil.rmtree("numbersAsText")

sc = SparkContext("local[*]", "SaveAsTextFile Action Demo")

# Create an RDD of numbers 1 to 9999
numbersRdd = sc.parallelize(range(1,10000))
# Filter to keep only multiples of 1000
filteredRdd = numbersRdd.filter(lambda x: x % 1000 == 0)

# saveAsTextFile() writes the RDD to a directory, one file per partition
filteredRdd.saveAsTextFile("numbersAsText")

sc.stop()
