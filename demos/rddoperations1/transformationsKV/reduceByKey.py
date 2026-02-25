from pyspark import SparkContext

sc = SparkContext()

# Key-value RDD with person names as keys and individual perk amounts as values
# Joe and Sam each have two separate perk entries
perksRdd = sc.parallelize( [ ["Joe", 1000], ["Sam", 100], ["Joe", 2000], ["Sam", 200] ] )

# reduceByKey() groups records with the same key and aggregates values with the given function
# Each person's perk values are summed: Joe -> 3000, Sam -> 300
sumRdd = perksRdd.reduceByKey(lambda x, y:  x + y)
result = sumRdd.collect()

print("result: %s" % result)
 
