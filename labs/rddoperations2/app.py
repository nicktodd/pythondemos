from pyspark import SparkContext
from sys import argv

sc = SparkContext("local[*]", "RDD Operations Part 2")
sc.setLogLevel("WARN")

# Read all lines from MacbethSnippet.txt.
lines = sc.textFile("MacbethSnippet.txt")


# Ex 1: Get all the words (split each line at the ' ' character). 


# Ex 2: Create an RDD of (word, count) tuples.


# Ex 3. Cache the RDD of (word, count) tuples.  


# Ex4: Take the first 100 items and print them.


# Ex 5: Perform aggregation actions.


# Ex 6: Perform key-based actions.


# Ex 7: Get just the counts, cache it, and then do some numeric actions.

sc.stop()
