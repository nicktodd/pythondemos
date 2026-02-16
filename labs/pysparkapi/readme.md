# Using the PySpark API

## Overview

This lab gives you an opportunity to start using the PySpark API to
perform simple RDD operations. We\'ll take a much closer look at RDD
operations in the next chapter as well.

## Source folders

- \\BigData\\Student\\03-PySparkApi

- \\BigData\\Solutions\\03-PySparkApi

## Roadmap

There are 3 exercises in this lab, of which the last exercise is \"if
time permits\". Here is a brief summary of the tasks you will perform in
each exercise; more detailed instructions follow later:

1.  Submitting a Python script to PySpark

2.  Performing RDD operations

3.  (If Time Permits) Saving RDDs

##  Exercise 1: Submitting a Python script to PySpark

In the *student* folder, open app.py in a text editor. Add the following
statement to print a message:

print(\"Hello World\\n\")

Save the file (but keep it open in the text editor, you\'ll continue
working with this file later).

Open a Command Prompt window in the *student* folder and submit the
Python script to PySpark as follows:

spark-submit app.py

This starts PySpark and executes the Python script. You should see
*Hello World* displayed.

## Exercise 2: Performing RDD operations

Modify app.py in the text editor as follows:

- Add an import statement, to import the SparkContext class from the
  pyspark package. Then create a SparkContext object and store it in a
  variable named sc, for example.

- Call the sc.textFile() method to open \"Macbeth.txt\". This method
  returns an RDD of strings, i.e. all the lines in the file. Assign the
  result to a variable named lines, for example.

- Call lines.count() to count the number of items in the RDD (i.e. the
  number of lines in the file). Print the result.

- Call lines.first() to obtain the first item in the RDD (i.e. the first
  line in the file). Print the result.

- Call lines.filter() to filter the lines, and print the result. Note
  that the filter() function takes a lambda expression as a parameter.
  The following statement shows how to write a lambda in Python, to
  retain lines that contain the word \"Witch\":

witchLines = lines.filter(lambda line: \"Witch\" in line)

Save app.py, then return to the Command Prompt window and submit app.py
to PySpark again. All being well, the application should display the
following results:

- Number of lines: 4102

- First line: ACT I

- Witch lines: *(A collection of RDD objects)*

## Exercise 3 (If time permits): Saving RDDs 

Modify app.py so that it saves the witchLines RDD to a directory named
\"witches\". Submit the script to PySpark. Upon completion you should
now have a folder named witches with files named something like
part-00000. Take a look at these files and verify they make sense.
