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
    