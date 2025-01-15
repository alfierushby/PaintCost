def get_named_dimension(name):
    wall_dimension_x = int(input(f"Enter the width of the {name} in meters: "))
    wall_dimension_y = int(input(f"Enter the height of the {name} in meters: "))
    return wall_dimension_x * wall_dimension_y


if __name__ == '__main__':
    paint_cost = float(input("Enter the cost of your paint per square meter: "))
    paint_area = 0
    obstruction_area = 0

    walls = True

    while walls:
        paint_area += get_named_dimension("wall")
        response = str(input("Do you want to add another wall? (Y or N)")).upper()
        if response == "N":
            walls = False

    paint_area += get_named_dimension("Ceiling")

