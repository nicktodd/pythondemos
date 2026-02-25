from pyspark import SparkContext, StorageLevel 
from pyspark.sql import SQLContext, SparkSession
from entities import Customer, Product, Home

# Create Spark objects.
sc = SparkContext("local[*]", "Spark DataFrames Basic Demo")
sparkSession = SparkSession(sc)
sqlContext = SQLContext(sc)

# Create a DataFrame containing customer data.
customers = [
    Customer(1, "David", 21, "M"),
    Customer(2, "Lydia", 22, "F"),
    Customer(3, "Peter", 23, "M"),
    Customer(4, "Frank", 24, "F"),
    Customer(5, "Benny", 25, "M")
]
customerDF = sc.parallelize(customers).toDF()

# Create a DataFrame containing product data.
products = [
    Product(1, "Bugatti", 1000000),
    Product(2, "Skis",    250),
    Product(3, "Macbook", 1500),
    Product(4, "Bible",   10),
    Product(5, "Smile",   0)
]
productDF = sc.parallelize(products).toDF()

# Create a DataFrame containing home data.
homes = [
    Home("Swansea", 1500, 4, 150000),
    Home("London",  70,   2, 500000),
    Home("Oslo",    200,  2, 250000),
    Home("SF",      85,   2, 600000)
]
homeDF = sc.parallelize(homes).toDF()


# Main code... To run a bit of the code, change the relevant "if" test to True.

if False:
    print("\n\n========== Demo columns property ====================================================")
    cols = customerDF.columns
    print("customerDF column names: %s" % cols)


if False:
    print("\n\n========== Demo dtypes property =====================================================")
    dtypes = customerDF.dtypes
    print("customerDF column types: %s" % dtypes)


if True:
    print("\n\n========== Demo explain() method ====================================================")
    extended = True
    customerDF.explain(extended)


if False:
    print("\n\n========== Demo printSchema() method ================================================")
    customerDF.printSchema()


if False:
    print("\n\n========== Demo cache() method ======================================================")
    sqlContext.setConf("spark.sql.inMemoryColumnarStorage.compressed", "true")
    sqlContext.setConf("spark.sql.inMemoryColumnarStorage.batchSize", "10000")
    customerDF.cache()


if False:
    print("\n\n========== Demo persist() method ====================================================")
    productDF.persist(StorageLevel.DISK_ONLY)


if False:
    print("\n\n========== Demo count() method ======================================================")
    print("homeDF count: %d" % homeDF.count())


if False:
    print("\n\n========== Demo first() method ======================================================")
    print(homeDF.first())


if False:
    print("\n\n========== Demo collect() method ====================================================")
    print(homeDF.collect())


if False:
    print("\n\n========== Demo take() method =======================================================")
    print(homeDF.take(3))


if False:
    print("\n\n========== Demo show() method =======================================================")
    homeDF.show(3)


if False:
    print("\n\n========== Demo describe() method ===================================================")
    homeDF.describe("size", "bedrooms", "price").show()


if True:
    print("\n\n========== Demo createOrReplaceTempView() method ==========================================")
    customerDF.createOrReplaceTempView("customer")
    countDF = sqlContext.sql("SELECT count(*) AS count FROM customer")
    countDF.show()


if False:
    print("\n\n========== Demo toDF() method =======================================================")
    df1 = sqlContext.sql("SELECT cId, name FROM customer")
    df2 = df1.toDF("customerID", "customerName")
    df1.show()
    df2.show()

sc.stop()
