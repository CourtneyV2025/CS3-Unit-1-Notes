def main():
    print("hello world")

    # Declare variables
    age = 17
    teacher = "Ms. Navab"
    is_fave_class = True
    my_grade = 99.99

    # Check the type of a variable
    type_of_age = type(age)
    print(type_of_age)

    # String formatting with f-strings
    #f"String literal {variable}""
    print(f"the type of the variable age is: {type_of_age}")
    print(f"My age in 10 years: {age + 10}") 
    print() #linebreak

    # Initialize args for function
    ingredients_list = ["chocolate chips", "cinnamon", "flour", "sugar", "butter", "eggs"]
    snickerdoodle = "mix everything and put in oven. there ya go!"
    temperature = 300

    # Call a function
    bake_cookie(ingredients_list, snickerdoodle, temperature, name=recipe_name) 

    #Call a function with an optional argument 
    bake_cookie(ingredients_list, snickerdoodle, temperature, "star")
   
#You can also use the argument's keyword. This helps with readability
print(calculate_numbers(2, 3)) #goes with default, "add"
print(calculate_numbers(2, 3, "subtract")) 
print(calculate_numbers(2,3,operation="subtract")) # specify keyword

# Different ways to modify values while iterating 
# Note that you can mix data types in the same list!!!!!!
numbers = [5, 5, 6, 5.5, 7, 42, 70] 
list_interation(numbers)

    #Test differet container types
list_demo()
tuple_demo()
set_demo()
dict_demo()

def list_demo():
    print("***LIST DEMO***")
    my_list = ["h", "e", "l", "l", "o"]

    # Add an item to a list 
    my_list.append("!") 
    print(my_list)

    # Get the number of items
    print(len(my_list))

    # Use inde to access specific items
    print(my_list[0])
    print(my_list[4:6]) # item at index 4 (inclusive) until 6 (excluded)
    print(my_list[4:1]) # item at 4 until the end
    # NEGATIVE INDEX is located from the end, back 2 spots
    print(my_list[-2:1]) # item at 4 until the end 

    # Remove the first 'l'
    my_list.remove("l")
    #Insert an item at a inde
    my_list.insert(1,"l") 
    print(my_list)





def tuple_demo():
    print("***TUPLE DEMO***")

def set_demo():
    print("***SET DEMO***")

def dict_demo():
    print("***DICT DEMO***")

def bake_cookie(ingredients, instructions, temperature, cutter="circle"):

    # Print the list of ingredients 
    for item in ingredients:
        print(item)
    # Print the oven temperature setting
    print(f"Set the oven to {temperature} degrees Farenheight")

    # Print the instructions 
    print(instructions) 
    #Tell them which cookie cutter to use 
    print(f"Now cut your cookies with a {cutter} cookie cutter")
    print()

def calculate_numbers(x, y, operation="add"):
    if operation == "add":
         return x + y
    elif operation == "subtract":
         return x - y


 # Let's try our new function. Remember, if we don't pass the operation keyword argument, the 
    calculate_numbers(2,3)
# You can pass a keyword argument as a normal positional argument 
    calculate_numbers(2, 3, "subtract")



def list_interation(list): 
    # 1. Create a new list as you loop
    new_list = []    
    for item in list:
        new_list.append(item * 2)
    print(new_list)

    #2. LIST COMPREHENSION
    input_list = [item * 2 for item in list]
    print(input_list)


if __name__ == "__main__":
    main()
    # Declare Variables
    x = 42
    y = 3 /4 
    z = int('7')
    a = float(5)
    name = "Nina" 
    
    # Check the type of variable
    print(type(x))
    print(type(y))
    print(type(z))
    print(type(a))
    print(type(name))
    