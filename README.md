Report Validator 📊

A Python program that reads numerical reports from a file, validates them based on specific rules, and writes the correct reports to a new file.

Description

This program processes a dataset of numerical reports and checks whether each report is valid based on:

Sorted order (ascending or descending)
Valid step differences between consecutive numbers

Valid reports are saved into a separate output file.

Validation Rules

A report is considered valid if:

The numbers are either:
strictly increasing
or strictly decreasing
The difference between every two consecutive numbers is:
greater than 0
less than 4
File Structure

.
main.py
reports.dat
correct-reports.dat
README.md

Input Format

Each line in the input file should contain integers separated by spaces.

Example:

1 2 3 5
8 6 4 3
1 4 8 9

Output

The program:

Prints the total number of reports
Prints the percentage of valid reports
Saves valid reports to correct-reports.dat

Example output file:

1 2 3 5
8 6 4 3

How to Run

python main.py

Concepts Used
File handling
Lists and loops
Data validation
Sorting
Functions
Future Improvements
Add command-line arguments for input/output files
Handle invalid data more robustly
Separate valid and invalid reports
Add unit tests
