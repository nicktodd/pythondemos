from pyspark import SparkContext, StorageLevel 
from pyspark.sql import SQLContext, SparkSession
from pyspark.sql import functions as F
from entities import Customer, Product, Home

# Create Spark objects.
sc = SparkContext("local[*]", "Output Demo")
sc.setLogLevel("WARN")
sparkSession = SparkSession(sc)
sqlContext = SQLContext(sc)

# Create a DataFrame containing customer data.
customers = [
    Customer(1, "David", 21, "M"),
    Customer(2, "Lydia", 22, "F"),
    Customer(3, "Peter", 23, "M"),
    Customer(4, "Frank", 24, "F"),
    Customer(5, "Benny", 25, "M"),
    Customer(6, "Maria", 26, "F")
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
    print("\n\n========== Demo write.json() method =================================================")
    customerDF.write.json("customerJson")


if False:
    print("\n\n========== Demo write.jdbc() method =================================================")

    # Specify JDBC connection info.
    jdbcUrl    = "jdbc:derby://localhost:1527/C:/PySparkDev/MyDatabase"
    tableName  = "MySchema.Customers"
    properties = { "driver": "org.apache.derby.jdbc.ClientDriver"}

    # Write DataFrame to the table.
    customerDF.write.jdbc(url=jdbcUrl, table=tableName, mode="overwrite", properties=properties)
    
    
if False:
    print("\n\n========== Demo write.parquet() method ==============================================")
    customerDF.write.parquet("customerParquet")

    
if False:
    print("\n\n========== Demo write.saveAsTable() method ==========================================")
    customerDF.write.saveAsTable("customer")

sc.stop()
