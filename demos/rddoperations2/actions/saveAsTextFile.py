import shutil
import os
from pyspark import SparkContext

if os.path.exists("numbersAsText"):
    shutil.rmtree("numbersAsText")

sc = SparkContext("local[*]", "SaveAsTextFile Action Demo")

numbersRdd = sc.parallelize(range(1,10000))
filteredRdd = numbersRdd.filter(lambda x: x % 1000 == 0)

filteredRdd.saveAsTextFile("numbersAsText")

sc.stop()
