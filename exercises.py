
# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.
def manage_students():
    students = ["teddy", "bob", "steve", "jim", "greg"]
    first_student = students[0]
    last_student = students[-1]
    return f"First: {first_student}, Last: {last_student}"

# Call the function and print the result
print('Exercise 1:', manage_students())

# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

def combine_foods():
    foods = ("pizza", "burger", "pasta", "salad", "sushi")
    meal = ""
    for food in foods:
        meal += food + " "
    return meal

print('Exercise 2:', combine_foods())



# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food strings in the foods to a variable named last_two_foods.



def slice_foods():
    foods = ("pizza", "burger", "pasta", "salad", "sushi")
    last_two_foods = foods[-2:]
    return last_two_foods

# Call the function and print the result
print('Exercise 3:', slice_foods())
print('Exercise 3:', slice_foods())

# Exercise 5: Iterating Over Dictionary Items



# Define an empty list named home_town_items.
# Use a for loop to iterate over the key: value pairs in the home_town dictionary and append a string with the following format to home_town_items: "<key> = <value>"
def list_home_town_items():
    home_town = {
        "city": "Austin",
        "state": "Texas",
        "population": "950000"
    }
    home_town_items = []
    for key, value in home_town.items():
        home_town_items.append(f"{key} = {value}")

    return home_town_items

print('Exercise 5:', list_home_town_items())
