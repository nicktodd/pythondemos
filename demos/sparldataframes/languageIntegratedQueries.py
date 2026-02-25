from pyspark import SparkContext, StorageLevel 
from pyspark.sql import SQLContext, SparkSession
from pyspark.sql import functions as F
from entities import Customer, Product, Home, SalesByCity, Email, Transaction

# Create Spark objects.
sc = SparkContext("local[*]", "Language Integrated Queries Demo")
sc.setLogLevel("WARN")
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

# Create a DataFrame containing some more customer data.
vipCustomers = [
    Customer(7, "James", 56, "M"),
    Customer(8, "Maria", 72, "F"),
    Customer(9, "Timmy", 31, "M"),
    Customer(4, "Frank", 24, "F"),
    Customer(5, "Benny", 25, "M")
]
vipCustomerDF = sc.parallelize(vipCustomers).toDF()

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

# Create a DataFrame containing sales by city.
salesByCity = [
    SalesByCity(2014, "Paris",     "France", 2000),
    SalesByCity(2015, "Paris",     "France", 3000),
    SalesByCity(2014, "Toulouse",  "France", 2000),
    SalesByCity(2015, "Toulouse",  "France", 3000),
    SalesByCity(2014, "Bordeaux",  "France", 4000),
    SalesByCity(2015, "Bordeaux",  "France", 6000),
    SalesByCity(2014, "Bardolino", "Italy",  1000),
    SalesByCity(2015, "Bardolino", "Italy",  1000),
    SalesByCity(2015, "Sorrento",  "Italy",  1000),
    SalesByCity(2014, "Sorrento",  "Italy",  2000)
]
salesByCityDF = sc.parallelize(salesByCity).toDF()

# Create a DataFrame containing emails.
emails = [
    Email("John Smith", "Ola Nordmann", "Hei",     "Tusen takk for dokumetenter!"),
    Email("Judy Evans", "Henri du Lac", "Bonjour", "Ayez une bonne journee!"),
    Email("Pete Wilks", "Iestyn Jones", "Bore da", "Diolch yn fawr!")
]
emailDF = sc.parallelize(emails).toDF()

# Create a DataFrame containing transactions (i.e. customers who have purchased products).
transactions = [
    Transaction(1001, 1, 4, "01/01/2015", "Birmingham"),
    Transaction(1002, 2, 4, "01/02/2016", "Liverpool"),  
    Transaction(1003, 3, 5, "01/01/2016", "London"),
    Transaction(1004, 7, 5, "01/02/2016", "Swansea"),
    Transaction(1005, 8, 3, "01/02/2016", "London")
]
transactionDF = sc.parallelize(transactions).toDF()


# Main code... To run a bit of the code, change the relevant "if" test to True.

if True:
    print("\n\n========== Demo accessing a column ==================================================")
    priceColumn = productDF.price
    print(priceColumn)


if False:
    print("\n\n========== Demo filter() method =====================================================")
    filteredHomeDF = homeDF.filter(homeDF.price > 200000)
    filteredHomeDF.show()


if False:
    print("\n\n========== Demo distinct() method ===================================================")
    distinctCustomerDF = customerDF.distinct()
    distinctCustomerDF.show()


if False:
    print("\n\n========== Demo limit() method ======================================================")
    first2Customers = customerDF.limit(2)
    first2Customers.show()


if False:
    print("\n\n========== Demo orderBy() method ====================================================")

    # The simplest way to call orderBy() is with string arguments.
    orderedCustomers1 = customerDF.orderBy("gender", "age")

    # If you want to do anything fancy, you must pass in Column objects instead. 
    orderedCustomers2 = customerDF.orderBy(customerDF.gender, customerDF.age.desc())

    orderedCustomers1.show()
    orderedCustomers2.show()


if False:
    print("\n\n========== Demo agg() method ========================================================")
    # min(), max(), and count() are in pyspark.sql.functions. We alias this as F - see top of code.
    aggregatesDF = homeDF.agg(F.min(homeDF.size), F.max(homeDF.price), F.count(homeDF.city))
    aggregatesDF.show()
 

if False:
    print("\n\n========== Demo groupBy() method ====================================================")
    groupedByGender = customerDF.groupBy(customerDF.gender)

    counts  = groupedByGender.count()
    minAges = groupedByGender.min("age")
    maxAges = groupedByGender.max("age")
    avgAges = groupedByGender.mean("age")

    counts.show()
    minAges.show()
    maxAges.show()
    avgAges.show()


if False:
    print("\n\n========== Demo select() method =====================================================")

    # The simplest way to call select() is with string arguments.
    namesAgesDF = customerDF.select("name", "age")
    namesAgesDF.show()

    # If you want to do anything fancy, you must pass in Column objects instead. 
    namesAgesNextYearDF = customerDF.select(customerDF.name, customerDF.age + 1)
    namesAgesNextYearDF.show()

    # There are also a lot of built-in functions available in pyspark.sql.functions. We alias this as F - see top of code.
    minAgeDF = customerDF.select(F.min(customerDF.age))
    minAgeDF.show()

    typeDF = customerDF.select( customerDF.name,
                                F.when(customerDF.age <= 21, "student") \
                                 .when(customerDF.age <= 24, "new grad") \
                                 .otherwise("mortgaged to hilt"))
    typeDF.show()


if False:
    print("\n\n========== Demo selectExpr() method =================================================")
    newCustomerDF = customerDF.selectExpr(
      "name", 
      "65 - age AS untilRetire",
      "IF (gender = 'M', true, false) AS male")

    newCustomerDF.show()


if False:
    print("\n\n========== Demo sample() method =====================================================")
    sampleDF = customerDF.sample(True, 0.5)
    sampleDF.show()


if False:
    print("\n\n========== Demo randomSplit() method ================================================")
    dfArray = productDF.randomSplit([0.5, 0.25, 0.25])
    print(dfArray[0].collect())
    print(dfArray[1].collect())
    print(dfArray[2].collect())


if False:
    print("\n\n========== Demo cube() method =======================================================")

    # Perform the cube operation.
    salesCubeDF = salesByCityDF.cube("year", "city", "country").sum("revenue")

    # Display first 20 results.
    salesCubeDF.show(20)

    # Tidy up the columns names.
    salesCubeDF.withColumnRenamed("sum(revenue)", "total").show(20)

    # Filter out detailed rows, to just display summaries for French cities.
    salesCubeDF.filter("year IS null AND city IS NOT null AND country='France'").show(20)


if False:
    print("\n\n========== Demo rollup() method =====================================================")
    revenuesDF = salesByCityDF.rollup("country", "city").sum("revenue")
    revenuesDF.show()


if False:
    print("\n\n========== Demo intersect() method ==================================================")
    commonCustomerDF = customerDF.intersect(vipCustomerDF)
    commonCustomerDF.show()


if False:
    print("\n\n========== Demo join() method =======================================================")

    # Perform an inner join, outer join, left outer join, and right outer join.
    innerDF      = transactionDF.join(customerDF, transactionDF.custId == customerDF.cId, "inner")
    outerDF      = transactionDF.join(customerDF, transactionDF.custId == customerDF.cId, "outer")
    leftOuterDF  = transactionDF.join(customerDF, transactionDF.custId == customerDF.cId, "left_outer")
    rightOuterDF = transactionDF.join(customerDF, transactionDF.custId == customerDF.cId, "right_outer")

    # Display the results.
    innerDF.show()
    outerDF.show()
    leftOuterDF.show()
    rightOuterDF.show()

sc.stop()
