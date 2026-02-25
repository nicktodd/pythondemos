# Using the PySpark API

## Overview

This lab gives you an opportunity to start using the PySpark API to
perform simple RDD operations. We\'ll take a much closer look at RDD
operations in the next chapter as well.

## Source folders

- labs/pysparkapi (student folder)

- solutions/pysparkapi (solutions folder)

## Roadmap

There are 2 exercises in this lab, of which the last exercise is \"if
time permits\". Here is a brief summary of the tasks you will perform in
each exercise; more detailed instructions follow later:

1. Performing RDD operations

2. (If Time Permits) Saving RDDs


## Exercise 1: Performing RDD operations

Modify app.py in the text editor as follows:

- Add an import statement, to import the SparkContext class from the
  pyspark package. Then create a SparkContext object with "local[*]" as the master
  and store it in a variable named sc, for example:

sc = SparkContext("local[*]", "PySpark API Lab")

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

Save app.py, then return to the Command Prompt window and run app.py
locally again. All being well, the application should display the
following results:

- Number of lines: 4102

- First line: ACT I

- Witch lines: *(A collection of RDD objects)*

## Exercise 2 (If time permits): Saving RDDs 

Modify app.py so that it saves the witchLines RDD to a directory named
\"witches\". Add cleanup code at the beginning to remove any existing "witches" directory.
Submit the script by running python app.py locally. Upon completion you should
now have a folder named witches with files named something like
part-00000. Take a look at these files and verify they make sense.
