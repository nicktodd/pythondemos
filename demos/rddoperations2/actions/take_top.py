from pyspark import SparkContext

sc = SparkContext("local[*]", "Take Top Action Demo")

numbers = sc.parallelize( [1, 2, 3, 1, 1, 2, 3, 1, 2, 1, 2, 2, 3, 4] )

# take(n) returns the first n elements from the RDD in their current order
take5        = numbers.take(5)
# takeOrdered(n) returns the n SMALLEST elements in ascending order
takeOrdered5 = numbers.takeOrdered(5)
# top(n) returns the n LARGEST elements in descending order
top5         = numbers.top(5)

print("take5: %s, takeOrdered5: %s, top5: %s" % (take5, takeOrdered5, top5))

sc.stop()


