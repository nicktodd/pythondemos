# PySpark DataFrame API Exercises

**Dataset:** `weatherWithHeader.csv` — daily weather readings with columns: `DayOfMonth`, `MinTemp`, `MaxTemp`, `Precipitation`. It is semicolon-delimited.

You can find the dataset at `demos/glue-notebooks/data/weatherWithHeader.csv`.

---

## Exercise 1 — Read and Explore
Read the CSV file into a Spark DataFrame. Make sure Spark treats the first row as a header and infers the column data types. Print the schema and display the first 10 rows.

> Hint: look at the `option()` method on the reader for `header`, `inferSchema`, and `sep`.

---

## Exercise 2 — Select and Filter
1. Select only the `DayOfMonth` and `MaxTemp` columns and display them.
2. Filter the data to show only days where `MaxTemp` was greater than 8 degrees.
3. Filter the data to show only days where `MinTemp` was below zero (i.e. a frost day).

---

## Exercise 3 — Add a Computed Column
Add a new column called `TempRange` that contains the difference between `MaxTemp` and `MinTemp` for each day. Display the result including `DayOfMonth`, `MinTemp`, `MaxTemp`, and your new `TempRange` column.

---

## Exercise 4 — Categorise with a Computed Column
Add a new column called `RainCategory` using a `when`/`otherwise` expression:
- `"Heavy"` if `Precipitation` > 20
- `"Moderate"` if `Precipitation` is between 5 and 20 (inclusive)
- `"Light"` if `Precipitation` is below 5

Display `DayOfMonth`, `Precipitation`, and `RainCategory`.

---

## Exercise 5 — Aggregations
Using the full dataset, calculate in a single query:
- The total precipitation for the period
- The average daily max temperature
- The highest max temperature recorded
- The lowest min temperature recorded
- The total number of days in the dataset

---

## Exercise 6 — Find Specific Days
1. Display the row for the day with the highest `MaxTemp`.
2. Display the row for the day with the lowest `MinTemp`.
3. Display all days where there was **no precipitation** (i.e. `Precipitation` == 0).

---

## Exercise 7 — Sort and Rank
1. Sort the DataFrame by `Precipitation` in descending order and display the top 10 wettest days.
2. Sort by `TempRange` descending (reuse your column from Exercise 3) to find the days with the biggest difference between min and max temperature.

---

## Exercise 8 — Rename and Drop
1. Rename `MinTemp` to `LowTemp` and `MaxTemp` to `HighTemp`.
2. Drop the `Precipitation` column from the DataFrame and display the result.

---

## Bonus Exercise — Descriptive Statistics
Use a single DataFrame API call to display basic statistics (count, mean, standard deviation, min, max) for `MinTemp`, `MaxTemp`, and `Precipitation`.
