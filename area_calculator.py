def calculate_square_area(side: float):
    return side * side

def calculate_rectangle_area(length: float, width: float):
    return length * width

def calculate_circle_area(radius: float):
    pi = 3.14
    return pi * (radius ** 2)

def calculate_rhombus_area(q: float, p: float):
    return (p*q)/2

print("""
----------------
Area Calculator)
----------------
Select a shape:
""")

selection = input("""
\t'S' - Square
\t'R' - Rectangle
\t'C' - Cirlce
\t'Rh' - Rhombus
""")



def calculate_area(selection):
    area = 0

    if selection == "S":
        side = input("Enter the side:")
        area = calculate_square_area(float(side))
    elif selection == "R":
        length = input("Enter the length:")
        width = input("Enter the width:")
        area = calculate_rectangle_area(float(length), float(width))
    elif selection == "C":
        radius = input("Enter the radius:")
        area = calculate_circle_area(float(radius))
    elif selection == "Rh":
        q = input("Enter the first diagonal:")
        p = input("Enter the second diagonal:")
        area = calculate_rhombus_area(float(q), float(p))
    else:
        print("Invald selection, choose 'S', 'R' or 'C'") 

    return area

def get_get_shape_name(tag):
    shape = "Unknown"
    if tag == "S":
        shape = "Square"
    elif tag == "R":
        shape = "Rectangle"
    elif tag == "C":
        shape = "Circle"
    elif tag == "Rh":
        shape = "Rhombus"
    return shape

area = calculate_area(selection)

print(f"The area of the {get_get_shape_name(selection)} is {area}")


