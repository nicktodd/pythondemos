from pyspark import SparkContext

sc = SparkContext()

numbersRdd = sc.parallelize(range(1,10000))
filteredRdd = numbersRdd.filter(lambda x: x % 1000 == 0)

filteredRdd.saveAsTextFile("numbersAsText")
