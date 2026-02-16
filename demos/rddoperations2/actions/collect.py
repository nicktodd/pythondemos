from pyspark import SparkContext

sc = SparkContext()

numbers = sc.parallelize( [1, 2, 3, 1, 1, 2, 3, 1, 2, 1, 2, 2, 3, 4] )

collectResult = numbers.collect()

print("collectResult: %s" % collectResult)

