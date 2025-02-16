# Python: Handling Empty Lists and Non-Numeric Elements in Average Calculation

This repository demonstrates a common error in Python: handling empty lists and lists containing non-numeric elements when calculating the average. The `bug.py` file contains code that does not handle these cases correctly, leading to errors. The `bugSolution.py` file provides a corrected version that addresses these issues.

## Bug Description

The original code does not handle cases where the input list is empty or contains non-numeric elements.  This leads to either a `ZeroDivisionError` (empty list) or a `TypeError` (non-numeric elements). 

## Solution

The solution implements error handling to gracefully manage these scenarios: 
- Check if the list is empty before performing calculations.
- Use a `try-except` block to catch `TypeError` if a non-numeric element is encountered. 

This improved code ensures the function works correctly even with unexpected inputs.