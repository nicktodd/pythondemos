# RDD Operations

# Part Two

## Overview

This lab continues our journey through RDD operations. In this lab
you\'ll get a chance to use various RDD action methods, as well as some
more practice using RDD transformation methods.

All the exercises will be based on the text in MacbethSnippet.txt, an
abbreviated version of the text file you worked with earlier. You\'ll
perform a variety of operations such as obtaining the count of each
word, finding the words that appear most often and least often, and so
on.

## Source folders

- labs/rddoperations2 (student folder)

- solutions/rddoperations2 (solutions folder)

## Roadmap

There are 7 exercises in this lab, of which the last two exercises are
\"if time permits\". Here is a brief summary of the tasks you will
perform in each exercise; more detailed instructions follow later:

1.  Mapping lines of text to a flat map of words

2.  Creating an RDD of (word, count) tuples

3.  Caching the RDD of (word, count) tuples

4.  Displaying the first 100 words

5.  Performing aggregation actions

6.  (If Time Permits) Performing key-based actions

7.  (If Time Permits) Performing numeric actions

##  Exercise 1: Mapping lines of text to a flat map of words

Open app.py in the text editor. We\'ve already created an RDD named
lines, containing all the lines of text from MacbethSnippet.txt.

Where indicated by the \"Ex 1\" comment, add code to create an RDD
containing all the words in all the lines. Here are some hints:

- Use the RDD flatMap() function, whose purpose is to map an item into a
  sequence of sub-items. In this case, it will map a line into its
  constituent words...

- flatMap() takes a lambda expression as a parameter, indicating how to
  map each item into sub-items. Implement the lambda so that it splits a
  line at the space character (call the split(\' \') function to do
  this).

The flatMap() function returns all words, including words that are
effectively empty. Call filter() to just keep the non-empty words.
You\'ll need to write a lambda that tests if a word isn\'t empty... how
can you test if a Python string isn\'t empty?

Finally, print the resultant RDD to the console, via the print()
function. In order to see the actual contents of the RDD, call collect()
on the RDD for simplicity.

Save app.py, then open a Command Prompt window in the *student* folder
and run app.py locally as follows:

## python app.py

## Verify that the application prints all the words found in the text file. Exercise 2: Creating an RDD of (word, count) tuples

In app.py, where indicated by the \"Ex 2\" comment, add code to create
an RDD containing tuples of words and word counts (i.e. the first item
in the tuple is a word, and the second item is the count of how many
times that word appears). Follow these steps:

- Call map() to map each word into a (word, count) tuple where each
  count is 1 initially.

- Call reduceByKey(), to group (key, value) tuples by *key* and then
  reduce the *values* into a single value. E.g. imagine you start off
  with the following (word, count) tuples:

  - (\"do\", 1)

  - (\"you\", 1)

  - (\"know\", 1)

  - (\"the\", 1)

  - (\"muffin\", 1)

  - (\"man\", 1)

  - (\"the\", 1)

  - (\"muffin\", 1)

  - (\"man\", 1)

  - (\"the\", 1)

  - (\"muffin\", 1)

  - (\"man\", 1)

> reduceByKey() first groups these tuples by key (i.e. word) as follows:

- (\"do\", 1)

- (\"you\", 1)

- (\"know\", 1)

- (\"the\", 1) (\"the\", 1) (\"the\", 1)

- (\"muffin\", 1) (\"muffin\", 1) (\"muffin\", 1)

- (\"man\", 1) (\"man\", 1) (\"man\", 1)

> For each different key, reduceByKey() calls the lambda expression that
> you provide, successively with each value. E.g. for the \"muffin\"
> key, it\'ll call your lambda 3 times, passing the values 1, 1, 1 each
> time.
>
> So, implement a lambda that accumulates the total word count for each
> word. The lambda receives two parameters:

- The accumulated value so far (defaults to 0 on the first call)

- The value of the next item in the key group (e.g. the value 1)

<!-- -->

- Finally call sortBy() to sort the (word, count) tuples by descending
  word count.

- Print the resultant RDD of (word, count) tuples.

## Test your new code. Exercise 3: Caching the RDD of (word, count) tuples

The exercises that follow will perform various actions on the RDD of
(word, count) tuples. Under normal circumstances, Spark would
re-evaluate all the intermediate steps to recreate the RDD ready for
each action. This is inefficient, so add code to cache the RDD of (word,
count) tuples before going any further.

## Exercise 4: Displaying the first 100 words

Where indicated by the \"Ex 4\" comment, add code to display the
first100 words. Here are some hints:

- First call take() to create an RDD containing just the first 100
  items.

- Then pass the resultant RDD to the Python print() function.

*Aside*: An alternative to take() is collect(). However, collect() might
cause the Spark driver to run out of memory, because it fetches the
entire RDD to a single machine. This is why take() is generally a safer
option, because it limits the number of items being collated.

## Exercise 5: Performing aggregation actions

Where indicated by the \"Ex 5\" comment, add code to perform the
following aggregation actions on the RDD of (word, count) tuples:

- Find the count of all items in the RDD, via the RDD count() method.
  This tells you the number of different words in MacbethSnippet.txt.

- Find the most frequent word. Use the RDD max() method to do this. Note
  the following points about the max() method:

  - The max() method takes an optional lambda expression, which allows
    you to specify how to compare items...

  - In our scenario, the RDD contains (word, count) tuples, and you want
    max() to compare element \[1\] in the tuples (i.e. the *counts*)...

  - Therefore, when you call max(), pass in a lambda that takes a (word,
    count) tuple and returns element \[1\] from the tuple.

- In the same way, find the least frequent word. Use the RDD min()
  method to do this.

##  Exercise 6 (If time permits): Performing key-based actions

Where indicated by the \"Ex 6\" comment, add code to lookup a word and
find its count. To make the application interesting, you\'ll pass in the
\"lookup words\" as command-line arguments. For example, you might run
your application as follows:

python app.py DUNCAN ACT Witch

In this case, argv contains 4 elements:

- argv\[0\]: \"app.py\"

- argv\[1\]: \"DUNCAN\"

- argv\[2\]: \"ACT\"

- argv\[3\]: \"Witch\"

Write code to iterate through argv (from element \[1\] to the end). For
each word, look it up in the (word, count) tuple. This will tell you the
occurrence count for that word. Display the results on the console.

## Exercise 7 (If time permits): Performing numeric actions

Where indicated by the \"Ex 7\" comment, add code to perform the
following numeric actions on the word counts:

- The sum of all counts (i.e. the total number of words)

- The average (mean) of all counts

- The standard deviation of all counts

- The variance of all counts

Note 1: You\'ll first need to create an RDD containing just the word
counts but not the words themselves -- how will you do this?

Note 2: Ensure that the process by which you map (word, count) tuples
isn\'t repeated each time you invoke one of the action methods.
