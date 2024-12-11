area_square = lambda side: side * side
area_rectangle = lambda length, width: length * width
area_triangle = lambda base, height: 0.5 * base * height
while True:
    print("\nChoose a shape to calculate the area:")
    print("1. Square")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Exit")
    choice = input("Enter choice (1/2/3/4): ")
    if choice == '1':
        side = float(input("Enter the side length of the square: "))
        print(f"The area of the square is: {area_square(side)}")
    elif choice == '2':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print(f"The area of the rectangle is: {area_rectangle(length, width)}")
    elif choice == '3':
        base = float(input("Enter the base length of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print(f"The area of the triangle is: {area_triangle(base, height)}")
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option.")
