def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average = calculate_average(my_empty_list)
print(f"The average is: {average}") # This will print 0

my_list_with_zero = [1, 0, 3, 4, 5]
average = calculate_average(my_list_with_zero)
print(f"The average is: {average}")

my_list_with_string = [1,2,'a',4,5]
average = calculate_average(my_list_with_string)
print(f"The average is: {average}") #This will throw TypeError