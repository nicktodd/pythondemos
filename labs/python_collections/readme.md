# Python Collections Practice Worksheet
*Lists, Tuples, Dictionaries, and Sets*

This worksheet contains small, self-contained exercises.  
Each exercise should be completed starting from a blank Python file.

---

## 1. Lists

### Exercise 1 – Favourite Foods
Create a list of five favourite foods.

- Print the first and last item  
- Add a new food  
- Remove one food  
- Print the updated list  

### Exercise 2 – Even Numbers
Create a list of numbers.  
Make a new list containing only the even numbers.  
Print the result.

### Exercise 3 – User Numbers
Ask the user to enter five numbers (one at a time).  
Store them in a list, then print:

- The largest number  
- The smallest number  
- The average  

### Exercise 4 – Reverse a List
Reverse a list **without** using `.reverse()` or slicing (`[::-1]`).  
Use a loop to build a new reversed list.

---

## 2. Tuples

### Exercise 5 – Tuple Unpacking
Create a tuple representing a point `(x, y, z)`.  
Unpack it into three variables and print each one.

### Exercise 6 – Tuple Immutability
Create a tuple of three colours.  
Try to change one element and observe what happens.  
Then create a new tuple with one colour replaced.

### Exercise 7 – Convert List ↔ Tuple
Start with a tuple of numbers.  
Convert it to a list, add a number, then convert it back to a tuple.

---

## 3. Dictionaries

### Exercise 8 – Contact Info
Create a dictionary with keys `"name"`, `"age"`, and `"city"`.  

- Print each value  
- Add a new key `"email"`  

### Exercise 9 – Word Counter
Ask the user for a sentence.  
Count how many times each word appears using a dictionary.  
Print the dictionary.

### Exercise 10 – Student Grades
Create a dictionary mapping student names to grades.

- Print all student names  
- Print all grades  
- Add a new student  
- Update an existing grade  

### Exercise 11 – Nested Dictionary
Create a dictionary representing a book with keys:

- `"title"`  
- `"author"`  
- `"details"` (another dictionary containing `"pages"` and `"publisher"`)

Print the number of pages.

---

## 4. Sets

### Exercise 12 – Unique Numbers
Ask the user to enter 10 numbers.  
Store them in a set to remove duplicates.  
Print the set.

### Exercise 13 – Set Operations
Create two sets of numbers.  
Print:

- The union  
- The intersection  
- The difference  

### Exercise 14 – Duplicate Check
Given a list of items, use a set to check whether any duplicates exist.  
Print a message indicating whether duplicates were found.

### Exercise 15 – Remove Duplicates (Keep Order)
Given a list with duplicates, create a new list with duplicates removed **while keeping the original order**.

---

## 5. Mixed Collection Exercises

### Exercise 16 – Shopping Basket
Create a list of items in a shopping basket.  
Convert it to a set to remove duplicates.  
Convert it back to a list and sort it.

### Exercise 17 – Student Registry
Create a dictionary where each key is a student name and each value is a tuple containing `(age, city)`.  
Add two students and print their information.

### Exercise 18 – Word Lengths
Given a list of words, create a dictionary mapping each word to its length.

### Exercise 19 – Number Categories
Given a list of numbers, create:

- A set of unique numbers  
- A list of even numbers  
- A dictionary with keys `"positive"` and `"negative"` mapping to lists of numbers  

### Exercise 20 – Menu Lookup
Create a dictionary representing a menu (item → price).  
Ask the user to enter an item name.  
If it exists, print the price; otherwise print `"Not on the menu"`.
