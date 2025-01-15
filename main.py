def get_named_dimension_square(name):
    wall_dimension_x = int(input(f"Enter the width of the {name} in meters: "))
    wall_dimension_y = int(input(f"Enter the height of the {name} in meters: "))
    return wall_dimension_x * wall_dimension_y


if __name__ == '__main__':
    paint_cost = float(input("Enter the cost of your paint per square meter: "))
    paint_area = 0

    walls = True

    while walls:
        paint_area += get_named_dimension_square("wall")
        response = str(input("Do you want to add another wall? (Y or N)")).upper()
        if response == "N":
            walls = False

    response = str(input("Do you want to add the ceiling? (Y or N)")).upper()
    if response == "Y":
        paint_area += get_named_dimension_square("Ceiling")

    response = str(input("Do you want to add any obstructions on your walls that you won't paint? (Y or N)")).upper()
    if response == "Y":
        obstructions = True
        while obstructions:
            paint_area -= get_named_dimension_square("obstruction")
            response = str(input("Do you want to add another obstruction? (Y or N)")).upper()
            if response == "N":
                obstructions = False

    print(f"The total cost of your paint is: {paint_area*paint_cost}")