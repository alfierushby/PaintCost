import math

def get_input_num(string):
    val = input(string)
    # Make sure it's a number being entered
    try:
        val = float(val)
    except ValueError:
        try:
            val = int(val)
        except ValueError:
            print("Please enter a number")
            return get_input_num(string)
    # Make sure a positive number is being entered
    if val < 0:
        print("Please enter a positive number")
        return get_input_num(string)
    return val

def get_input_choice(string):
    val = str(input(string))
    try:
        val = val.upper()
    except ValueError:
        print("Please enter a valid choice")
        get_input_choice(string)

    if val != "Y" and val != "N":
        print("Please enter a valid choice")
        get_input_choice(string)
    return val
def get_named_dimension_square(name):
    dimension_base = float(get_input_num(f"Enter the width of the {name} in meters: "))
    dimension_height = float(get_input_num(f"Enter the height of the {name} in meters: "))
    return dimension_base * dimension_height

def get_named_dimension_triangle(name):
    dimension_base = float(get_input_num(f"Enter the base of the {name} in meters: "))
    dimension_height = float(get_input_num(f"Enter the height of the {name} in meters: "))
    return (dimension_base * dimension_height) / 2

def get_named_dimension_ellipse(name):
    dimension_base = float(get_input_num(f"Enter the a-axis of the {name} in meters: "))
    dimension_height = float(get_input_num(f"Enter the b-axis of the {name} in meters: "))
    return math.pi * dimension_base * dimension_height

def get_dimension(name):
    dim_response = str(input(f"Enter the shape of the {name} with the option of 'square', 'triangle', 'ellipse', "
                             f"or to go cancel with 'cancel': "))
    match dim_response:
        case 'square':
            return get_named_dimension_square(name)
        case 'triangle':
            return get_named_dimension_triangle(name)
        case 'ellipse':
            return get_named_dimension_ellipse(name)
        case 'cancel':
            return 0
        case _:
            get_dimension(name)

if __name__ == '__main__':
    print("This program will calculate the cost of painting a room.")
    print("You will choose the number of walls to paint and their dimensions, whether you want to paint your ceiling "
          "and its dimension, and any obstructions that you won't paint on your walls and ceiling.")
    paint_cost = float(get_input_num("Enter the cost of your paint per square meter: "))
    paint_area = 0

    while True:
        response = get_input_choice("Do you want to add a wall? (Y or N): ")
        if response == "N":
            break
        paint_area += get_dimension("wall")

    response = get_input_choice("Do you want to add the ceiling? (Y or N): ")
    if response == "Y":
        paint_area += get_dimension("Ceiling")

    response = get_input_choice("Do you want to add any obstructions that you won't paint? (Y or N): ")
    if response == "Y":

        while True:
            paint_area -= get_dimension("obstruction")
            response = get_input_choice("Do you want to add another obstruction? (Y or N): ")
            if response == "N":
                break

    print(f"The total cost of your paint is: £{paint_area * paint_cost}")
    print(f"The area to paint is: {paint_area} square meters")
