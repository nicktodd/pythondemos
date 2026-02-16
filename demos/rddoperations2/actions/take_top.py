from pyspark import SparkContext

sc = SparkContext("local[*]", "Take Top Action Demo")

numbers = sc.parallelize( [1, 2, 3, 1, 1, 2, 3, 1, 2, 1, 2, 2, 3, 4] )

take5        = numbers.take(5)
takeOrdered5 = numbers.takeOrdered(5)
top5         = numbers.top(5)

print("take5: %s, takeOrdered5: %s, top5: %s" % (take5, takeOrdered5, top5))

sc.stop()


