from pyspark import SparkContext
import shutil
import os

# Clean up output folder if it exists
if os.path.exists("lengths-output"):
    shutil.rmtree("lengths-output")

sc = SparkContext("local[*]", "Simple PySpark Demo")

inputFile = sc.textFile("Macbeth.txt")

lengths = inputFile.map(lambda line: len(line))

# Use collect() to avoid Hadoop file system dependencies on Windows
results = lengths.collect()

# Write output manually
os.makedirs("lengths-output")
with open("lengths-output/part-00000", "w") as f:
    for length in results:
        f.write(f"{length}\n")

sc.stop()
print(f"Done! Processed {len(results)} lines.")