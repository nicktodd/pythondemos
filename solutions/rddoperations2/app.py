from pyspark import SparkContext
from sys import argv

sc = SparkContext("local[*]", "RDD Operations Part 2")
sc.setLogLevel("WARN")

# Read all lines from MacbethSnippet.txt.
lines = sc.textFile("MacbethSnippet.txt")


# Ex 1: Get all the words (split each line at the ' ' character). 
words = lines.flatMap(lambda line:line.split(' ')) \
             .filter(lambda word: word)
print("All words: %s" % words.collect())


# Ex 2: Create an RDD of (word, count) tuples.
wordCounts = words.map(lambda word: (word, 1)) \
                  .reduceByKey( lambda accumulatedValue, thisValue: accumulatedValue + thisValue) \
                  .sortBy(lambda wc: wc[1], False)
print("All words and counts: %s" % wordCounts.collect())


# Ex 3. Cache the RDD of (word, count) tuples. 
wordCounts.cache()


# Ex4: Take the first 100 items and print them.
print("First 100 words and counts: %s" % wordCounts.take(100))


# Ex 5: Perform aggregation actions.
count = wordCounts.count()
max   = wordCounts.max(lambda wc: wc[1])
min   = wordCounts.min(lambda wc: wc[1])
print("Number of different words: %d" % count)
print("Most frequent word: %s, count: %d" % max)
print("Least frequent word: %s, count: %d" % min)


# Ex 6: Perform key-based actions.
for w in argv[1:]:
    c = wordCounts.lookup(w)
    print("Word: %s, count: %s" % (w, c))

    
# Ex 7: Get just the counts, cache it, and then do some numeric actions.
counts = wordCounts.map(lambda wc: wc[1])
counts.cache()
sum = counts.sum()
mean = counts.mean()
stdev = counts.stdev()
variance = counts.variance()
print("Sum: %d, mean: %f, standard deviation: %f, variance: %f" % (sum, mean, stdev, variance))

sc.stop()

 
