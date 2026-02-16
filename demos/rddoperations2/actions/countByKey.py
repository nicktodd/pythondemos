from pyspark import SparkContext

sc = SparkContext("local[*]", "CountByKey Action Demo")

kvRdd = sc.parallelize( [ ["UK","London"], ["FR","Paris"], ["UK","Leeds"], ["SA","Joburg"] ] )

countByKeyResult = kvRdd.countByKey()

print("countByKeyResult: %s" % countByKeyResult)

sc.stop()


