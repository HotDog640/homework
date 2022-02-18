# Pg 46
# 1: A test case is a set of conditions/inputs to test a piece of code.
# 2: See if there are any errors or bad logic in the code.
# 3: Test ID, test description, test data, expected result, actual result, passed.
# 4: The expected value is the value that you want the code to produce. The actual value is the value that the code actually produced.
# 5: The expeced result must not be taken from the code being tested, and instead calculated independently.
# 6: The extent to which all possible conditions or inputs have been tested.
# 7: Areas of code that should have the same behaviour.
# 8: Testing alues you wouldn't normally expect to be inputted, such as really high, really small, or negative values.
# 9: Inputs that are at the boundary of a condition.
# 10: Anticipating user conditions or inputs that could result in an error.
# 11: Having a negative number as age.
# 12: To ensure the logic is sound in code, and that there are no errors

# Tasks
# Q1
age = int(input("Please enter your age: "))
if age >= 17:
    print("You are eligible")
else:
    print("You are not eligible")
    
# Input | Expected result | Actual result | Passed
# 1     | not eligible    | not eligible  | Y
# 2     | not eligible    | not eligible  | Y
# 18    | eligible        | eligible      | Y
# 19    | eligible        | eligible      | Y
# 17    | eligible        | eligible      | Y