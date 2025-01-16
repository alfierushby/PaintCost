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


def double_check(string):
    print(string)
    choice = get_input_choice("Is this dimension correct? (Y/N): ")
    if choice == "N":
        return False
    return True


def try_again():
    choice = get_input_choice("Do you want to try again? (Y/N): ")
    if choice == "N":
        return False
    return True


def get_general_dimension(xaxis, yaxis, area_fun):
    dimension_x = float(get_input_num(f"Enter the {xaxis} in meters: "))
    dimension_y = float(get_input_num(f"Enter the {yaxis} in meters: "))
    if double_check(f"{xaxis}: {dimension_x}m\n{yaxis}: {dimension_y}m\nArea: "
                    f"{round(area_fun(dimension_x, dimension_y),3)}m"):
        return area_fun(dimension_x, dimension_y)
    if try_again():
        return get_general_dimension(xaxis, yaxis, area_fun)
    return 0


def get_dimension(name):
    dim_response = str(input(f"Enter the shape of the {name} with the option of 'square', 'triangle', 'ellipse', "
                             f"or to cancel with 'cancel': "))
    match dim_response:
        case 'square':
            return get_general_dimension("Width", "Height", lambda x, y: x * y)
        case 'triangle':
            return get_general_dimension("Base", "Height", lambda x, y: (x * y) / 2)
        case 'ellipse':
            return get_general_dimension("A-axis", "B-axis", lambda x, y: math.pi * x * y)
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

    print(f"The total cost of your paint is: £{round(paint_area * paint_cost,2)}")
    print(f"The area to paint is: {round(paint_area,3)} square meters")
