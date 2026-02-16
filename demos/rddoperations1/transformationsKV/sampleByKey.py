from pyspark import SparkContext

sc = SparkContext()

pairRdd = sc.parallelize([
    ["a",100], 
    ["b",200], 
    ["a",101], 
    ["b",201], 
    ["a",102], 
    ["b",202],
    ["a",103], 
    ["b",203],
    ["a",104], 
    ["b",204],
    ["a",105], 
    ["b",205],
    ["a",106], 
    ["b",206],
    ["a",107], 
    ["b",207],
    ["a",108], 
    ["b",209],
    ["a",109], 
    ["b",209],
    ["a",110], 
    ["b",210], 
    ["a",111], 
    ["b",211], 
    ["a",112], 
    ["b",212], 
    ["a",113], 
    ["b",213], 
    ["a",114], 
    ["b",214], 
    ["a",115], 
    ["b",215], 
    ["a",116], 
    ["b",216], 
    ["a",117], 
    ["b",217], 
    ["a",118], 
    ["b",218], 
    ["a",119], 
    ["b",219], 

])

sampleRdd = pairRdd.sampleByKey(True, {"a": 0.2, "b": 0.4})
result = sampleRdd.collect()

print("result: %s" % result)

